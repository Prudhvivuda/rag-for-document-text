# db/document_parser.py

import os
import json
from zipfile import ZipFile
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import glob

# def parse_documents(zip_path="db/renewable-energy.zip", output_path="db/document_index.json"):
#     index = {}
#     document_texts = []
#     document_ids = []
    
#     documents_folder = "db/energy_docs/renewable-energy"
    
#     with ZipFile(zip_path, 'r') as zip_ref:
#         zip_ref.extractall(documents_folder)
        
#     for file_path in glob.glob(os.path.join(documents_folder, "*.txt")):
#         print('helo')
#         print(file_path)
#         with open(file_path, 'r') as file:
#             document_id = os.path.basename(file_path).split('.')[0]
#             content = file.read()
#             index[document_id] = content
#             document_texts.append(content)
#             document_ids.append(document_id)
    

#     # Save index to JSON for easy loading during API requests
#     with open(output_path, 'w') as out_file:
#         json.dump({"index": index, "texts": document_texts, "ids": document_ids}, out_file)

# if __name__ == "__main__":
#     parse_documents()

def parse_documents(documents_folder):
    document_texts = {}
    for file_path in glob.glob(os.path.join(documents_folder, "*.txt")):
        with open(file_path, 'r') as file:
            doc_id = os.path.basename(file_path).split('.')[0]
            document_texts[doc_id] = file.read()
    return document_texts
