import pandas as pd
import os
import sys


def load_dataset(path='../data/raw/train.csv'):
    return pd.read_csv(path, index_col=0)


def save_dataset(df, path='../data/processed/train_clean.csv'):
    return df.to_csv(path, index=False)


def clean_rooms(df):
    '''
    This function get the dataset and clean all columns related with the rooms.
    To understand what the cleanning does, please read the notebook 2.1 and 1.1.
    '''

    df['BsmtCond'].replace(['Fa', 'Po'], 'Below avarage', inplace=True)
    df['GarageQual'].replace(['Ex', 'Gd', 'TA'],
                             "Average/Above Average",
                             inplace=True)
    df['GarageQual'].replace(['Fa', 'Po'], "Below Average", inplace=True)
    df['BsmtFinType1'].replace(['BLQ', 'LwQ', 'Rec'], 'Others', inplace=True)
    df['BsmtFinType2'].replace(['BLQ', 'LwQ', 'Rec'], 'Others', inplace=True)
    df['GarageCond'].replace(['TA', 'Gd', 'Ex'],
                             'Avarage/Above Avarage',
                             inplace=True)
    df['GarageCond'].replace(['Po', 'Fa'], 'Below Average', inplace=True)
    df['GarageType'].replace(['Detchd', 'CarPort', 'Basment', '2Types'],
                             "Other",
                             inplace=True)

    return df


def clean_mix(df, test=False):
    '''
    This function get the dataset and clean all columns related with the mix data.
    To understand what the cleanning does, please read the notebooks.
    '''

    df['MSSubClass'].replace([150], 20, inplace=True)
    df['LotConfig'].replace(['FR3', 'FR2'], 'FRX', inplace=True)
    df['HouseStyle'].replace(['1Story', '1.5Fin', '1.5Unf'],
                             '<=1.5Story',
                             inplace=True)
    df['HouseStyle'].replace(['2Story', '2.5Fin', '2.5Unf'],
                             '>1.5Story',
                             inplace=True)
    df['SaleType'].replace(
        ['WD', 'COD', 'ConLID', 'CWD', 'ConLw', 'Con', 'Oth'],
        'Other',
        inplace=True)
    df['SaleCondition'].replace(
        ['Abnorml', 'Normal', 'AdjLand', 'Alloca', 'Family'],
        'Other',
        inplace=True)
    df['MSZoning'].replace(['RH'], 'RM', inplace=True)
    df.drop('Street', axis=1, inplace=True)
    df['Alley'].replace(['Grvl Gravel', 'Pave paved'], 'Other', inplace=True)
    df['LotShape'].replace(['IR1', 'IR2', 'IR3'], 'IR', inplace=True)
    df.drop('Utilities', axis=1, inplace=True)
    df.drop('MiscFeature', axis=1, inplace=True)
    df['MasVnrArea'].fillna(0, inplace=True)

    return df


def clean_outliers(df):
    df = df[df['LotArea'] < 100000]
    df = df[df['LotFrontage'] < 200]

    return df


def fill_test(df):
    str_cols = df.columns[df.dtypes == object]
    df[str_cols] = df[str_cols].fillna(df[str_cols].mode().iloc[0])
    df.fillna(0, inplace=True)
    return df


def clean_strucute(df):
    '''
    This function get the dataset and clean all columns related with the structure data.
    To understand what the cleanning does, please read the notebooks.
    '''

    df['RoofStyle'].replace(['Flat', 'Gambrel', 'Hip', 'Mansard', 'Shed'],
                            'Other',
                            inplace=True)
    df['RoofMatl'].replace(
        ['ClyTile', 'Membran', 'Metal', 'Roll', 'Tar&Grv', 'WdShake'],
        'Other',
        inplace=True)
    df['Exterior1st'].replace(['AsbShng', 'AsphShn', 'BrkComm', 'CBlock'],
                              'LowQualMat',
                              inplace=True)
    df['Exterior1st'].replace(['HdBoard', 'Stucco'],
                              'HDBoard/Stucco',
                              inplace=True)
    df['Exterior1st'].replace(['MetalSd', 'Wd Sdng', 'WdShing'],
                              'Metal/RegWood',
                              inplace=True)
    df['Exterior1st'].replace(['ImStucc', 'Stone', 'VinylSd', 'BrkFace'],
                              'HighQualMat',
                              inplace=True)
    df['Exterior2nd'].replace(['AsbShng', 'AsphShn', 'Brk Cmn', 'CBlock'],
                              'LowQualMat',
                              inplace=True)
    df['Exterior2nd'].replace(['HdBoard', 'Stucco', 'Plywood', 'Wd Shng'],
                              'HDBoard/Stucco/Wood',
                              inplace=True)
    df['Exterior2nd'].replace(['MetalSd', 'Wd Sdng'],
                              'Metal/Wood Siding',
                              inplace=True)
    df['Exterior2nd'].replace(['ImStucc', 'Stone', 'VinylSd', 'BrkFace'],
                              'HighQualMat',
                              inplace=True)
    df['ExterCond'].replace(['Po', 'Fa'], "Below Average", inplace=True)
    df['Foundation'].replace(['Stone', 'Wood', 'CBlock'],
                             "Cinder/Stone/Wood",
                             inplace=True)
    df['Heating'].replace(['GasA', 'GasW'], 'Gas', inplace=True)
    df['Heating'].replace(['Floor', 'Grav', 'Wall', 'OthW'],
                          'Other',
                          inplace=True)
    df['HeatingQC'].replace(['Gd', 'TA', 'Fa', 'Po'], 'Below Ex', inplace=True)
    df['Electrical'].replace(['FuseA', 'FuseF', 'FuseP', 'Mix'],
                             'Other',
                             inplace=True)
    df['Fireplaces'].replace([2, 3], '2+', inplace=True)
    df['PavedDrive'].replace(['N', 'P'], 'No/Partial', inplace=True)
    df['PavedDrive'].replace('Y', 'Yes', inplace=True)
    df['Fence'].replace(['GdWo', 'MnWw'], 'Wood/Wire', inplace=True)
    df['Foundation'].replace(['CBlock', 'BrkTil', 'Wood', 'Slab', 'Stone'],
                             'Other',
                             inplace=True)
    df['ExterQual'].replace(['Fa', 'TA'], 'Fa/TA', inplace=True)

    return df


def clean(df, to_test=False):
    '''
    Script to clean a entiry dataset.
    '''

    df = clean_mix(df)
    df = clean_rooms(df)
    df = clean_strucute(df)
    if not to_test:
        df = clean_outliers(df)
    else:
        df = fill_test(df)
    return df


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    train = load_dataset()
    train = clean(train)
    save_dataset(train)
