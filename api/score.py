from nltk.translate.bleu_score import sentence_bleu
from api.logging_config import logger

def compute_bleu_score(reference_answer, generated_answer):
    """
        compute_bleu_score computes the similarity score using sentence_bleu
        :reference_answer: the correct or truthful answer 
        :generated_answer: the answer generated by our LLM
    """
    # calculating the bleu score
    bleu_score = sentence_bleu([reference_answer.split()], generated_answer.split())

    feedback = "Generated answer covers most aspects of the question!"
    
    logger.info(f"The score is {bleu_score}")

    return bleu_score, feedback