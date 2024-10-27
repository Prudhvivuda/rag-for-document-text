from utils.retrieve_docs import retrieveDocuments
import ollama

def answerQuestion(question, index):
    
    # retrieve top documents based on the query
    top_docs = retrieveDocuments(question, index)

    # combine content of top documents
    combined_docs = ""
    for doc_id in top_docs:
        with open(f"../renewable-energy/renewable-energy/{doc_id}.txt", 'r') as file:
            combined_docs += file.read() + '\n'

    # create a prompt using the documents and question from the user
    prompt = (
        f"Please answer the following question based on the provided documents.\n\n"
        f"Question: {question}\n\n"
        f"Documents: {combined_docs}"
    )

    # using try for exception handling
    try:
        response = ollama.chat(
            model = 'mistral',
            messages = [{'role': 'user', 'content': prompt}]
        )
        # extract or parse required content from the response
        answer = response['message']['content'] if response and 'message' in response else 'No answer generated.'
        
    except Exception as e:
        print("Exception occurred!", e)
        answer = "Error in generating answer"

    # return the repsonse in json which includes answer and top_docs 
    return {"Answer": answer, "SourceDoc": top_docs}