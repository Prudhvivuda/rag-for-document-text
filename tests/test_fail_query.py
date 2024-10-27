import pytest
from fastapi.testclient import TestClient
from api.main import app

# Initializing the TestClient for the app
client = TestClient(app)

# test function to check the query API
def test_query():
    
    # make a post request
    response = client.post( "/query", json={"question": 143})
    
    # assert the response status code
    assert response.status_code == 200
    