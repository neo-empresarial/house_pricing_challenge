#!/usr/bin/env python
# coding: utf-8

# # EDA Rooms data

# To explore all the 81 collumns of this dataframe, the NEO team decided to split the EDA in 3 notebooks: 1- EDA of Structural Data 2- EDA of Rooms data 3- EDA of Mix Data (data that's not about Structural and Rooms data).

# The rooms data is composed of 24 categories, which are listed below:

rooms_columns = ['BedroomAbvGr', 'BsmtCond', 'BsmtExposure', 'BsmtFinSF1','BsmtFinSF2',
                'BsmtFinType1', 'BsmtFinType2', 'BsmtFullBath', 'BsmtHalfBath', 'BmstQual',
                'BsmtUnfSF', 'FullBath', 'GarageArea', 'GarageCars', 'GarageCond',
                'GarageFinish', 'GarageQual', 'GarageType', 'GarageYrBlt', 'HalfBath',
                 'KitchenAbvGr', 'KitchenQual', 'TotalBmstSF', 'TotRmsAbvGrd']


# ## Missing data

# The first code used to look for missing data had the objective of finding "NaN" values on the dataframe columns:

import pandas as pd

df = pd.read_csv('C:/Users/gilan/Desktop/Victor/NEO/N67/rooms.csv')

print(len(df) - df.count())


# Analysing the output above, it is possible to see missing data on basement and garage related categories. The reason for this is that some of the houses sold don't have basements or garage.

# # #Target and predictor variables relation

# After searching for missing data, the next step taken was to find a relation between the target variable (SalePrice) and the predictor variables.
# First of all, a correlation heatmap was plotted, using the following code:

import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/gilan/Desktop/Victor/NEO/N67/rooms.csv')
corrMatrix = df.corr()
sn.heatmap(corrMatrix, cmap='Greens')
plt.show()


# The algorithm only displayed the quantitative variables of the dataset, as it wasn't able to order the string categories in the qualitative categories. Because of that, this analysis couldn't give us any valuable information.

# Afterwards, the predictor variables were divided as continuous variables and discrete variables. By doing this, it became much easier to find a viable way to look at the data.
# The analysis done with the continuous variables was a scatter plot, with the x axis being the predictor variable and the y axis being the SalePrice. The following code was used for this plot, using as an example the "BsmtFinSF1" variable:

df = pd.read_csv('C:/Users/gilan/Desktop/Victor/NEO/N67/rooms.csv')
df.plot.scatter(x='BsmtFinSF1', y='SalePrice')
plt.show()


# In this example, we can see that the great majority of the ocurrences have similar values in the "BsmtFinSF1" category, with only very few outliers. At a first look, the variable doesn't seem to influence the target variable very much. One thing that can be done to possibilitate a better analysis of this variable is to exlude these outliers.

# The "GarageArea" is another example of a continuous variable analysed in the same way:

df = pd.read_csv('C:/Users/gilan/Desktop/Victor/NEO/N67/rooms.csv')
df.plot.scatter(x='GarageArea', y='SalePrice')
plt.show()


# As it can be seen, the "GarageArea" variable has less outliers than the "BsmtFinSF1" one, but it doesn't seem to affect the target variable considerably either.

# For the discrete variables, a bar plot was used to analyze their influence in the target variables. The x axis has the predictor variable categories and the y axis has the sale price average for each of these categories. The example below shows the code used for it with the "BsmtFullBath" variable on the y axis:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/gilan/Desktop/Victor/NEO/N67/rooms.csv')
avg = df.groupby('BsmtFullBath').mean()
avg.plot.bar(y='SalePrice')
plt.xlabel('BsmtFullBath')
plt.ylabel('Sale Price Average')
plt.show()


# As it can be seen, the price increases as the basement bathrooms also increase, except for the category of 3 bathrooms. We can use the method() function for a better understanding of this behavior:

print(df.groupby('BsmtFullBath')['SalePrice'].describe())


# As the describe() method showed us, the number of ocurrences of the categories "2" and especially "3" are very lower than the ocurrences of "0" and "1". Other fact that can be seen is that the average of the categories "1" and "2" are quite close, as their standard deviation also is. Because of that, we can try to replace the categories "1", "2" and "3" for "1+" and describe it again to see the result:

df['BsmtFullBath'].replace([1, 2, 3], '1+', inplace=True)
print(df.groupby('BsmtFullBath')['SalePrice'].describe())


# The describe() method shows that the average SalePrice and the standard deviation barely changed. The quartiles also remained very similar. Thus, we can conclude that if we keep this merging, the set will probably have a better performance when trained.

# Another example with the same analysis is the "BsmtFinType1" category. First of all, let's show a bar plot of it:

avg = df.groupby('BsmtFinType1').mean()
avg.plot.bar(y='SalePrice')
plt.xlabel('BsmtFinType1')
plt.ylabel('Sale Price Average')
plt.show()


# The "GLQ" (Good Living Quarters) category is clearly higher than the other ones, which have a similar average. Analysing the describe() method of the variable:

print(df.groupby('BsmtFinType1')['SalePrice'].describe())


# As we can see, the three categories with least ocurrences have similar averages and standard deviations. Using the replace method on "BsmtFinType1" for these categories and analysing the describe() output:

df['BsmtFinType1'].replace(['BLQ', 'LwQ', 'Rec'], 'Others', inplace=True)
print(df.groupby('BsmtFinType1')['SalePrice'].describe())


# After replacing the categories for "Others", it's possible to see that the average SalePrice, standard deviation and quartiles of the new category are very similar to those of the "BLQ" category, the category with most occurrences between those that were replaced. Therefore, we can keep this replacement to improve the performance of the future train model.

# Similar analysis were made with all 24 categories related to rooms. In order to keep this notebook objective, these are the main insights collected by them:

# - Rooms quality seem to be the categories that influence the target variable the most;
# - When the variable categories are qualitative grades (Ex, Gd, TA, Fa, Po), the TA (Typical/Average) category usually has the majority of the occurences;
# - Basement and garage areas don't seem to have a logical relation with the target variable;
# - BsmtQual, GarageFinish, GarageQual, KitchenQual, TotRmsAbvGrd, HalfBath and BedroomAbvGr are the predictor variables that seem to influence the target variable the most.

# Furthermore, these are the predictor variables that seemed to have categories that could be merged:

# - BsmtQual: "TA" and "Fa" were replaced by "TA/Fa";
# - BsmtCond: "Fa" and "Po" were replaced by "Below Average";
# - BsmtExposure: "Av and "Mn" were replaced by "Av/Mn";
# - BsmtFinType1: "BLQ", "LwQ" and "Rec" were replaced by "Others";
# - BsmtFinType2: "BLQ", "LwQ" and "Rec" were replaced by "Others";
# - BsmtFullBath: 1, 2 and 3 were replaced by 1+;
# - GarageQual: "Ex", "Gd" and "TA" were replaced by "Average/Above Average" and "Fa" and "Po" were replaced by "Below Average";
# - GarageType: "2Types", "Basment" and "CarPort" were replaced by "Others";
# - KitchenQual: "TA" and "Fa" were replaced by "TA/Fa";
# - BedroomAbvGr: 5, 6 and 8 were replaced by "5+";
# - TotRmsAbvGrd: 2, 3 and 4 were replaced by "4-" and 10, 11, 12 and 14 were replaced by "10+";
# - FullBath: 0 and 1 were replaced by "0/1".

print(df.groupby('FullBath')['SalePrice'].describe())


# The only predictor variable on which it was decided to use a different plot is "GarageYrBlt". For this variable, the analysis was made with the help of a line plot:

df = pd.read_csv('C:/Users/gilan/Desktop/Victor/NEO/N67/rooms.csv')
avg = df.groupby('GarageYrBlt').mean()
avg.plot.line(y='SalePrice')
plt.title('Sale Price Average')
plt.show()


# As it can be seen, the target variable averages oscilate very much. However, after 1940, a certain growth pattern in the target variable can be identified as the predictor variable increases, but it was not enough to reach a satisfying conclusion about its influence on it.

# !jupyter nbconvert --to script mycode.ipynb --TemplateExporter.exclude_input_prompt=True
