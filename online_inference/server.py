import os
import pickle
import uvicorn
import logging
from fastapi import FastAPI
from pydantic import BaseModel

import pandas as pd

from typing import Literal

import time
start_time = time.time()

app = FastAPI()
model = None
transformer = None

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)

class MedicalData(BaseModel):
    age: float
    sex: Literal[0, 1]
    cp: Literal[0, 1, 2, 3]
    trestbps: float
    chol: float
    fbs: Literal[0, 1]
    restecg: Literal[0, 1, 2]
    thalach: float
    exang: Literal[0, 1]
    oldpeak: float
    slope: Literal[0, 1, 2]
    ca: Literal[0, 1, 2, 3]
    thal: Literal[0, 1, 2]


@app.on_event("startup")
def preload_model():
    model_file = os.getenv("MODEL")
    transformer_file = os.getenv("TRANSFORMER")
    if model_file is None:
        error_message = "MODEL variable is None or smthg is wrong"
        raise FileNotFoundError(error_message)

    with open(model_file, 'rb') as f:
        global model
        model = pickle.load(f)

    with open(transformer_file, 'rb') as ff:
        global transformer
        transformer = pickle.load(ff)


@app.post("/predict")
def predict(request: MedicalData):
    df = pd.DataFrame([request.dict()])
    X = transformer.transform(df)
    y = model.predict(X)
    condition = 'healthy' if not y[0] else 'sick'
    return {'target': str(y[0])}
    #return {'condition': condition}

@app.get("/", status_code=200)
def root():
    return {"message": "service is up"}

@app.get("/ready", status_code=200)
def ready() -> bool:
    cur_time = time.time()
    if cur_time - start_time < 30.0:
        return false
    #return (model is not None) and (transformer is not None)
    return true

@app.get("/health", status_code=200)
def health() -> bool:
    cur_time = time.time()
    if cur_time - start_time < 35.0 or cur_time - start_time > 120.0:
        return false
    #return (model is not None) and (transformer is not None)
    return true

if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=os.getenv("PORT", 18000))
