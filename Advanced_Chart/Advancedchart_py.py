#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(connected=True)


# In[2]:


df = pd.read_csv("dataset/dataset_baru.csv",parse_dates=["order_date"])
df.head()


# In[3]:


data = go.Scatter(
    x=df.sales,
    y=df.profit,
    mode="markers",
   
)
fig = go.Figure(data=data)
iplot(fig)


# In[8]:


import numpy as np


# In[11]:


from scipy import stats


# In[12]:


slope, intercept, r_value, p_value, std_err = stats.linregress(x=df.sales, y=df.profit)
lines = slope * df.sales.values + intercept
lines


# In[14]:


dot = go.Scatter(
    x=df.sales,
    y=df.profit,
    mode="markers",  
)
line  = go.Scatter(
    x=df.sales,
    y=lines,
    name="Linear trend liner",  
)

data=[dot,line]
fig = go.Figure(data=data)
iplot(fig)


# In[15]:


dot = go.Scatter(
    x=df.sales,
    y=df.profit,
    mode="markers",  
)
line  = go.Scatter(
    x=df.sales,
    y=lines,
    name="Linear trend liner",  
)

data=[dot,line]

layout = {
    "title" : "sales vs profit",
}
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[20]:


dot = go.Scatter(
    x=df.sales,
    y=df.profit,
    mode="markers",  
)
line  = go.Scatter(
    x=df.sales,
    y=lines,
    name="Linear trend liner",  
)

data=[dot,line]

layout = {
    "title" : {
       "text" : "sales vs profit",
        "x" : 0.5,
    },
        "xaxis": {
            "title" : "sales",
            
        },
        "yaxis": {
            "title" : "profit",      
    }
}
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[22]:


dot = go.Scatter(
    x=df.sales,
    y=df.profit,
    mode="markers",  
)
line  = go.Scatter(
    x=df.sales,
    y=lines,
    name="Linear trend liner",  
)

data=[dot,line]

layout = {
    "title" : {
       "text" : "sales vs profit",
        "x" : 0.5,
    },
        "xaxis": {
            "title" : "sales",
            "range" :[0,7500],
            
        },
        "yaxis": {
            "title" : "profit",  
            "range":[-2500,2500],
    }
}
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[23]:


df.head()


# In[24]:


df.category.unique()


# In[26]:


dot1 = go.Scatter(
    x=df[df.category == "Furniture"].sales,
    y=df[df.category == "Furniture"].profit,
    mode="markers",  
    name="Furniture"
)

dot2 = go.Scatter(
    x=df[df.category == "Office Supplies"].sales,
    y=df[df.category == "Office Supplies"].profit,
    mode="markers",  
    name="Office Supplies"
)
dot3 = go.Scatter(
    x=df[df.category == "Technology"].sales,
    y=df[df.category == "Technology"].profit,
    mode="markers",  
    name="Technology"
)


data=[dot1,dot2,dot3,line]

layout = {
    "title" : {
       "text" : "sales vs profit",
        "x" : 0.5,
    },
        "xaxis": {
            "title" : "sales",
            "range" :[0,7500],
            
        },
        "yaxis": {
            "title" : "profit",  
            "range":[-2500,2500],
    }
}
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[28]:


dot1 = go.Scatter(
    x=df[df.category == "Furniture"].sales,
    y=df[df.category == "Furniture"].profit,
    mode="markers",  
    name="Furniture"
)

dot2 = go.Scatter(
    x=df[df.category == "Office Supplies"].sales,
    y=df[df.category == "Office Supplies"].profit,
    mode="markers",  
    name="Office Supplies"
)
dot3 = go.Scatter(
    x=df[df.category == "Technology"].sales,
    y=df[df.category == "Technology"].profit,
    mode="markers",  
    name="Technology"
)

line  = go.Scatter(
    x=df.sales,
    y=lines,
    line={
        "dash": "dash",
        "width": 5,
    },
    name="Linear trend liner",  
)

data=[dot1,dot2,dot3,line]

layout = {
    "title" : {
       "text" : "sales vs profit",
        "x" : 0.5,
    },
        "xaxis": {
            "title" : "sales",
            "range" :[0,7500],
            
        },
        "yaxis": {
            "title" : "profit",  
            "range":[-2500,2500],
    }
}
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[29]:


dot1 = go.Scatter(
    x=df[df.category == "Furniture"].sales,
    y=df[df.category == "Furniture"].profit,
    mode="markers", 
    marker={
        "size":10,
    },
    name="Furniture"
)

dot2 = go.Scatter(
    x=df[df.category == "Office Supplies"].sales,
    y=df[df.category == "Office Supplies"].profit,
    mode="markers",
     marker={
        "size":5,
    },
    name="Office Supplies"
)
dot3 = go.Scatter(
    x=df[df.category == "Technology"].sales,
    y=df[df.category == "Technology"].profit,
    mode="markers", 
     marker={
        "size":10,
    },
    name="Technology"
)

line  = go.Scatter(
    x=df.sales,
    y=lines,
    line={
        "dash": "dash",
        "width": 5,
    },
    name="Linear trend liner",  
)

data=[dot1,dot2,dot3,line]

layout = {
    "title" : {
       "text" : "sales vs profit",
        "x" : 0.5,
    },
        "xaxis": {
            "title" : "sales",
            "range" :[0,7500],
            
        },
        "yaxis": {
            "title" : "profit",  
            "range":[-2500,2500],
    }
}
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[35]:


dot1 = go.Scatter(
    x=df[df.category == "Furniture"].sales,
    y=df[df.category == "Furniture"].profit,
    mode="markers", 
    marker={
        "size":10,
    },
    name="Furniture"
)

dot2 = go.Scatter(
    x=df[df.category == "Office Supplies"].sales,
    y=df[df.category == "Office Supplies"].profit,
    mode="markers",
     marker={
        "size":5,
    },
    name="Office Supplies"
)
dot3 = go.Scatter(
    x=df[df.category == "Technology"].sales,
    y=df[df.category == "Technology"].profit,
    mode="markers", 
     marker={
        "size":10,
    },
    name="Technology"
)

line  = go.Scatter(
    x=df.sales,
    y=lines,
    line={
        "dash": "dash",
        "width": 5,
    },
    name="Linear trend liner",  
)

data=[dot1,dot2,dot3,line]

layout = {
    "title" : {
       "text" : "sales vs profit",
        "x" : 0.5,
    },
        "xaxis": {
            "title" : "sales",
            "range" :[0,7500],
            
        },
        "yaxis": {
            "title" : "profit",  
            "range":[-2500,2500],
    },
    "legend" : {
        "orientation":"h",
        "x":0.5,
        "y":1,
        "xanchor":"center",
    }
}
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[39]:


dot1 = go.Scatter(
    x=df[df.category == "Furniture"].sales,
    y=df[df.category == "Furniture"].profit,
    mode="markers", 
    marker={
        "size":10,
    },
    name="Furniture"
)

dot2 = go.Scatter(
    x=df[df.category == "Office Supplies"].sales,
    y=df[df.category == "Office Supplies"].profit,
    mode="markers",
     marker={
        "size":5,
    },
    name="Office Supplies"
)
dot3 = go.Scatter(
    x=df[df.category == "Technology"].sales,
    y=df[df.category == "Technology"].profit,
    mode="markers", 
     marker={
        "size":10,
    },
    name="Technology"
)

line  = go.Scatter(
    x=df.sales,
    y=lines,
    line={
        "dash": "dash",
        "width": 5,
    },
    name="Linear trend liner",  
)

data=[dot1,dot2,dot3,line]

layout = {
    "title" : {
       "text" : "sales vs profit",
        "x" : 0.5,
    },
        "xaxis": {
            "title" : "sales",
            "range" :[0,7500],
            
        },
        "yaxis": {
            "title" : "profit",  
            "range":[-2500,2500],
    },
  "showlegend" : False,
    
}
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[ ]:




