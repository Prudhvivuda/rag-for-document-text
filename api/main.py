# api/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from .model_integration import generate_answer
from .similarity import compute_similarity_score
from .model_integration import build_index

app = FastAPI()
# import zipfile
# with zipfile.ZipFile("db/renewable-energy.zip","r") as zip_ref:
#     zip_ref.extractall("db/renewable-energy")
    
documents_folder = "db/renewable-energy/renewable-energy/"
index = build_index(documents_folder)

# with open("db/document_index.json") as f:
#     document_index = json.load(f)
    
class QuestionInput(BaseModel):
    question: str

class EvaluationInput(BaseModel):
    question: str
    reference_answer: str
    generated_answer: str

@app.post("/upload")
async def upload_document(question_input: QuestionInput):
    question = question_input.question
    answer, relevant_docs = generate_answer(question, index)
    return {"answer": answer, "generated_docs": relevant_docs}

@app.post("/evaluate")
async def evaluate_answer(evaluation_input: EvaluationInput):
    score, feedback = compute_similarity_score(
        evaluation_input.reference_answer,
        evaluation_input.generated_answer
    )
    return {"score": score, "feedback": feedback}
