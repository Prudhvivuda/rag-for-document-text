import os
import json
import glob
from zipfile import ZipFile
from api.logging_config import logger

def parse_documents():
    """
        It does two fuctions:
        1. Unzip and extract the files.
        2. To parse the documents and save the indexes in a file
    """
    # unzip and extract the files
    with ZipFile("db/renewable-energy.zip", 'r') as ref:
        logger.info("Extracting files in renewable-energy.zip")
        ref.extractall("db/renewable-energy")
        logger.info("Extraction done. Files extracted to db/renewable-energy")

    logger.info("Parsing the documents...")
    documents_folder = "db/renewable-energy/renewable-energy/"

    # try block for exception handling 
    try:
        document_texts = {}

        # match the files with extension.txt and iterate each of them
        for file_path in glob.glob(os.path.join(documents_folder, "*.txt")):

            # open the file
            with open(file_path, 'r') as file:
                # retreive the doument id
                document_id = os.path.basename(file_path).split('.')[0]
                # read the contents of the file
                document_texts[document_id] = file.read()

    except Exception as e:
        logger.error(f"Parsing failed. Encountered exception: {e}")

    logger.info("Document ids and content created")

    # save the document ids and its content in a json file
    with open("db/document_ids_and_content.json", "w") as f:
        json.dump(document_texts, f, indent=4)
        logger.info("Index file strored at db/document_ids_and_content.json")

    return "Documents parsed successfully"