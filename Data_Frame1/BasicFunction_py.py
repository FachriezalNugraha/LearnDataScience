#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("dataset/dataset.csv")


# In[3]:


df = pd.read_csv("dataset/dataset_123.csv")


# In[4]:


df = pd.read_csv("dataset/dataset_baru.csv")


# In[5]:


df = pd.read_csv("../dataset/dataset_baru.csv")


# In[6]:


df.head()


# In[7]:


df.dtypes


# In[8]:


df = pd.read_csv("../dataset/dataset_baru.csv", parse_dates["order_date"])


# In[9]:


df = pd.read_csv("../dataset/dataset_baru.csv", parse_dates["order_date"])
df.head()


# In[10]:


df = pd.read_csv("../dataset/dataset_baru.csv", parse_dates=["order_date"])
df.head()


# In[11]:


df.dtypes


# In[12]:


order_ids = ["CA-2016-152156","CA-2016-152156", "CA-2016-138688", "US-2015-108966" , "US-2015-108966"]
couriers = ["courier A", "courier A" , None , "courier B", "courier B"]

df.couriers = pd.DataFrame({
    "oder_id" : order_ids,
    "courier" : couriers,
})
df_courier.head()


# In[13]:


order_ids = ["CA-2016-152156","CA-2016-152156", "CA-2016-138688", "US-2015-108966" , "US-2015-108966"]
couriers = ["Courier A", "Courier A" , None , "Courier B", "Courier B"]

df.couriers = pd.DataFrame({
    "oder_id" : order_ids,
    "courier" : couriers,
})
df_courier.head()


# In[19]:


order_ids = ["CA-2016-152156","CA-2016-152156", "CA-2016-138688", "US-2015-108966" , "US-2015-108966"]
couriers = ["Courier A", "Courier A" , None , "Courier B", "Courier B"]

df.courier = pd.DataFrame({
    "oder_id" : order_ids,
    "courier" : couriers,
})
df_courier.head()


# In[21]:


order_ids = ["CA-2016-152156","CA-2016-152156", "CA-2016-138688", "US-2015-108966" , "US-2015-108966"]
couriers = ["Courier A", "Courier A" , None , "Courier B", "Courier B"]

df_courier = pd.DataFrame({
    "oder_id" : order_ids,
    "courier" : couriers,
})
df_courier.head()


# In[22]:


df_courier.isna()


# In[23]:


df_courier.isna().any("columns")


# In[24]:


df_couriers[df_courier.isna().any("columns")]


# In[25]:


df_courier[df_courier.isna().any("columns")]


# In[26]:


df_courier.to_csv("../dataset/dataset_barukkk.csv")


# In[27]:


df_courier.to_csv("../dataset/dataset_barukkk.csv", index=false)


# In[28]:


df_courier.to_csv("../dataset/dataset_barukkk.csv", index = false)


# In[29]:


df_courier.to_csv("../dataset/dataset_barukkk.csv", index : false)


# In[30]:


df_courier.to_csv("../dataset/dataset_barukkk.csv", index = "false")


# In[31]:


df_courier.to_csv("../dataset/dataset_barukkk.csv", index = False)


# In[32]:


df_head = df.head()


# In[33]:


df_tail = df.tail()


# In[34]:


df_head


# In[35]:


df_tail


# In[36]:


df_congcat = pd.congcat([df_tail, df_head])


# In[37]:


df_concat = pd.congcat([df_tail, df_head])


# In[38]:


df_concat = pd.concat([df_tail, df_head])


# In[39]:


df_concat


# In[40]:


df_concat = pd.concat([df_tail, df_head], ignore_index = true )
df_concat


# In[41]:


df_concat = pd.concat([df_tail, df_head], ignore_index = True )
df_concat


# In[42]:


df_concat.short_values("oder_date")


# In[45]:


df_concat.sort_values("oder_date")


# In[ ]:





# In[46]:


df_concat.sort_values("oder_date")


# In[47]:


df_concat.short_values("oder_date", ascending = False)


# In[48]:


df_concat.sort_values("oder_date", ascending = False)


# In[49]:


df_concat.short_values("quantity", ascending = False)


# In[50]:


df_concat.sort_values("quantity", ascending = False)


# In[51]:


df_concat.sort_values("quantity")


# In[52]:


df_concat.sort_values("order_date")


# In[53]:


df_concat.sort_values("order_date", ascending = False)


# In[54]:


df_concat = df_concat.sort_values("order_date", ascending = False)


# In[55]:


df_concat


# In[56]:


df_head = df.iloc(2:7)
df_head


# In[57]:


df_head = df.iloc[2:7]
df_head


# In[58]:


df_courier


# In[61]:


df_merge = pd.merge(df_head, df_courier, how="left" , on="order_id")
df_merge


# In[66]:


df_merge = pd.merge(df_head, df_courier ,how="left" ,on="order_id")
df_merge


# In[67]:


df_merge = pd.merge(df_head, df_courier ,how:"left" ,on:"order_id")
df_merge


# In[74]:


df_merge = pd.merge(df_head, df_courier ,how="left" ,on= "order_id")
df_merge


# In[76]:


df_head = df.iloc[2:7]
df_head


# In[77]:


df_courier


# In[97]:


df_merge = pd.merge(df_courier, df_head ,how='Left', on='Order_Id')
df_merge


# In[ ]:





# In[98]:


df_merge


# In[99]:


df_merge()


# In[100]:


df_merge = pd.merge(df_courier, df_head ,how='Left', on='Order_Id')
df_merge


# In[101]:


df_head = df.iloc[3:7]
df_head


# In[102]:


df_courier


# In[108]:


df_merge = pd.merge(df_courier, df_head ,how="Left", on="oder_id")
df_merge


# In[109]:


order_ids = ["CA-2016-152156","CA-2016-152156", "CA-2016-138688", "US-2015-108966" , "US-2015-108966"]
couriers = ["Courier A", "Courier A" , None , "Courier B", "Courier B"]

df_courier = pd.DataFrame({
    "order_id" : order_ids,
    "courier" : couriers,
})
df_courier.head()


# In[110]:


df_head = df.iloc[3:7]
df_head


# In[111]:


df_courier


# In[113]:


df_merge = pd.merge(df_courier, df_head ,how="left", on="order_id")
df_merge


# In[114]:


df_merge.drop(columns=["customer_id", "segment"])


# In[115]:


df_merge[["order_date", "category", "courier"]]


# In[116]:


df_groupby = df.groupby(["order_date", "category"]).agg({
    "sales" : "sum",
})
df_groupby


# In[117]:


df["order_month"]= df.order_date.dt.strftime("%y-%m")
df.head()


# In[118]:


df_groupby = df.groupby(["order_date", "category"]).agg({
    "sales" : "sum",
})
df_groupby


# In[119]:


df_groupby = df_groupby.reset_index()
df_groupby


# In[121]:


df_groupby = df_groupby.rename(columns=
                              {
                                  "order_date" : "date",
                              })
df_groupby


# In[122]:


df_groupby = df.groupby(["order_month", "category"]).agg({
    "sales" : "sum",
})
df_groupby


# In[123]:


df_groupby = df_groupby.reset_index()
df_groupby


# In[124]:


df_groupby = df_groupby.rename(columns=
                              {
                                  "order_month" : "month",
                              })
df_groupby


# In[125]:


df_groupby.pivot(index="month",columns="category", values="sales")


# In[ ]:




