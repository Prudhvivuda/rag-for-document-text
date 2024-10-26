# api/similarity.py
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def compute_similarity_score(reference, generated):
    # Compute similarity (example using TF-IDF and cosine similarity)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([reference, generated])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    feedback = "Generated answer covers most aspects of the question."
    return score, feedback
