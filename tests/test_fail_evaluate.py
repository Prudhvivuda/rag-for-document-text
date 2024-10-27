import pytest
from fastapi.testclient import TestClient
from api.main import app

# Initializing the TestClient for the app
client = TestClient(app)

# test function to check the evaluate API
def test_evaluate():
    
    # make a post request call 
    response = client.post( 
        "/evaluate", 
        json={
            "question": "what is renewable energy?",
            "generated_answer": ""
        }
    )
    
    # assert the response status code
    assert response.status_code == 200