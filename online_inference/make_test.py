import json
import pytest
from fastapi.testclient import TestClient
import os

from server import app, preload_model

client = TestClient(app)

@pytest.fixture(scope='session', autouse=True)
def initialize_model():
    os.environ["MODEL"] = "model_knn.pkl"
    os.environ["TRANSFORMER"] = "transformer_knn.pkl"
    preload_model()

def test_predict():
    request = {
        'age': 46,
        'sex': 0,
        'cp': 3,
        'trestbps': 150,
        'chol': 169,
        'fbs': 0,
        'restecg': 0,
        'thalach': 87,
        'exang': 0,
        'oldpeak': 1.2,
        'slope': 0,
        'ca': 0,
        'thal': 1
        }
    response = client.post('/predict',json.dumps(request))
    assert response.status_code == 200
    assert response.json() == {'target': '1'}
    print(111)
