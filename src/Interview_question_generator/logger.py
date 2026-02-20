import logging
import os
from datetime import datetime

# Create a unique log file name based on current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a 'logs' directory in the root of your project
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

# Combine path and file name
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging format
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# You can test it by running: python src/Interview_question_generator/logger.py
if __name__ == "__main__":
    logging.info("Logging has started successfully.")