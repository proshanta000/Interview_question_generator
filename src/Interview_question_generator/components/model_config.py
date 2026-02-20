import os
import sys
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from src.Interview_question_generator.exception import CustomException
from src.Interview_question_generator.logger import logging

class ModelProvider:
    def __init__(self):
        self.llm_model = "llama-3.1-8b-instant"
        self.embedding_model = "sentence-transformers/all-MiniLM-L6-v2"

    def get_llm(self, temperature=0.3):
        """
        Initializes and returns the Groq Chat model.
        """
        try:
            logging.info(f"Initializing Groq LLM: {self.llm_model}")
            api_key = os.getenv("GROQ_API_KEY")
            
            if not api_key:
                raise ValueError("GROQ_API_KEY not found in environment variables")

            llm = ChatGroq(
                groq_api_key=api_key,
                model_name=self.llm_model,
                temperature=temperature
            )
            return llm
        except Exception as e:
            raise CustomException(e, sys)

    def get_embeddings(self):
        """
        Initializes and returns the HuggingFace Embeddings model.
        """
        try:
            logging.info(f"Initializing Embeddings: {self.embedding_model}")
            embeddings = HuggingFaceEmbeddings(model_name=self.embedding_model)
            return embeddings
        except Exception as e:
            raise CustomException(e, sys)