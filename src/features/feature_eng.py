import pandas as pd
import os, sys


def load_dataset(path='../../data/processed/train.csv'):
    return pd.read_csv(path)


def save_dataset(df, path='../../data/processed/df_after_feature_eng.csv'):
    return df.to_csv(path, index=False)


def feature_selection(df):

    # Change variables types
    df['ExterQual'].replace(['Fa/TA'], '0', inplace=True)
    df['ExterQual'].replace(['Gd'], '1', inplace=True)
    df['ExterQual'].replace(['Ex'], '2', inplace=True)
    df['ExterQual'] = df['ExterQual'].apply(int)
    df['BsmtQual'].replace(['Fa'], '0', inplace=True)
    df['BsmtQual'].replace(['TA'], '1', inplace=True)
    df['BsmtQual'].replace(['Gd'], '2', inplace=True)
    df['BsmtQual'].replace(['Ex'], '3', inplace=True)
    df['BsmtQual'].fillna('0', inplace=True)
    df['BsmtQual'] = df['BsmtQual'].apply(int)
    df['KitchenQual'].replace(['Fa'], '0', inplace=True)
    df['KitchenQual'].replace(['TA'], '1', inplace=True)
    df['KitchenQual'].replace(['Gd'], '2', inplace=True)
    df['KitchenQual'].replace(['Ex'], '3', inplace=True)
    df['KitchenQual'] = df['KitchenQual'].apply(int)
    df['MSSubClass'] = df['MSSubClass'].apply(str)

    # Create new features
    df['PorchArea'] = df[[
        'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
        'ScreenPorch'
    ]].sum(axis=1)
    df['HighQualMat1st'] = df['Exterior1st'].apply(
        lambda x: 1 if x in ['HighQualMat', 'CemntBd'] else 0)
    df['HighQualMat2nd'] = df['Exterior2nd'].apply(
        lambda x: 1 if x in ['HighQualMat', 'CemntBd'] else 0)
    df['MasVnrType'].replace(['BrkCmn', 'BrkFace'], 'Brick', inplace=True)
    df['1FamBldg'] = df['BldgType'].apply(lambda x: 1 if x == '1Fam' else 0)

    # Drop features
    df.drop(columns=[
        'Fence', 'Alley', 'Heating', 'Condition1', 'Condition2', 'Electrical',
        'Fireplaces', 'PoolArea', 'PavedDrive', 'GarageType', 'GarageQual',
        'GarageYrBlt', 'GarageFinish', 'GarageCond', 'GarageArea',
        'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch',
        'ScreenPorch', 'FireplaceQu', 'PoolQC', 'HeatingQC', 'ExterCond',
        'BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1',
        'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF',
        'Neighborhood', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd',
        'BldgType', 'Functional', 'MoSold', 'MiscVal', 'LowQualFinSF',
        'KitchenAbvGr'
    ],
            inplace=True)

    return df


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    df = load_dataset()
    df = feature_selection(df)
    save_dataset(df)