import json
import ollama
from db.document_parser import parse_documents
from .utils import retrieve_documents

with open('db/document_ids_and_content.json', 'r') as file:
    # Load the JSON data into a dictionary
    document_ids_and_content = json.load(file)

def generate_answer(question):
    """
        This function generate_answer generates the answer using the Mistral 7B LLM and return the 
        answer which is generated along with the document ids used for the generation.
        :question: input question from the user
    """
    # get the most relevant top 3 documents 
    relevant_documents = retrieve_documents(question, document_ids_and_content)
    
    # combine the content from the relevant documents to send to the llm
    combined_documents = ''
    for document_id in relevant_documents:
        combined_documents += document_ids_and_content[document_id] + '\n'
    
    # build the prompt using the question, relavant documents and any other requied information
    prompt = (
        f"Please answer the question based on the provided documents.\n\n"
        f"Question: {question}\n\n"
        f"Documents: \n{combined_documents}\n"
    )

    # invoke the mistral model by calling ollama.chat and sending the prompt
    response = ollama.chat(
        model='mistral',
        messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ]
    )

    # parse the generated answer
    generated_answer = response['message']['content'] if response and 'message' in response else "No answer is generated."

    # get the relevant documents for this answer generation by llm
    documents_ids = [doc[0] for doc in relevant_documents]

    return generated_answer, documents_ids