import logging

# set the logging template
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
    handlers=[logging.StreamHandler()]
)

# get the logger object
logger = logging.getLogger("GenAI_BE_RAG_APP")