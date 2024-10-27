from nltk.tokenize import word_tokenize

def retrieveDocuments(question, index):

    # create a word_tokenized query
    tokenized_query = word_tokenize(question.lower())

    # fetch the key bm25 from the index object
    bm25 = index['bm25']

    # fetch scores from bm25
    scores = bm25.get_scores(tokenized_query)

    # get the top 3 relevant documents
    top_indices = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:3]
    top_docs = [index['document_ids'][i] for i in top_indices]
    
    return top_docs