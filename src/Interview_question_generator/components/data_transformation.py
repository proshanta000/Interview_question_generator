import os
import sys
from dataclasses import dataclass
# Updated import
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from src.Interview_question_generator.logger import logging
from src.Interview_question_generator.exception import CustomException

@dataclass
class DataTransformationConfig:
    chunk_size: int = 1000
    chunk_overlap: int = 200

class DataTransformation:
    def __init__(self):
        self.transformation_config = DataTransformationConfig()

    def initiate_data_transformation(self, documents):
        logging.info("Starting Data Transformation (Text Splitting)")
        try:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=self.transformation_config.chunk_size,
                chunk_overlap=self.transformation_config.chunk_overlap
            )
            
            chunks = text_splitter.split_documents(documents)
            logging.info(f"Created {len(chunks)} chunks from documents.")
            return chunks

        except Exception as e:
            raise CustomException(e, sys)