#!/usr/bin/env python
# coding: utf-8

# In[88]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
test = pd.read_csv('../data/raw/test.csv',sep=';', decimal = ',')
test.head()


# In[89]:


mix_columns = ['OverallQual', 'OverallCond', 'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea', 'ExterQual', 'ExterCond', 'Foundation', 'Heating', 'HeatingQC', 'CentralAir', 'Electrical', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF', 'GrLivArea', 'Fireplaces', 'FireplaceQu', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'PoolQC', 'Fence', 'SalePrice']

test[mix_columns].head()


# In[90]:


test[mix_columns].describe()


# In[97]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['OverallQual']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('OverallQual')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='OverallQual', y='SalePrice')


plt.show()


# In[98]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['OverallCond']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('OverallCond')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='OverallCond', y='SalePrice')


plt.show()


# In[99]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['RoofStyle']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('RoofStyle')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='RoofStyle', y='SalePrice')


plt.show()


# In[100]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['RoofMatl']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('RoofMatl')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='RoofMatl', y='SalePrice')


plt.show()


# In[103]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['Exterior1st']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('Exterior1st')
plt.ylabel('Sale Price Average')


plt.show()


# In[104]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['Exterior2nd']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('Exterior2nd')
plt.ylabel('Sale Price Average')



plt.show()


# In[106]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['MasVnrType']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('MasVnrType')
plt.ylabel('Sale Price Average')



plt.show()


# In[107]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['MasVnrArea']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('MasVnrArea')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='MasVnrArea', y='SalePrice')


plt.show()


# In[108]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['ExterQual']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('ExterQual')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='ExterQual', y='SalePrice')


plt.show()


# In[109]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['ExterCond']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('ExterCond')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='ExterCond', y='SalePrice')


plt.show()


# In[110]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['Foundation']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('Foundation')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='Foundation', y='SalePrice')


plt.show()


# In[111]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['Heating']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('Heating')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='Heating', y='SalePrice')


plt.show()


# In[112]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['HeatingQC']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('HeatingQC')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='HeatingQC', y='SalePrice')


plt.show()


# In[113]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['CentralAir']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('CentralAir')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='CentralAir', y='SalePrice')


plt.show()


# In[114]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['Electrical']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('Electrical')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='Electrical', y='SalePrice')


plt.show()


# In[115]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['1stFlrSF']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('1stFlrSF')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='1stFlrSF', y='SalePrice')


plt.show()


# In[116]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['2ndFlrSF']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('2ndFlrSF')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='2ndFlrSF', y='SalePrice')


plt.show()


# In[117]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['LowQualFinSF']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('LowQualFinSF')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='LowQualFinSF', y='SalePrice')


plt.show()


# In[118]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['GrLivArea']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('GrLivArea')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='GrLivArea', y='SalePrice')


plt.show()


# In[119]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['Fireplaces']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('Fireplaces')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='Fireplaces', y='SalePrice')


plt.show()


# In[121]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['FireplaceQu']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('FireplaceQu')
plt.ylabel('Sale Price Average')



plt.show()


# In[122]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['PavedDrive']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('PavedDrive')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='PavedDrive', y='SalePrice')


plt.show()


# In[123]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['WoodDeckSF']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('WoodDeckSF')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='WoodDeckSF', y='SalePrice')


plt.show()


# In[124]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['OpenPorchSF']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('OpenPorchSF')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='OpenPorchSF', y='SalePrice')


plt.show()


# In[125]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['EnclosedPorch']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('EnclosedPorch')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='EnclosedPorch', y='SalePrice')


plt.show()


# In[126]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['3SsnPorch']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('3SsnPorch')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='3SsnPorch', y='SalePrice')


plt.show()


# In[127]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['ScreenPorch']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('ScreenPorch')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='ScreenPorch', y='SalePrice')


plt.show()


# In[128]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['PoolArea']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('PoolArea')
plt.ylabel('Sale Price Average')

test.plot.scatter(x='PoolArea', y='SalePrice')


plt.show()


# In[130]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['PoolQC']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('PoolQC')
plt.ylabel('Sale Price Average')



plt.show()


# In[132]:


pd.to_numeric(test['SalePrice'])
test['SalePrice'] = test['SalePrice']
avg = test.groupby(test['Fence']).mean()
avg.plot.bar(y ='SalePrice')
plt.xlabel('Fence')
plt.ylabel('Sale Price Average')



plt.show()


# In[ ]:




