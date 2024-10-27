import os
import glob

def parseDocuments(documents_folder):

    # create a dictionary with the file names as key and the content in the file as values
    document_texts = {}
    for file_path in glob.glob(os.path.join(documents_folder, "*.txt")):

        # open and read the file
        with open(file_path, 'r') as file:
            doc_id = os.path.basename(file_path).split('.')[0]

            # saving the file contents in dictionary with the key as document id
            document_texts[doc_id] = file.read()
            
    return document_texts