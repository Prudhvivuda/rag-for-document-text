from pydantic import BaseModel

# Input model for the query call
class Question(BaseModel):
    question: str

# Input model for the evaluate call
class EvaluationInput(BaseModel):
    question: str
    reference_answer: str
    generated_answer: str