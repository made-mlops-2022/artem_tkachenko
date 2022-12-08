import os
import click
import pandas as pd
from sklearn.datasets import load_wine


@click.command('generate')
@click.option('--out-dir')
def generate_data(out_dir: str):
    os.makedirs(out_dir, exist_ok=True)

    X, y = load_wine(return_X_y=True, as_frame=True)
    X.to_csv(os.path.join(out_dir, "data.csv"))
    y.to_csv(os.path.join(out_dir, "target.csv"))

if __name__ == '__main__':
    generate_data()
