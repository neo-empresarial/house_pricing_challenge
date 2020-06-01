import pandas as pd
import os, sys

def clean_rooms(df):
    '''
    This function get the dataset and clean all columns related with the rooms.
    To understand what the cleanning does, please read the notebook 2.1 and 1.1.
    '''
    
    df.drop(columns=['BsmtFinType1','BsmtFinType2'], inplace=True)
    df['BsmtFullBath'].replace([1, 2, 3], 1, inplace=True)
    df.rename(columns={'BsmtFullBath':'1 or higher'}, inplace=True)
    df['BsmtCond'].replace(['Fa', 'Po'], 'Below avarage', inplace=True)
    df['GarageQual'].replace(['Ex', 'Gd', 'TA'], "Average/Above Average", inplace=True)
    df['GarageQual'].replace(['Fa', 'Po'], "Below Average", inplace=True)
    df['BedroomAbvGr'].replace([0,1,2], '2 or less', inplace=True)
    df['BedroomAbvGr'].replace([5,6,8], '5 or higher', inplace=True)
    df['FullBath'].replace([0,1], '1 or less', inplace=True)
    df['BsmtFinType1'].replace(['BLQ', 'LwQ', 'Rec'], 'Others', inplace=True)
    df['BsmtFinType2'].replace(['BLQ', 'LwQ', 'Rec'], 'Others', inplace=True)
    df['GarageCond'].replace(['TA', 'Gd' 'Ex'], 'Avarage/Above Avarage', inplace=True)
    df['GarageCond'].replace(['Po', 'Fa', 'Below Average'], inplace=True)
    df['HalfBath'].replace([0,1], '1 or higher', inplace=True)
    df['GarageType'].replace(['Detchd', 'CarPort', 'Basment', '2Types'], "Other", inplace=True)

    return df
