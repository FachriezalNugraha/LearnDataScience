#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly


# In[2]:


import pandas as pd
import plotly.graph_objs.as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(connection=True)


# In[3]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(connection=True)


# In[4]:


import pandas as pd
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot

init_notebook_mode(connected=True)


# In[7]:


df = pd.read_csv("dataset/dataset_baru.csv",parse_dates=["order_date"])
df.head()


# In[8]:


data = go.Scatter(
    x=df.sales,
    y=df.profit,
    mode="markers",
    name="Sales VS profit"
)
fig = go.Figure(data=data)
iplot(fig)


# In[10]:


import numpy as np


# In[15]:


import numpy as np


# In[16]:


df.head()


# In[17]:


data.drop(["marker color", "marker_color"], axis = 1, inplace = True) 


# In[19]:


df.drop(["marker color", "marker_color"], axis = 1, inplace = True) 


# In[20]:


df.head()


# In[21]:


import numpy as np


# In[22]:


df["marker_color"] = np.where(
    df.profit >=0,
    "green",
    "red",
)


# In[23]:


df.head()


# In[26]:


data = go.Scatter(
    x=df.sales,
    y=df.profit,
    mode="markers",
    marker={
        "color":df.marker_color,
    },
    name="Sales VS profit"
)
fig = go.Figure(data=data)
iplot(fig)


# In[27]:


data = go.Pie(labels=df.segment, values=df.sales)
fig = go.Figure(data=data)
iplot(fig)


# In[28]:


data = go.Histogram(x=df.sales)
fig = go.Figure(data=data)
iplot(fig)


# In[30]:


data = go.Histogram(
    x=df.sales,
    xbins={
        "size" : 500,
    }
    )
fig = go.Figure(data=data)
iplot(fig)


# In[32]:


df_segment = df.groupby("segment").agg({"sales" : "sum"})
df_segment = df_segment.reset_index()
df_segment.head()


# In[33]:


data =go.Bar(
    x=df_segment.segment, 
    y=df_segment.sales
)
fig = go.Figure(data=data)
iplot(fig)


# In[36]:


df_segment_category = df.groupby(["segment","category"]).agg({
    "sales" : "sum",
})
df_segment_category = df_segment_category.reset_index()
df_segment_category.head()                              


# In[ ]:





# In[38]:


bar1 = go.Bar(
    x=df_segment_category [df_segment_category.segment == "Coorprate"].category, 
    y=df_segment_category [df_segment_category.segment == "Coorprate"].sales,
    name ="Coorprate"
)
bar2 = go.Bar(
    x=df_segment_category [df_segment_category.segment == "Consumer"].category, 
    y=df_segment_category [df_segment_category.segment == "Consumer"].sales,
    name ="Consumer"
)

bar3 = go.Bar(
    x=df_segment_category [df_segment_category.segment == "Home Office"].category, 
    y=df_segment_category [df_segment_category.segment == "Home Office"].sales,
    name ="Home Office"
)

data = [bar1,bar2,bar3]

fig = go.Figure(data=data)
iplot(fig)


# In[39]:


data = [bar1,bar2,bar3]
layout ={"barmode" : "stack"}
fig = go.Figure(data=data, layout=layout)
iplot(fig)


# In[40]:


df["month"]= df.order_date.dt.strftime("%y-%m-01")
df.head()


# In[41]:


df_monthly_sales = df.groupby("month").agg({"sales": "sum"})
df_monthly_sales = df_monthly_sales.reset_index()
df_monthly_sales.head()


# In[42]:


data = go.Scatter(
    x=df_monthly_sales.month,
    y=df_monthly_sales.sales,
)
fig = go.Figure(data=data)
iplot(fig)


# In[44]:


data = go.Scatter(
    x=df_monthly_sales.month,
    y=df_monthly_sales.sales,
    mode="lines+markers"
)
fig = go.Figure(data=data)
iplot(fig)


# In[50]:


df_monthly_sales_category = df.groupby(["month","category"]).agg({"sales":"sum"})
df_monthly_sales_category = df_monthly_sales_category.reset_index()
df_monthly_sales_category.head()


# In[52]:


df_monthly_sales_category = df_monthly_sales_category.pivot(
        index="month",
        columns = "category",
        values="sales",
)
df_monthly_sales_category.head()


# In[54]:


line1 = go.Scatter(
    x=df_monthly_sales_category.index,
    y=df_monthly_sales_category["Furniture"],
    mode="lines+markers",
    name="Furniture"
)

line2 = go.Scatter(
    x=df_monthly_sales_category.index,
    y=df_monthly_sales_category["Office Supplies"],
    mode="lines+markers",
    name="Office Suplies"
)

line3 = go.Scatter(
    x=df_monthly_sales_category.index,
    y=df_monthly_sales_category["Technology"],
    mode="lines+markers",
    name="Technology"
)

data=[line1,line2,line3]

fig = go.Figure(data=data)
iplot(fig)


# In[56]:


line1 = go.Scatter(
    x=df_monthly_sales_category.index,
    y=df_monthly_sales_category["Furniture"],
    mode="lines+markers",
    marker={"symbol" : "diamond"},
    name="Furniture"
)

line2 = go.Scatter(
    x=df_monthly_sales_category.index,
    y=df_monthly_sales_category["Office Supplies"],
    mode="lines+markers",
     marker={"symbol" : "diamond"},
    name="Office Suplies"
)

line3 = go.Scatter(
    x=df_monthly_sales_category.index,
    y=df_monthly_sales_category["Technology"],
    mode="lines+markers",
     marker={"symbol" : "diamond"},
    name="Technology"
)

data=[line1,line2,line3]

fig = go.Figure(data=data)
iplot(fig)


# In[ ]:




