import sys
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from src.Interview_question_generator.logger import logging
from src.Interview_question_generator.exception import CustomException
from src.Interview_question_generator.components.model_config import ModelProvider
from src.Interview_question_generator.utils.prompts import RAG_PROMPT

class RAGPipeline:
    def __init__(self, vector_store):
        """
        Initializes the RAG pipeline with the local vector store.
        """
        self.model_provider = ModelProvider()
        self.llm = self.model_provider.get_llm()
        self.retriever = vector_store.as_retriever(search_kwargs={"k": 3})
        self.parser = StrOutputParser()

    def get_answers(self, question_list_string):
        """
        Takes the raw string of questions, parses them, and finds answers for each.
        """
        logging.info("Starting RAG process to find answers")
        try:
            # 1. Clean and split the questions into a Python list
            # Removes empty lines and numbering (like 1., 2.)
            questions = [
                q.split('.', 1)[-1].strip() if '.' in q else q.strip() 
                for q in question_list_string.split('\n') 
                if q.strip() and ('?' in q or len(q) > 10)
            ]

            # 2. Define the LCEL Chain
            rag_chain = (
                {"context": self.retriever, "question": RunnablePassthrough()}
                | RAG_PROMPT
                | self.llm
                | self.parser
            )

            logging.info(f"Finding answers for {len(questions)} questions...")
            
            answers = []
            for q in questions:
                ans = rag_chain.invoke(q)
                answers.append(ans)

            return questions, answers

        except Exception as e:
            logging.error("Error in RAG Pipeline")
            raise CustomException(e, sys)