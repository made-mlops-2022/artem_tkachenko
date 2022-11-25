FROM python:3.9-slim-buster

COPY requirements.txt .

RUN apt-get update && apt-get install -y wget && apt-get clean \
    && pip install --no-cache-dir -r requirements.txt

COPY heart.csv make_test.py model_knn.pkl server.py start.sh transformer_knn.pkl ./

WORKDIR ./

ENV MODEL="model_knn.pkl"
ENV TRANSFORMER="transformer_knn.pkl"

CMD ["bash", "start.sh"]