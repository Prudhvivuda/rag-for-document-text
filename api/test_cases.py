import requests

def test_upload():
    response = requests.post("http://0.0.0.0:5001/upload", json={"question": "What is renewable energy?"})
    assert response.status_code == 200

def test_evaluate():
    response = requests.post("http://0.0.0.0:5001/evaluate", json={
        "question": "Define renewable energy.",
        "reference_answer": "Renewable energy comes from natural sources...",
        "generated_answer": "Energy from natural resources..."
    })
    assert response.status_code == 200
    
test_upload()
test_evaluate()