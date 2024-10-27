import pytest
from fastapi.testclient import TestClient
from api.main import app

# Initializing the TestClient for the app
client = TestClient(app)

# test function to check the upload functionality
def test_upload_documents():

    # make a post request
    response = client.post("/upload")

    # assert the reponse status code
    assert response.status_code == 200