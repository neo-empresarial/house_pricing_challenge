#!/usr/bin/env python
# coding: utf-8

# In[3]:

import pandas as pd
train = pd.read_csv('../data/raw/train.csv',sep=';', decimal = ',')
train.head()


# In[2]:


# Here we are just ploting our data to see if every thing is ok


# In[5]:


mix_columns = ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea',
               'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities',
               'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1',
               'Condition2', 'YearBuilt', 'YearRemodAdd', 'BldgType', 'HouseStyle',
               'Functional', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold',
               'SaleType', 'SaleCondition', 'SalePrice']
train[mix_columns].head()

#again, just checking the colums that we will clean


# In[ ]:


##The first column that we are going to clean is the 'Sale Condition'. In the analisys made by PYC the variable 'partial' should be
##maintained and the other variables joined


# In[16]:


train['SaleCondition'].replace(['Abnorml', 'Normal', 'AdjLand', 'Alloca', 'Family'], 'Other')


# In[19]:


##Now we changeed the variable that are not 'Partial' for 'Other'


# In[20]:


## The 'MSZoning' column identifies the general zoning clssification of the sale - For this column we are joining the RH category with the RM one 


# In[21]:


train['MSZoning'].replace(['RH'], 'RM')


# In[23]:


#Column 'Street': Type of road acess to property - We have litlle data in this column so we are going to drop it
train.drop('Street', axis = 1)


# In[24]:


#Column 'Alley': Type of aleey acess to property - We are joining the not 'NAN' variables in 'Other'
train['Alley'].replace(['Grvl Gravel', 'Pave paved'], 'Other')


# In[26]:


#Column 'Neighborhood': Physical locations within Ames city limits - stand by


# In[27]:


#Column 'LotShape': General shape of property - Joining the IR1, IR2 and IR3 in IR
train['LotShape'].replace(['IR1', 'IR2','IR3'], 'IR')


# In[28]:


#Column 'Utilities': Type of utilities available - we are droping this column
train.drop('Utilities', axis = 1)


# In[32]:


#Column 'MiscFeature':  Miscellaneous feature not covered in other categories - joining all the categories not nan for 'Other'
train['MiscFeature'].replace(['Elev', 'Gar2','Othr','Shed', 'TenC'], 'Other')


# In[33]:


#Column 'MiscFeature': Value of miscellaneous feature - Droping column
train.drop('MiscFeature', axis = 1)


# In[ ]:




