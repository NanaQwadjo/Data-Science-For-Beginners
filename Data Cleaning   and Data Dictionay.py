#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import pandas as pd
import numpy as np


# DATA DICTIONARY

# In[2]:


#Reading file from your computer 
data =pd.read_csv('Billionaires Statistics Dataset.csv')
data


# In[17]:


data.head()


# In[26]:


data.tail()


# In[15]:


#Check if there's any duplicate in the data
data.duplicated()


# In[12]:


#Drop all the duplicates
data.drop_duplicates()


# In[6]:


#Helps to know the data Type 0f the data 
data.info()


# In[7]:


#Helps to find the statistics of a data
data.describe()


# In[20]:


#Sun the number of Nan's in eeach of the variables if any
data.isna().sum()


# In[24]:


#checking the number of rows and columns 0f the dataset
data.shape


# In[25]:


# The columns of the data
data.columns


# #        DATA CLEANING 

# In[27]:


# find the median  of the age in the data
data['age'].median()


# In[28]:


# Count the occurance of each unquie age value 
data['age'].value_counts()


# In[32]:


#Displays the values of the 'category'
set(data ['gender'])


# In[34]:


#how to select one or more columns 
data[['gender','age']]


# In[36]:


#How to select just one column
data['country']


# In[38]:


#remove the rows from the 'data' Dataframe whwere either the 'tite ' or 'organization columns contains '
data.dropna(subset = ['title','organization'  ], inplace = True )


# # The iloc and the loc

# In[40]:


# To find the  data
data.iloc[1:4]


# In[46]:


# Use to find specific data
data.loc[1:3 , ['country','category' ,'city']]


# In[64]:


data.loc[(data.category=='Automotive') & (data.age >20 ) & (data.country=='United States')] # To fnd the value  who's category is 'Automative' and has the age 'greater than 20' and and stays in the country of 'united Sates '


# In[71]:


data.loc[ (data.total_tax_rate_country   > 50) & (data.population_country > 200)].describe() 


# In[75]:


data[['country','age']].groupby('country').mean()


# In[76]:


data[['category','age']].groupby('category').mean()


# In[ ]:




