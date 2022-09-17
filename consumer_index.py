#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


# In[3]:


df= pd.read_csv("D:\\IISc\\sem3\\research_methods\\data_sets\\a5df75bc-4578-48ad-bc9d-e6eb4b63de0a.csv")


# In[4]:


# print(df.head)


# In[5]:


# for column_num in df.columns:
#     print(column_num)


# In[6]:


df_1 = df.loc[2::,"Transport and communication"]
df_2 = df.loc[2::,"Meat and fish"]


# In[7]:


df_1_numpy = df_1.to_numpy()
df_2_numpy = df_2.to_numpy()


# In[8]:


#scatter plot 
print(df_1_numpy.shape)


# In[9]:


df_3 = df.loc[2::,"Pulses and products"]
df_4 = df.loc[2::,"Spices"]

df_5 = df.loc[2::,"Clothing"]
df_6 = df.loc[2::,"Housing"]

df_7 = df.loc[2::,"Oils and fats"]
df_8 = df.loc[2::,"Food and beverages"]

df_9 = df.loc[2::,"Health"]
df_10 = df.loc[2::,"Recreation and amusement"]


# In[10]:


df_3_numpy = df_3.to_numpy()
df_4_numpy = df_4.to_numpy()
df_5_numpy = df_5.to_numpy()
df_6_numpy = df_6.to_numpy()
df_7_numpy = df_7.to_numpy()
df_8_numpy = df_8.to_numpy()
df_9_numpy = df_9.to_numpy()
df_10_numpy = df_10.to_numpy()


# In[18]:


fig1 = plt.figure()
plt.title("Meat and fish  vs Transport and communication")
plt.grid()
# ax = fig.add_subplot(111)
# ax.set_aspect('equal', adjustable='box')
plt.xlim(100,220)
plt.ylim(100,220)
ax1 = plt.gca()
x = np.linspace(100,220)
ax1.plot(x, x,linestyle='dashed',color = "black")
plt.scatter(df_1_numpy,df_2_numpy,color='red',marker='x',linewidths=1)
# plt.plot([-.2,1.2], [-.2,1.2], linestyle='--', color='k')/

plt.ylabel("Meat and fish")
plt.xlabel("Transport and communication")
plt.savefig('scatter_meat_transport.jpg')
plt.show()

fig2 = plt.figure()
plt.title("Spices vs Transport and communication")
plt.grid()
plt.xlim(100,220)
plt.ylim(100,220)
ax2 = plt.gca()
x = np.linspace(100,220)
ax2.plot(x, x,linestyle='dashed',color = "black")
plt.scatter(df_1_numpy,df_4_numpy,color='blue',marker='x',linewidths=1)
plt.xlabel("Transport and communication")
plt.ylabel("Spices")
plt.savefig('scatter_Spices_transport.jpg')
plt.show()



# In[17]:


plt.grid()
plt.title("Colthing and Housing vs Transport and communication")
plt.scatter(df_1_numpy,df_7_numpy,color='red',marker='x',label = "Clothing")
plt.scatter(df_1_numpy,df_9_numpy,color='blue',marker='x',label = "Housing")
plt.legend(loc="upper left")
plt.xlim(100,220)
plt.ylim(100,220)
ax2 = plt.gca()
x = np.linspace(100,220)
ax2.plot(x, x,linestyle='dashed',color = "black")
plt.xlabel("Transport and communication")
plt.ylabel("Clothing and Housing ")
plt.savefig('scatter_clothing_housing.jpg')
plt.show()


# In[325]:


#pandas separate out rural-urban from the data_set. 
# print(df.index)
df_rural = df[df["Sector"] == "Rural"]
df_urban = df[df["Sector"] == "Urban"]
df_ruralUrban = df[df["Sector"] == "Rural+Urban"]
# df_ruralUrban = 


# In[326]:


print(df_rural.shape)
print(df_urban.shape)
print(df_ruralUrban.shape)


# In[352]:


plt.figure()
box_data1 = df_rural["Cereals and products"].dropna()
box_data2 = df_urban["Cereals and products"].dropna()
box_data3 = df_ruralUrban["Cereals and products"].dropna()

all_box_data_cereal = pd.DataFrame([box_data1,box_data2,box_data3], columns=['Col1', 'Col2', 'Col3'])
plt.title("Consumer price index for Cereal and Products")
# print(all_box_data_cereal.isnull().values.any())


plt.boxplot([box_data1,box_data2,box_data3])
plt.xticks([1,2,3],["Rural","Urban","Rural+Urban"])
plt.ylabel("Consumer price index")


plt.savefig('box_cereal.jpg')
plt.show()

# plt.figure()
# plt.boxplot(box_data1)
# plt.xlabel("Cereals and products(Rural)")
# plt.ylabel("Consumer price index")
# plt.boxplot(box_data2)
# plt.xlabel("Cereals and products(Urban)")
# plt.boxplot(box_data3)
# plt.xlabel("Cereals and products(Rural and Urban)")


# In[328]:


#Line Plot


# In[342]:


df_July = df[df["Month"] == "July"]
print(df_July.shape)


df_R = df_July[df_July["Sector"] == "Rural"]
df_U = df_July[df_July["Sector"] == "Urban"]
df_RU = df_July[df_July["Sector"] == "Rural+Urban"]
# line_rural =df_R["Fuel and light"].dropna()
# line_urban =df_U["Fuel and light"].dropna()
# line_ruralUrban =df_RU["Fuel and light"].dropna()
# plt.figure()
# plt.plot()
# plt.plot()


# In[353]:


plt.figure()
plt.title("Fuel and light consumer index vs Year for the Month of July")
plt.grid()
#pd.to_datetime(df_rural[['Year', 'Month']].assign(DAY=1))
plt.plot(df_R["Year"],df_R["Fuel and light"],color = "blue",label = "Rural")
plt.plot(df_U["Year"],df_U["Fuel and light"],color = "red",label = "Urban")
plt.plot(df_RU["Year"],df_RU["Fuel and light"],color = "green",label = "Rural+Urban")
plt.legend(loc = "upper left")
# plt.plot(line_urban)
# plt.plot(line_ruralUrban)
plt.xlabel("Year")
plt.ylabel("Fuel and Light consumer index")
plt.savefig('line_july.jpg')
plt.show()


# In[ ]:




