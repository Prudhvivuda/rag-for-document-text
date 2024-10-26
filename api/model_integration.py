# api/model_integration.py

import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import ollama
import os
from nltk.tokenize import word_tokenize
from rank_bm25 import *
from db.document_parser import parse_documents

documents_folder = "db/energy-docs/renewable-energy"

# Load preprocessed document index
with open("db/document_index.json") as f:
    data = json.load(f)
    index = data["index"]
    doc_texts = data["texts"]
    doc_ids = data["ids"]
    
def build_index(documents_folder):
    documents = parse_documents(documents_folder)
    corpus = [word_tokenize(doc.lower()) for doc in documents.values()]
    bm25 = BM25Okapi(corpus)
    index = {"bm25": bm25, "document_ids":list(documents.keys()), "corpus": corpus}
    return index

# Vectorizer for transforming documents and query for similarity matching
# vectorizer = TfidfVectorizer().fit(doc_texts)
# doc_vectors = vectorizer.transform(doc_texts)

def retrieve_documents(query, index, top_k=3):
    # query_vector = vectorizer.transform([query])
    # similarities = cosine_similarity(query_vector, doc_vectors).flatten()
    # relevant_indices = similarities.argsort()[-top_k:][::-1]
    # relevant_docs = [(doc_ids[i], index[doc_ids[i]]) for i in relevant_indices]
    # return relevant_docs
    
    tokenized_query = word_tokenize(query.lower())
    bm25 = index['bm25']
    scores = bm25.get_scores(tokenized_query)
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]
    top_docs = [index['document_ids'][i] for i in top_indices]
    return top_docs

def generate_answer(question, index):
    relevant_docs = retrieve_documents(question, index)
    
    combined_docs = ""
    for doc_id in relevant_docs:
        with open(f"db/renewable-energy/renewable-energy/{doc_id}.txt", 'r') as file:
            combined_docs += file.read() + "\n"

        prompt = (
        f"Please answer the following question based on the provided documents.\n\n"
        f"Question: {question}\n\n"
        f"Documents:\n{combined_docs}\n\n"
    )
    
    response = ollama.chat(
            model='mistral', 
            messages=[{'role': 'user', 'content': prompt}]
        )
    
    # Assuming `response` contains generated text in desired format
    answer = response['message']['content'] if response and 'message' in response else "No answer generated."
    print(answer)
    doc_ids = [doc[0] for doc in relevant_docs]

    return answer, doc_ids

