import pandas as pd
train = pd.read_csv('../data/raw/train.csv')
train.head()

# Here we are just ploting our data to see if every thing is ok


mix_columns = ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea',
               'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities',
               'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1',
               'Condition2', 'YearBuilt', 'YearRemodAdd', 'BldgType', 'HouseStyle',
               'Functional', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold',
               'SaleType', 'SaleCondition', 'SalePrice']



##The first column that we are going to clean is the 'Sale Condition'. In the analisys made by PYC the variable 'partial' should be
##maintained and the other variables joined



train['SaleCondition'].replace(['Abnorml', 'Normal', 'AdjLand', 'Alloca', 'Family'], 'Other')



##Now we changeed the variable that are not 'Partial' for 'Other'



## The 'MSZoning' column identifies the general zoning clssification of the sale - For this column we are joining the RH category with the RM one 



train['MSZoning'].replace(['RH'], 'RM')



#Column 'Street': Type of road acess to property - We have litlle data in this column so we are going to drop it
train.drop('Street', axis = 1)



#Column 'Alley': Type of aleey acess to property - We are joining the not 'NAN' variables in 'Other'
train['Alley'].replace(['Grvl Gravel', 'Pave paved'], 'Other')



#Column 'Neighborhood': Physical locations within Ames city limits - stand by



#Column 'LotShape': General shape of property - Joining the IR1, IR2 and IR3 in IR
train['LotShape'].replace(['IR1', 'IR2','IR3'], 'IR')



#Column 'Utilities': Type of utilities available - we are droping this column
train.drop('Utilities', axis = 1)



#Column 'MiscFeature':  Miscellaneous feature not covered in other categories - joining all the categories not nan for 'Other'
train['MiscFeature'].replace(['Elev', 'Gar2','Othr','Shed', 'TenC'], 'Other')


#Column 'MiscFeature': Value of miscellaneous feature - Droping column
train.drop('MiscFeature', axis = 1)