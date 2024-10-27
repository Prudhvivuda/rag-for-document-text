from fastapi import FastAPI, HTTPException
from api.logging_config import logger
from fastapi.responses import PlainTextResponse
from .score import compute_bleu_score
from .model_integration import generate_answer
from .models import Question, EvaluationInput
from db.document_parser import parse_documents
import nltk
# nltk.download('punkt_tab')

# Instantiate the FastAPI class 
app = FastAPI()


# API to upload documents
@app.post("/upload", response_class=PlainTextResponse)
async def upload_document():
    # call pase_documents to parse the documents
    response = parse_documents()
    return response


# API to query the model
@app.post("/query")
async def user_query(input_question: Question):

    # get the question from the user input
    question = input_question.question
    logger.info(f"The question is - {question}")

    # call generate_answer to invoke the model
    answer, relevant_documents = generate_answer(question)

    # build the response with answer and relevant documents
    return {
        "answer": answer,
        "sourceDocuments": relevant_documents
    }


# API to evaluate the response
@app.post("/evaluate")
async def evaluate_answer(evaluation_input: EvaluationInput):

    # call the function compute_bleu_score to get the bleu score
    score, feedback = compute_bleu_score(
        evaluation_input.reference_answer,
        evaluation_input.generated_answer
    )

    # build the response with bleu score and feedback
    return {
        "score": score,
        "feedback": feedback
    }

