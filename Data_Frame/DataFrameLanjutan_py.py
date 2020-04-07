#!/usr/bin/env python
# coding: utf-8

# In[1]:


numbers [1, 2, 3, 4, 5, 6]


# In[2]:


Numbers = [1, 2, 3, 4, 5, 6]


# In[3]:


Numbers


# In[4]:


len (Numbers)


# In[5]:


Numbers.append(6)


# In[6]:


Numbers


# In[7]:


Numbers[2:5]


# In[8]:


Numbers[:4]


# In[9]:


Numbers[1:]


# In[10]:


biodata = {
    "nama" : "andi",
    "umur" : "20",
    "alamat" : "bogor"
}


# In[11]:


biodata.keys()


# In[12]:


biodata.values()


# In[13]:


import pandas as pd


# In[14]:


outlook = [
"sunny", "sunny", "overcast", "rainy", "rainy",
"rainy", "overcast", "sunny", "sunny", "rainy",
"sunny", "overcast", "overcast", "rainy",
]

temp [
"hot", "hot", "hot", "mild", "cool",
"cool", "cool", "mild","cool","mild",
"mild","mild","hot","mild",
]

humadity[
"high","high","high","high","normal",
"normal","normal","high","normal","normal",
"normal","high","normal","high",
]

windy = [
False,True,False,False,False,
True,True,False,False,False,
True,True,False,True,
]

play = [
"no","no","yes","yes","yes",
"no", "yes","no","yes","yes",
"yes","yes","yes","no",
]


# In[15]:


outlook = [
"sunny", "sunny", "overcast", "rainy", "rainy",
"rainy", "overcast", "sunny", "sunny", "rainy",
"sunny", "overcast", "overcast", "rainy",
]

temp [
"hot", "hot", "hot", "mild", "cool",
"cool", "cool", "mild","cool","mild",
"mild","mild","hot","mild",
]

humadity[
"high","high","high","high","normal",
"normal","normal","high","normal","normal",
"normal","high","normal","high",
]

windy = [
False,True,False,False,False,
True,True,False,False,False,
True,True,False,True,
]

play = [
"no","no","yes","yes","yes",
"no", "yes","no","yes","yes",
"yes","yes","yes","no",
]


# In[16]:


outlook = [
"sunny", "sunny", "overcast", "rainy", "rainy",
"rainy", "overcast", "sunny", "sunny", "rainy",
"sunny", "overcast", "overcast", "rainy",
]

temp = [
"hot", "hot", "hot", "mild", "cool",
"cool", "cool", "mild","cool","mild",
"mild","mild","hot","mild",
]

humadity = [
"high","high","high","high","normal",
"normal","normal","high","normal","normal",
"normal","high","normal","high",
]

windy = [
False,True,False,False,False,
True,True,False,False,False,
True,True,False,True,
]

play = [
"no","no","yes","yes","yes",
"no", "yes","no","yes","yes",
"yes","yes","yes","no",
]


# In[17]:


df = pd.DataFrame(
    {
    "outlook" : outlook,
    "temp" : temp,
    "humadity" : humadity,
    "windy" : windy,
    "play" : play,
    }
)


# In[18]:


df


# In[19]:


df.shape


# In[20]:


df.describe()


# In[21]:


df.outlook.describe()


# In[22]:


df=["new_column"] = "new value"


# In[23]:


df["new_column"] = "new value"


# In[24]:


df


# In[25]:


df["play-1"] = df["play"].shift[-1]


# In[26]:


df["play-1"] = df["play"].shift(-1)


# In[27]:


df


# In[28]:


df.head()


# In[29]:


df.tail()


# In[30]:


df.sample()


# In[31]:


df=[["outlook", "temp"]]


# In[32]:


df[["outlook", "temp"]]


# In[33]:


df.sample()


# In[34]:


outlook = [
"sunny", "sunny", "overcast", "rainy", "rainy",
"rainy", "overcast", "sunny", "sunny", "rainy",
"sunny", "overcast", "overcast", "rainy",
]

temp = [
"hot", "hot", "hot", "mild", "cool",
"cool", "cool", "mild","cool","mild",
"mild","mild","hot","mild",
]

humadity = [
"high","high","high","high","normal",
"normal","normal","high","normal","normal",
"normal","high","normal","high",
]

windy = [
False,True,False,False,False,
True,True,False,False,False,
True,True,False,True,
]

play = [
"no","no","yes","yes","yes",
"no", "yes","no","yes","yes",
"yes","yes","yes","no",
]


# In[35]:


df.sample()


# In[36]:


df = pd.DataFrame(
    {
    "outlook" : outlook,
    "temp" : temp,
    "humadity" : humadity,
    "windy" : windy,
    "play" : play,
    }
)


# In[ ]:





# In[37]:


df


# In[38]:


df.sample()


# In[39]:


df.outlook


# In[40]:


df.outlook.unique()


# In[ ]:




