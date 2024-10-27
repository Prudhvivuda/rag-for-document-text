from .parse_docs import parseDocuments
from nltk.tokenize import word_tokenize
from rank_bm25 import *

def buildIndex(documents_folder):

    # parse the documents 
    documents = parseDocuments(documents_folder)

    # convert all text into lowercase and word_tokenize them
    corpus = [word_tokenize(doc.lower()) for doc in documents.values()]

    # use bm25O to to query the corpus and returns relevant ones
    bm25 = BM25Okapi(corpus)

    # create the response object called index
    index = {"bm25": bm25, "document_ids":list(documents.keys()), "corpus": corpus}
    
    return index