from flask import Flask, render_template, request
import os
import sys
from src.Interview_question_generator.pipelines.generation_pipeline import GenerationPipeline
from src.Interview_question_generator.components.model_trainer import ModelTrainer
from src.Interview_question_generator.pipelines.rag_pipeline import RAGPipeline
from src.Interview_question_generator.exception import CustomException
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
os.makedirs('data', exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        file = request.files['pdf_file']
        user_count = request.form.get('no_of_questions', 10)
        
        if file.filename == '':
            return "No file selected"

        pdf_path = os.path.join("data", "input_file.pdf")
        file.save(pdf_path)

        # 1. Generate Questions using Map-Reduce
        gen_pipeline = GenerationPipeline()
        raw_questions, chunks = gen_pipeline.run_pipeline(no_of_questions=user_count)
        
        # 2. Train Vector Store
        trainer = ModelTrainer()
        vector_db = trainer.initiate_model_trainer(chunks)

        # 3. Get Answers via RAG
        rag_pipeline = RAGPipeline(vector_db)
        questions, answers = rag_pipeline.get_answers(raw_questions)

        return render_template('result.html', result=zip(questions, answers))

    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)