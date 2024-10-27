# Retrieval-Augmented Generation (RAG) system that automates the task of answering questions based on a collection of documents

## Introduction
We are building a RAG system to answer question based on a collection of documents. Exploring and implementing RAGs in ones workplace is very crucial as it helps in saving a lot of time and this is better to search or generate content based on some context. Building In-House-RAG systems is very helpful when the corporates don't want to expose their data to outside world but would still want to use LLM models for various tasks by providing some context to the models to improve the accuracy and to get the most relevant text.

## Instructions to run the code
This is developed in such a way that this can be run entirely in a notebook or as a separate application.
1. If this has to be run on jupyter notebook, then simply run all the cells in the notebook.
2. If this has to be run as an application or from CLI, the code for entire application is present in src folder.
    a. src/util contains the utility code like parsing, indexing and retrieving logic for modularity
    b. answer_question.py is the main file which inviokes the model to get the responses
    c. test_cases.py file contains 5 testcases with different queries. The queries can be found [here](../prompts)
   
### Installing requirements

- Use the below command to install all the requirements
    `pip install -r requirements.txt`

- If you are running this as an application, then please open a new terminal and run the bellow command
    `ollama pull mistral`

## Flow
Simplest way is to run the rag.ipynb notebook in sequential way.

Below are the steps that takes place in running our RAG system. 
1. Firstly, index is built by calling `build_index` with the documents folder as the parameter which is the renewable-energy text files folder.
2. Then call the function answerQuestion() with the question as the paramater which returns the response.
3. answerQuestion() internally calls retrieveDocuments() and then parses the documents returned by it and created a combined document with relevant information to sent to the model.
4. This combined document paired with the question is then passed on to the Mistral 7B model to get the response.

## Assumption or Decisions
- Mistral-7B is used here as it is better than llama-2-7B
- Ollama is downloaded using `pip install ollama` assuimg for a windows user. To install it on MacOs please follow the command `brew install ollama`.
- To install on other operating systems, please follow the Ollama Website.