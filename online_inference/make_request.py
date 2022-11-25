import json
import requests
import logging
import pandas as pd

HOST = "localhost"
PORT = 18000
DATA_PATH = "heart.csv"
NUM_REQUESTS = 5

logger = logging.getLogger(__name__)
logging.basicConfig(
    format="%(asctime)s %(name)s %(levelname)s %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)


def main():
    host = HOST
    port = PORT
    data_path = DATA_PATH
    num_requests = NUM_REQUESTS

    data = pd.read_csv(data_path)
    data.drop("condition", inplace=True, axis=1)
    data_requests = data.to_dict(orient='records')

    for idx, req in enumerate(data_requests):
        logger.info(req)
        response = requests.post('http://localhost:18000/predict',
            json.dumps(req)
        )
        logger.info(f"{idx}: Response status code: {response.status_code}")
        logger.info(f"{idx}: Response: {response.json()}")


if __name__ == "__main__":
    main()