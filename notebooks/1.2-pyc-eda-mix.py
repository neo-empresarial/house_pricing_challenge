#!/usr/bin/env python
# coding: utf-8

# # EDA MIX data
# 
# To explore all the 81 columns of this data frame the NEO team decide to split the EDA into 3 notebooks where:
# 1- EDA of Structural Data
# 2- EDA of Rooms data
# 3- EDA of Mix Data (data that's not about Structural and Rooms data)
# 
# This notebook had the role to analyze the MIX data, **focus on the distribution of the variable, and try to get some useful insights**.

from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import pandas as pd
import numpy as np

#Cdf function
def ecdf(x):
    x = np.sort(x)
    def result(v):
        return np.searchsorted(x, v, side='right') / x.size
    return result

def multiple_ecdf(column, target='SalePrice'):
    fig = go.Figure()
    keys = train[column].unique()
    for key in keys:
        bool_series = train[column]==key
        fig.add_trace(
            go.Scattergl(
                x=np.unique(train[bool_series][target]), 
                y=ecdf(train[bool_series][target])(np.unique(train[bool_series][target])), 
                line_shape='hv',
                name=str(key) + ', total: ' + str(bool_series.sum()))
        )
    return fig.show()

train = pd.read_csv('../data/raw/train.csv')


# ## Mix Columns overview
# 
# The columns of the training dataset that represents what we're calling mix data are represented in the strings in the variable **mix_columns**

mix_columns = ['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea',
               'Street', 'Alley', 'LotShape', 'LandContour', 'Utilities',
               'LotConfig', 'LandSlope', 'Neighborhood', 'Condition1',
               'Condition2', 'YearBuilt', 'YearRemodAdd', 'BldgType', 'HouseStyle',
               'Functional', 'MiscFeature', 'MiscVal', 'MoSold', 'YrSold',
               'SaleType', 'SaleCondition', 'SalePrice']

train[mix_columns].head()


train[mix_columns].isna().mean()


train[mix_columns].describe()


# # Sales variables
# 
# - MoSold
# - YrSold
# - SaleType
# - SaleCondition

# ## Sale Condition
# 
# 
# Condition of sale
# 
#        Normal	Normal Sale
#        Abnorml	Abnormal Sale -  trade, foreclosure, short sale
#        AdjLand	Adjoining Land Purchase
#        Alloca	Allocation - two linked properties with separate deeds, typically condo with a garage unit	
#        Family	Sale between family members
#        Partial	Home was not completed when last assessed (associated with New Homes)
# 

multiple_ecdf('SaleCondition')


# **Insights**
# 
# - The partial category in this column appears to increase significantly the sale Price
# - Maybe the other categories can be joined

# ## SaleType
# 
# 
# SaleType: Type of sale
# 		
#        WD 	Warranty Deed - Conventional
#        CWD	Warranty Deed - Cash
#        VWD	Warranty Deed - VA Loan
#        New	Home just constructed and sold
#        COD	Court Officer Deed/Estate
#        Con	Contract 15% Down payment regular terms
#        ConLw	Contract Low Down payment and low interest
#        ConLI	Contract Low Interest
#        ConLD	Contract Low Down
#        Oth	Other

multiple_ecdf('SaleType')


# **Insights**
# 
# - have a lot of categories, but appears that just the category New increase in the sale
# - Maybe we should try an unsupervised model to join these categories

# ## Sale date
# 
# Month and Year of the sale

sns.pairplot(train[['SalePrice','MoSold','YrSold']])


train[train['YrSold']==2010]['MoSold'].value_counts()


fig = make_subplots(rows=1, cols=2,
                   subplot_titles=("Mean", "Std"))

fig.add_trace(go.Scatter(x=np.sort(train['YrSold'].unique()), 
                         y=train.groupby(['YrSold'])['SalePrice'].mean()),
            row=1,col=1)

fig.add_trace(go.Scatter(x=np.sort(train['YrSold'].unique()), 
                         y=train.groupby(['YrSold'])['SalePrice'].std()),
            row=1,col=2)

fig.update_layout(showlegend=False, title_text="Mean and Std of Sales Price per Year")
fig.show()


train['day'] = 1
train['dateSold'] = pd.to_datetime(train.rename(columns={"YrSold": "year",
                                                         "MoSold": "month"})[['year','month','day']],
                                   unit='D')
train.drop(columns=['day'], inplace=True)
fig = px.line(train.groupby(['dateSold'])[['SalePrice', 'dateSold']].mean(), 
              x=train.groupby(['dateSold'])[['SalePrice', 'dateSold']].mean().index,
              y='SalePrice')
fig.show()


# **Insights**
# - The last month we have just 6 data, so, probably, we don't have data of the full month
# - Maybe it's better to join the 2 columns to understand the timeline
# - The timeline appears to make more sense that the Month or Year column alone

# ## Neighborhood Variables
# 
# - MSZoning
# - Street
# - Alley
# - Neighborhood
# - Condition 1
# - Condition 2

# ## MSZoning
# 
# Identifies the general zoning classification of the sale.
# 		
#        A	Agriculture
#        C	Commercial
#        FV	Floating Village Residential
#        I	Industrial
#        RH	Residential High Density
#        RL	Residential Low Density
#        RP	Residential Low Density Park 
#        RM	Residential Medium Density

multiple_ecdf('MSZoning')


# **Insights**
# 
# - The RH category can be joined with the RM one
# - C category have few data, but this graphic doesn't give us an option to join with another column

# ## Street
# 
# 
# Type of road access to property
# 
#        Grvl	Gravel	
#        Pave	Paved

train['Street'].value_counts()


# **Insights**
# 
# - Few values aren't equal to Pave, so maybe we should just drop this column

# ## Alley
# 
# Type of alley access to property
# 
#        Grvl	Gravel
#        Pave	Paved
#        NA 	No alley access

train['Alley'].value_counts()


multiple_ecdf('Alley')


# **Insights**
# 
# - Almost all values are Nan
# - The not nan variables appears to be very important
# - I think that we should just fill the nan values in this column

# ## Neighborhood
# 
# Physical locations within Ames city limits
# 
#        Blmngtn	Bloomington Heights
#        Blueste	Bluestem
#        BrDale	Briardale
#        BrkSide	Brookside
#        ClearCr	Clear Creek
#        CollgCr	College Creek
#        Crawfor	Crawford
#        Edwards	Edwards
#        Gilbert	Gilbert
#        IDOTRR	Iowa DOT and Rail Road
#        MeadowV	Meadow Village
#        Mitchel	Mitchell
#        Names	North Ames
#        NoRidge	Northridge
#        NPkVill	Northpark Villa
#        NridgHt	Northridge Heights
#        NWAmes	Northwest Ames
#        OldTown	Old Town
#        SWISU	South & West of Iowa State University
#        Sawyer	Sawyer
#        SawyerW	Sawyer West
#        Somerst	Somerset
#        StoneBr	Stone Brook
#        Timber	Timberland
#        Veenker	Veenker
# 			

multiple_ecdf('Neighborhood')


# **Insights**
# 
# - A LOT of categories
# - It's hard to group the categories, so we can use an unsupervised method to group then

# ## Condition 1 and 2
# 
# Proximity to various conditions
# 	
#        Artery	Adjacent to arterial street
#        Feedr	Adjacent to feeder street	
#        Norm	Normal	
#        RRNn	Within 200' of North-South Railroad
#        RRAn	Adjacent to North-South Railroad
#        PosN	Near positive off-site feature--park, greenbelt, etc.
#        PosA	Adjacent to postive off-site feature
#        RRNe	Within 200' of East-West Railroad
#        RRAe	Adjacent to East-West Railroad
# 	

multiple_ecdf('Condition1')


multiple_ecdf('Condition2')


# **Insights**
# 
# - almost all are 'Norm"
# - We can take just the more often categories, like "Feeddr" and "Artery" and make bool columns with these ones

# # Lot or Propriety Variables
# 
# - LotFrontage
# - LotArea
# - LotShape
# - LandContour
# - Utilities
# - LotConfig
# - LandSlope
# - MiscFeature
# - MiscVal

# ## Lot Frontage 
# 
# Linear feet of street connected to property
# 

fig = go.Figure()

fig.add_trace(
    go.Histogram(
        x=train['LotFrontage']
    )
)

fig.update_layout(title='Lot Frontage Distribution'
)

fig.show()


fig = px.scatter(train[train['LotFrontage'].notnull()], x="LotFrontage", y="SalePrice", trendline="ols")
fig.show()


