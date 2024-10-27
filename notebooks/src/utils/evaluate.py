from nltk.translate.bleu_score import sentence_bleu

def evaluateAnswer(reference_answer, generated_answer):
    bleu_score = sentence_bleu([reference_answer.split()], generated_answer.split())
    return{"Score": bleu_score, "Feedback": "The answer is relatively close!"}