from clean import clean
from feature_selection import feature_selection
import numpy as np
import pandas as pd
import joblib
import glob
import os
import sys


def predict_results(model, df, save_csv=True):
    predictions = model.predict(df)
    result = load_submission()
    result['SalePrice'] = predictions
    if save_csv:
        result.to_csv('../data/processed/test_results.csv', index=False)

    return result


def load_submission(path='../data/raw/sample_submission.csv'):
    return pd.read_csv(path)


def preprocessing(df):
    df = pd.get_dummies(df, drop_first=True)
    return df


def load_model(filename="../models/2-gradient-boosting.sav"):
    return joblib.load(filename)


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    model = load_model()
    test = pd.read_csv('../data/raw/test.csv', index_col=0)
    test = clean(test, to_test=True)
    test = feature_selection(test)
    test = preprocessing(test)
    print(predict_results(model, test))
