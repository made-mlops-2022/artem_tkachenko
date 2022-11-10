import logging
from dataclasses import dataclass
from hydra.utils import to_absolute_path
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

logger = logging.getLogger("main")

@dataclass
class DataLoader:
    categorical_features: list
    target: str

    def read_data(self, path: str) -> (pd.DataFrame, pd.Series):
        df = pd.read_csv(to_absolute_path(path))
        names2drop = []
        new_dfs = []
        for catdata in self.categorical_features:
            name = catdata['name']
            names2drop.append(name)
            data = df[name].values.reshape(-1, 1)
            ohe = OneHotEncoder(categories=[catdata['values']], sparse=False).fit_transform(data)
            transformed = pd.DataFrame(ohe)
            transformed.columns = [f"{name}_{value}" for value in catdata['values']]
            new_dfs.append(transformed)
        df = df.drop(names2drop, axis=1, errors='ignore')
        df = pd.concat((df, *new_dfs), axis=1)
        if self.target in df.columns:
            target = df[self.target]  
        else: 
            target = None
        df.drop(self.target, axis=1, inplace=True, errors='ignore')
        return df, target