# **Insights**
# 
# - The data remember a normal distribution with some outliers
# - Doesn't has a strong correlation with the sale price

# ## Lot Area
# 
# Lot size in square feet

fig = go.Figure()

fig.add_trace(
    go.Histogram(
        x=train['LotArea']
    )
)

fig.update_layout(title='Lot Frontage Distribution'
)

fig.show()


fig = px.scatter(train[train['LotArea'].notnull()], x="LotArea", y="SalePrice", trendline="ols")
fig.show()


# **Insights**
# 
# - The data remember a normal distribution with some outliers
# - Doesn't has a strong correlation with the sale price

# ## Lot Shape
# 
# General shape of property
# 
#        Reg	Regular	
#        IR1	Slightly irregular
#        IR2	Moderately Irregular
#        IR3	Irregular

multiple_ecdf('LotShape')


# **Insights**
# 
# - The IR1, IR2, and IR3 appears that can be joined in one category

# ## LandContour
# 
# Flatness of the property
# 
#        Lvl	Near Flat/Level	
#        Bnk	Banked - Quick and significant rise from street grade to building
#        HLS	Hillside - Significant slope from side to side
#        Low	Depression

multiple_ecdf('LandContour')


# **Insights**
# 
# - The Low and HLS appears that can be joined in one category, but I don't know if it really needs.

# ## Utilities
# 
# Type of utilities available
# 		
#        AllPub	All public Utilities (E,G,W,& S)	
#        NoSewr	Electricity, Gas, and Water (Septic Tank)
#        NoSeWa	Electricity and Gas Only
#        ELO	Electricity only

multiple_ecdf('Utilities')


# **Insights**
# 
# 
# - The values are almost all the same, this column should be dropped

# ## Lot Config
# 
# Lot configuration
# 
#        Inside	Inside lot
#        Corner	Corner lot
#        CulDSac	Cul-de-sac
#        FR2	Frontage on 2 sides of property
#        FR3	Frontage on 3 sides of property

multiple_ecdf('LotConfig')


# **Insights**
# 
# - The FR3 column have little values so have to be joined if another one, but the graphic don't point to any other category

# ## LandSlope
# 
# Slope of property
# 		
#        Gtl	Gentle slope
#        Mod	Moderate Slope	
#        Sev	Severe Slope

multiple_ecdf('LandSlope')


# **Insights**
# 
# - The lines are almost all the same in this analyze
# - Sev category has few data but this graphic doesn't show another category to join

# ## MiscFeature
# 
# Miscellaneous feature not covered in other categories
# 		
#        Elev	Elevator
#        Gar2	2nd Garage (if not described in garage section)
#        Othr	Other
#        Shed	Shed (over 100 SF)
#        TenC	Tennis Court
#        NA	None

train['MiscFeature'].value_counts()


train[train['MiscFeature'].isna()]['SalePrice'].describe()


train[~train['MiscFeature'].isna()]['SalePrice'].describe()


# **Insights**
# 
# - The rows are almost all filled with nan values
# - I suggest joining all the categories not nan

# ## MiscVal
# 
# $Value of miscellaneous feature

train[train['MiscFeature'].isna()]['MiscVal'].sum()


# **Insights**
# 
# - All the rows with nan values in Misc Feature are 0 in these columns
# - I suggest joining drop the column Misc Feature and use just MiscVal

# # Another Insights and Graphics

# ## Sale date with Condition and Type
# 
# We're going to analyze the sale price in time, grouping by the condition and type.

fig = px.line(train.groupby(['dateSold'])[['SalePrice', 'dateSold']].std(), 
              x=train.groupby(['dateSold'])[['SalePrice', 'dateSold']].std().index,
              y='SalePrice')
fig.show()


fig = px.scatter(train, x='dateSold', y='SalePrice',
                 trendline="lowess", color='SaleType', opacity=0.2)
fig.show()


fig = px.scatter(train, x='dateSold', y='SalePrice',
                 trendline="lowess", color='SaleCondition', opacity=0.2)
fig.show()


# # Notebook to python script
# 
# To improve our code review we are going to use the command below to convert this notebook in a .py file

get_ipython().system('jupyter nbconvert --to script mycode.ipynb --TemplateExporter.exclude_input_prompt=True')

