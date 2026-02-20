import os
import sys
from langchain_community.vectorstores import FAISS
from src.Interview_question_generator.logger import logging
from src.Interview_question_generator.exception import CustomException
from src.Interview_question_generator.components.model_config import ModelProvider

class ModelTrainer:
    def __init__(self):
        """
        Initializes the ModelTrainer with the centralized ModelProvider.
        """
        self.model_provider = ModelProvider()
        self.vector_store_path = os.path.join("vectorstore", "faiss_index")

    def initiate_model_trainer(self, text_chunks):
        """
        Converts text chunks into a FAISS vector store and saves it locally.
        """
        logging.info("Entered the initiate_model_trainer method")
        try:
            # Get embeddings from the centralized provider
            embeddings = self.model_provider.get_embeddings()
            
            logging.info("Creating FAISS vector store from text chunks...")
            vector_db = FAISS.from_documents(text_chunks, embeddings)
            
            # Save the index to the vectorstore/ directory
            os.makedirs(os.path.dirname(self.vector_store_path), exist_ok=True)
            vector_db.save_local(self.vector_store_path)
            
            logging.info(f"Vector store saved successfully at {self.vector_store_path}")
            return vector_db

        except Exception as e:
            logging.error("Error occurred in Model Trainer component")
            raise CustomException(e, sys)