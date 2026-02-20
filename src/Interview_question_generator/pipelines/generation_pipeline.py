import sys
from concurrent.futures import ThreadPoolExecutor
from langchain_core.output_parsers import StrOutputParser
from src.Interview_question_generator.logger import logging
from src.Interview_question_generator.exception import CustomException
from src.Interview_question_generator.components.data_ingestion import DataIngestion
from src.Interview_question_generator.components.data_transformation import DataTransformation
from src.Interview_question_generator.components.model_config import ModelProvider
from src.Interview_question_generator.utils.prompts import MAP_PROMPT, REDUCE_PROMPT

class GenerationPipeline:
    def __init__(self):
        self.model_provider = ModelProvider()
        self.llm = self.model_provider.get_llm()
        self.parser = StrOutputParser()

    def run_pipeline(self, no_of_questions=10):
        logging.info(f"Starting Map-Reduce Pipeline for {no_of_questions} questions")
        try:
            # 1. Prepare Data
            ingestion = DataIngestion()
            raw_docs = ingestion.initiate_data_ingestion()
            
            transformation = DataTransformation()
            chunks = transformation.initiate_data_transformation(raw_docs)

            # 2. MAP PHASE (Parallel Execution)
            map_chain = MAP_PROMPT | self.llm | self.parser
            logging.info(f"Mapping {len(chunks)} chunks in parallel...")

            with ThreadPoolExecutor() as executor:
                # We send all chunks to the LLM at once
                map_results = list(executor.map(
                    lambda chunk: map_chain.invoke({"text": chunk.page_content}), 
                    chunks
                ))

            # 3. REDUCE PHASE (Consolidation)
            logging.info("Reducing questions to final list...")
            combined_questions = "\n".join(map_results)
            
            reduce_chain = REDUCE_PROMPT | self.llm | self.parser
            final_questions = reduce_chain.invoke({
                "combined_questions": combined_questions,
                "no_of_questions": no_of_questions
            })

            logging.info("Generation Pipeline completed successfully")
            return final_questions, chunks

        except Exception as e:
            raise CustomException(e, sys)