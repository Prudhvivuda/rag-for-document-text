import requests

# define the url
url = "http://0.0.0.0:5000"

# test function for upload functionality
def test_upload():
    response = requests.post(
        f"{url}/upload"
    )
    assert response.status_code == 200
    print("Response: ", response.json())
    
# test function for query fucntionality
def test_query():
    response = requests.post(
        f"{url}/query", 
        json={
            "question": "what is renewable energy?"
        }
    )
    assert response.status_code == 200
    print("Response: ", response.json())

# test function for evaluate functionality
def test_evaluate():
    response = requests.post(
        url=f"{url}/evaluate", 
        json={
            "question": "what is renewable energy?",
            "reference_answer": "",
            "generated_answer": ""
        }
    )
    assert response.status_code == 200
    print("Response: ", response.json())

# calling the test functions
test_evaluate()
test_query()