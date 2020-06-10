import pandas as pd
import os, sys


def load_dataset(path='../../data/raw/train.csv'):
    return pd.read_csv(path)


def save_dataset(df, path='../../data/processed/train.csv'):
    return df.to_csv(path)


def clean_rooms(df):
    '''
    This function get the dataset and clean all columns related with the rooms.
    To understand what the cleanning does, please read the notebook 2.1 and 1.1.
    '''

    df['BsmtFullBath'].replace([1, 2, 3], 1, inplace=True)
    df.rename(columns={'BsmtFullBath': '1 or higher'}, inplace=True)
    df['BsmtCond'].replace(['Fa', 'Po'], 'Below avarage', inplace=True)
    df['GarageQual'].replace(['Ex', 'Gd', 'TA'],
                             "Average/Above Average",
                             inplace=True)
    df['GarageQual'].replace(['Fa', 'Po'], "Below Average", inplace=True)
    df['BedroomAbvGr'].replace([0, 1, 2], '2 or less', inplace=True)
    df['BedroomAbvGr'].replace([5, 6, 8], '5 or higher', inplace=True)
    df['FullBath'].replace([0, 1], '1 or less', inplace=True)
    df['BsmtFinType1'].replace(['BLQ', 'LwQ', 'Rec'], 'Others', inplace=True)
    df['BsmtFinType2'].replace(['BLQ', 'LwQ', 'Rec'], 'Others', inplace=True)
    df['GarageCond'].replace(['TA', 'Gd', 'Ex'],
                             'Avarage/Above Avarage',
                             inplace=True)
    df['GarageCond'].replace(['Po', 'Fa'], 'Below Average', inplace=True)
    df['HalfBath'].replace([1, 2], '1 or higher', inplace=True)
    df['GarageType'].replace(['Detchd', 'CarPort', 'Basment', '2Types'],
                             "Other",
                             inplace=True)

    return df


def clean_mix(df):
    '''
    This function get the dataset and clean all columns related with the mix data.
    To understand what the cleanning does, please read the notebooks.
    '''

    df['SaleCondition'].replace(
        ['Abnorml', 'Normal', 'AdjLand', 'Alloca', 'Family'], 'Other')
    df['MSZoning'].replace(['RH'], 'RM')
    df.drop('Street', axis=1)
    df['Alley'].replace(['Grvl Gravel', 'Pave paved'], 'Other')
    df['LotShape'].replace(['IR1', 'IR2', 'IR3'], 'IR')
    df.drop('Utilities', axis=1)
    df['MiscFeature'].replace(['Elev', 'Gar2', 'Othr', 'Shed', 'TenC'],
                              'Other')
    df.drop('MiscFeature', axis=1)

    return df


def clean_strucute(df):
    '''
    This function get the dataset and clean all columns related with the structure data.
    To understand what the cleanning does, please read the notebooks.
    '''

    df['OverallQual'].replace([1, 2, 3, 4], '4-', inplace=True)
    df['OverallCond'].replace([6, 7, 8], '6-8', inplace=True)
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
    df['HeatingQC'].replace(['Fa', 'Po'], 'Below Average', inplace=True)
    df['HeatingQC'].replace(['Gd', 'TA'], 'Gd/TA', inplace=True)
    df['Electrical'].replace(['FuseA', 'FuseF', 'FuseP', 'Mix'],
                             'Other',
                             inplace=True)
    df['Fireplaces'].replace([2, 3], '2+', inplace=True)
    df['PavedDrive'].replace(['N', 'P'], 'No/Partial', inplace=True)
    df['PavedDrive'].replace('Y', 'Yes', inplace=True)
    df['Fence'].replace(['GdWo', 'MnWw'], 'Wood/Wire', inplace=True)

    return df


def clean(df):
    '''
    Script to clean a entiry dataset.
    '''

    df = clean_mix(df)
    df = clean_rooms(df)
    df = clean_strucute(df)
    return df


if __name__ == "__main__":
    os.chdir(os.path.dirname(sys.argv[0]))
    train = load_dataset()
    train = clean(train)
    save_dataset(train)