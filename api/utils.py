from nltk.tokenize import word_tokenize
from rank_bm25 import *

def build_index(document_ids_and_content):
    """
        This function helps to build index
        :document_ids_and_content: is a dictionary with file name as the key and content as the value.
    """
    # word tokenize the content in the document_ids_and_content
    corpus = [word_tokenize(doc.lower()) for doc in document_ids_and_content.values()]

    # BM25Okapi uses set of algorithms to find the most relevant items
    bm25 = BM25Okapi(corpus)

    # create response body and return
    index = {
        "bm25": bm25,
        "document_ids": list(document_ids_and_content.keys()),
        "corpus": corpus
    }
    return index

def retrieve_documents(question, document_ids_and_content):
    """
        retreive_document function retrieves the top 3 documents and return them.
        :question: is the user input question
        :document_ids_and_content: is a dictionary with file name as the key and content as the value.
    """
    # call build_index function to get the index
    index = build_index(document_ids_and_content)

    # build a tokenized query using word tokenizer
    tokenized_query = word_tokenize(question.lower())

    # retreive the object bm25 from the index returned by the build_index function
    bm25 = index['bm25']

    # get the scores
    scores = bm25.get_scores(tokenized_query)

    # sort and get the top 3 most relevant indices
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]

    # get the document_ids for the top 3 indices
    top_documents = [index['document_ids'][i] for i in top_indices]

    # returning the top 3 documents as the response
    return top_documents