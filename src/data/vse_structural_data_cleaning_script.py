train['OverallQual'].replace([1, 2, 3, 4], '4-', inplace=True)

train['OverallCond'].replace([6, 7, 8], '6-8', inplace=True)

train['RoofStyle'].replace(['Flat', 'Gambrel', 'Hip', 'Mansard', 'Shed'], 'Other', inplace=True)

train['RoofMatl'].replace(['ClyTile', 'Membran', 'Metal', 'Roll', 'Tar&Grv', 'WdShake'], 'Other', inplace=True)

train['Exterior1st'].replace(['AsbShng', 'AsphShn', 'BrkComm', 'CBlock'], 'LowQualMat' ,inplace=True)
train['Exterior1st'].replace(['HdBoard', 'Stucco'], 'HDBoard/Stucco', inplace=True)
train['Exterior1st'].replace(['MetalSd', 'Wd Sdng', 'WdShing'], 'Metal/RegWood', inplace=True)
train['Exterior1st'].replace(['ImStucc', 'Stone', 'VinylSd', 'BrkFace'], 'HighQualMat', inplace=True)

train['Exterior2nd'].replace(['AsbShng', 'AsphShn', 'Brk Cmn', 'CBlock'], 'LowQualMat' ,inplace=True)
train['Exterior2nd'].replace(['HdBoard', 'Stucco', 'Plywood', 'Wd Shng'], 'HDBoard/Stucco/Wood', inplace=True)
train['Exterior2nd'].replace(['MetalSd', 'Wd Sdng'], 'Metal/Wood Siding', inplace=True)
train['Exterior2nd'].replace(['ImStucc', 'Stone', 'VinylSd', 'BrkFace'], 'HighQualMat', inplace=True)

train['ExterCond'].replace(['Po', 'Fa'], "Below Average", inplace=True)

train['Foundation'].replace(['Stone', 'Wood', 'CBlock'], "Cinder/Stone/Wood", inplace=True)

train['Heating'].replace(['GasA', 'GasW'], 'Gas', inplace=True)
train['Heating'].replace(['Floor', 'Grav', 'Wall', 'OthW'], 'Other', inplace=True)

train['HeatingQC'].replace(['Fa', 'Po'], 'Below Average', inplace=True)
train['HeatingQC'].replace(['Gd', 'TA'], 'Gd/TA', inplace=True)

train['Electrical'].replace(['FuseA', 'FuseF', 'FuseP', 'Mix'], 'Other', inplace=True)

train['Fireplaces'].replace([2, 3], '2+', inplace=True)

train['PavedDrive'].replace(['N', 'P'], 'No/Partial', inplace=True)
train['PavedDrive'].replace('Y', 'Yes', inplace=True)

train['Fence'].replace(['GdWo', 'MnWw'], 'Wood/Wire', inplace=True)
