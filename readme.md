# Retrieval Augmented Generation Backend System

## Introduction
This a python based backend system that supports a Retrieval-Augmented Generation (RAG) model using Ollama with
Mistral 7B model and the model runs locally and fully offline built usinf FastAPI framework. The backend will manage document processing, query handling, and AI model integration to provide automated responses based on renewable energy documents.
The entire code is in the `rag-server` folder.

## Project Structure
This project contains three folders `api`, `db` and `tests`

/api: for the backend API code and model integration logic.
- main.py: instantiates FastAPI and routes requests based on the endpoint
- model_integration.py: contains the main logic to integrate with LLM and calling the model
- score.py: computes the bleu_score
- utils.py: contains the functions to build_index and retrieve_documents
- logging_config.py: contains the template for the logging used across this project
- models.py: contains the models for user input

/db: for database and document processing scripts
- document_parser.py: contains the parsing logic
- document_ids_and_content.json: a json with file ids as keys and contents as values
- renewable_energy: root folder for the db
    - renewable_energy: contains 30 text files used in building the RAG
        - 1.txt
        - 2.txt
        - ...
    
/tests
- test_evaluate.py: evaluate api testcase
- test_query.py: query api testcase
- test_upload.py: upload api testcase
- test_fail_evaluate.py: failure testcase for evaluate api
- test_fail_query.py: failute testcase for query api

readme.md: documentation of the rentire project continaing the setup instructions and api usage examples.

requirements.txt: requirements documents which contains the essential libraries to run this project

## Installation and Setup Instructions

Install and activate the virual environment using below commands

- `pip install vistualenv`
- `virtualenv .rangenv`

To install the project requirements, run the command:

- `pip install -r requirements.txt`

To download and install the ollama, please run the command:

- `curl -fsSL https://ollama.com/install.sh | sh`

To use mistral, please run the command:

- `ollama pull mistral`

To run the ollama, please run the below command and let it run in a new terminal until you want to close the server.

- `ollama serve`

To download the dataset, please run in a terminal:

- `wget https://storage.googleapis.com/ds--tasks-datasets/renewable-energy.zip`

To run the backend server, please run the command and it runs on 0.0.0.0:5000:

- `uvicorn api.main:app --host 0.0.0.0 --port 5000`

To run any sample test case and see the output, run the below command:

- `python api/test_cases.py`

## Testing

Test cases are written using `pytest` framework. 

To run all the testcases at once, please run the command in the terminal:

- `pytest tests/`

To run any individual testcases, use the below commands

- `pytest tests/test_evaluate.py`
- `pytest tests/test_upload.py`
- `pytest tests/test_query.py`
- `pytest tests/test_fail_query.py`
- `pytest tests/test_fail_evaluate.py`

The above test cases also contains a couple of failure testcases as well which should not pass and intentionally designed to fail.

## API Usage Examples

### 1. /query api

Run this cURL on terminal and change the data field to your desired question to check the response of the query API.

- `curl -X POST -H "Content-Type: application/json" -d '{"question": "Which policies guarantee a fixed price for electricity generated from renewable sources?"}' http://0.0.0.0:5000/query`

- `curl -X POST -H "Content-Type: application/json" -d '{"question": "What are the two key areas making solar energy more powerful and accessible?"}' http://0.0.0.0:5000/query`

Input 1:

- `{"question": "Which policies guarantee a fixed price for electricity generated from renewable sources"}`

Output 1:
- `{"answer":" The policy that guarantees a fixed price for electricity generated from renewable sources is called \"Feed-in tariffs\". This policy can be found in various documents you've provided: Pushing the Green Button, Policies Powering the Path to Renewables, and Policies Propelling Progress. Feed-in tariffs are highlighted as a key incentive for investment in renewable energy and provide long-term financial certainty, encouraging the development of renewable energy sources.","sourceDocuments":["2","2","2"]}`

Input 2:

- `{"question": "What are the two key areas making solar energy more powerful and accessible?"}`

Output 2:

- `{"answer":" The two key areas making solar energy more powerful and accessible are efficiency and materials. Efficiency advancements involve improving the ability of solar panels to convert sunlight into electricity, such as the development of bifacial solar panels and refined cell designs. Material advancements include exploring new materials like perovskites and organic semiconductors for creating even more efficient solar cells. These improvements are expected to make solar power more attractive for individuals and businesses alike.","sourceDocuments":["3","1","1"]}`

### 2. /evaluate api

Run this cURL interminal and change the data field to your desired question and answers to check the response of the evaluate API.

- `curl -X POST -H "Content-Type: application/json" -d '{"question": "What are the latest innovations in renewable energy?", "reference_answer": "Feed-in tariffs policies guarantee a fixed price for electricity generated from renewable sources.", "generated_answer":"The policy that guarantees a fixed price for electricity generated from renewable sources is called Feed-in tariffs."}' http://0.0.0.0:5000/evaluate`

- `curl -X POST -H "Content-Type: application/json" -d '{"question": "What are the two key areas making solar energy more powerful and accessible?", "reference_answer": "The two key areas making solar energy more powerful and accessible are efficiency and materials.", "generated_answer":"The two key areas making solar energy more powerful and accessible are efficiency and materials. Efficiency advancements involve improving the ability of solar panels to convert sunlight into electricity, such as the development of bifacial solar panels and refined cell designs."}' http://0.0.0.0:5000/evaluate`

Input 1:

- `{"question": "Which policies guarantee a fixed price for electricity generated from renewable sources?", "reference_answer": "Feed-in tariffs policies guarantee a fixed price for electricity generated from renewable sources.", "generated_answer":"The policy that guarantees a fixed price for electricity generated from renewable sources is called \"Feed-in tariffs\". This policy can be found in various documents you've provided: Pushing the Green Button, Policies Powering the Path to Renewables, and Policies Propelling Progress."}`

Output 1:

- `{"score":0.42649937722961534,"feedback":"Generated answer covers most aspects of the question!"}`

Input 2:

- `{"question": "What are the two key areas making solar energy more powerful and accessible?", "reference_answer": "The two key areas making solar energy more powerful and accessible are efficiency and materials.", "generated_answer":"The two key areas making solar energy more powerful and accessible are efficiency and materials. Efficiency advancements involve improving the ability of solar panels to convert sunlight into electricity, such as the development of bifacial solar panels and refined cell designs."}`

Output 2:

- `{"score":0.34073202973754074,"feedback":"Generated answer covers most aspects of the question!"}`

### 3. /upload api

Run this cURL in the terminal to check the response of the upload API.

Input:

- `curl -X POST -H "Content-Type: application/json" http://0.0.0.0:5000/upload`

Output:

- `Documents parsed successfully`

These APIs can be tested or used using Postman where we have to send the same request in the body and we would receive the response.

Going forward, we can implement caching technique to speed up the query response times.