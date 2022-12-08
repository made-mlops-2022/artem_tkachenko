import argparse
import base64
import datetime
import os
from io import BytesIO
import numpy as np
import pandas as pd

CATEGORICAL_FEATURES = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']

num_samples = 200

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, default="./data/raw/heart_cleveland_upload.csv")
    parser.add_argument("--no_probs", action="store_true")
    parser.add_argument("--output", type=str, default="./data/generated/generated.csv")
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    df = pd.read_csv(args.data)
    statistics = df.describe()
    cat_features_values = dict()
    cat_features_probs = dict()
    answer = dict()
    for c in CATEGORICAL_FEATURES:
        keys = list(df.value_counts(c).to_dict().keys())
        values = list(df.value_counts(c, normalize=True).to_dict().values())
        cat_features_values[c] = keys
        cat_features_probs[c] = values
    for col in statistics:
        if col not in CATEGORICAL_FEATURES:
            if not args.no_probs:
                mean = statistics[col].loc['mean']
                std = statistics[col].loc['std']
                answer[col] = np.random.normal(loc=mean, scale=std, size=num_samples)
            else:
                answer[col] = np.random.uniform(
                    low=statistics[col]['min'], high=statistics[col]['max'], size=num_samples
                )
        else:
            if not args.no_probs:
                answer[col] = np.random.choice(
                    cat_features_values[col], replace=True, p=cat_features_probs[col], size=num_samples
                )
            else:
                answer[col] = np.random.choice(
                    cat_features_values[col], replace=True, size=num_samples
                )

    filename = os.path.abspath(args.output)
    new_df = pd.DataFrame()
    for col in df.columns:
        new_df[col] = answer[col]
    new_df.to_csv(filename)


if __name__ == "__main__":
    main()
