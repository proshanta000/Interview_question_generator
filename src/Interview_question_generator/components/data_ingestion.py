import os
import sys
from langchain_community.document_loaders import PyPDFLoader
from src.Interview_question_generator.logger import logging
from src.Interview_question_generator.exception import CustomException

class DataIngestion:
    def __init__(self):
        """
        Configuration for data ingestion. 
        It points to the directory where Flask saves uploaded files.
        """
        self.data_path = os.path.join("data", "input_file.pdf")

    def initiate_data_ingestion(self):
        """
        Loads the PDF from the data folder and returns document objects.
        """
        logging.info("Entered the data ingestion method")
        try:
            if not os.path.exists(self.data_path):
                raise FileNotFoundError(f"No file found at {self.data_path}")

            logging.info(f"Loading PDF file from: {self.data_path}")
            loader = PyPDFLoader(self.data_path)
            
            # Load and split into pages
            docs = loader.load()
            
            logging.info(f"Successfully loaded {len(docs)} pages from the PDF")
            return docs

        except Exception as e:
            logging.error("Exception occurred during Data Ingestion")
            raise CustomException(e, sys)