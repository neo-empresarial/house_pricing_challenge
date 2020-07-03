from clean import clean
from feature_selection import feature_selection
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.impute import SimpleImputer
import joblib
import numpy as np
import pandas as pd
import sys
import os


def preprocessing_train(df):
    df = pd.get_dummies(df, drop_first=True)
    return df


def train_model(df):
    X_train, y_train = df.drop(columns=['SalePrice']), df[['SalePrice']]
    X_train = preprocessing_train(X_train)
    model = GradientBoostingRegressor(n_estimators=3500,
                                      learning_rate=0.01,
                                      max_depth=4,
                                      max_features='sqrt',
                                      min_samples_leaf=15,
                                      min_samples_split=10,
                                      loss='huber',
                                      random_state=42)
    model.fit(X_train, y_train)
    return model


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    df = pd.read_csv('../data/raw/train.csv', index_col=0)
    df = clean(df)
    df = feature_selection(df)
    model = train_model(df)
    joblib.dump(model, '../models/1-regression-tree.sav')
