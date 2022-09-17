#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


# In[115]:



# df= pd.read_csv("D:\\IISc\\sem3\\research_methods\\data_sets\\a5df75bc-4578-48ad-bc9d-e6eb4b63de0a.csv")
df=pd.read_csv("D:\\IISc\\sem3\\research_methods\\data_sets\\south_pen-India_rainfall_act_dep_1901_2016.csv")


# In[116]:


#Line Plot 
df.plot(x="YEAR", y=["Actual Rainfall: JUN", "Actual Rainfall: JUL","Actual Rainfall: SEPT"], kind="line", figsize=(20,8))
plt.title(label="Monthwise report for rainfall in Peninsular India (1900-2016)",fontsize = 20)
plt.xlabel("YEAR",fontsize = 16)
plt.ylabel("Actual rainfall (mm)",fontsize = 16)
plt.savefig("Line_rainfall.jpg")
plt.show()


# In[117]:


#Bar plot

df_1970 = df[df["YEAR"] > 1969]
print(df_1970.shape)
fig = plt.figure()


df_1970.plot(x="YEAR", y=["Actual Rainfall: JUN-SEPT"], kind="bar", figsize=(30,11), color = 'cyan', width = 0.7)

plt.title(label="Yearwise report for Average rainfall in Peninsular India(1980-2016)", fontsize=32)
plt.ylabel("Rainfall in mm", fontsize=21)
plt.xlabel("YEAR", fontsize=21)
plt.savefig("bar_rainfall.jpg")
plt.show()


# In[118]:


#scatter plot
x = df['YEAR']
y1 = df['Actual Rainfall: JUN']
y2=df['Actual Rainfall: JUL']
y3=df['Actual Rainfall: AUG']
plt.figure(figsize=(20, 8))

plt.subplot(1, 2, 1)
plt.scatter(y1,y2,color = 'red')
plt.title(label="Rainfall in July vs Rainfall in June")
plt.xlabel("Rainfall in June")
plt.ylabel("Rainfall in July")
plt.xlim(90,375)
plt.ylim(90,375)
ax1 = plt.gca()
x = np.linspace(90,375)
ax1.plot(x, x,linestyle='dashed',color = "black")

plt.subplot(1, 2, 2)
plt.scatter(y1,y3,color = 'blue')
plt.title(label="Rainfall in August vs Rainfall in June")
plt.xlabel("Rainfall in June")
plt.ylabel("Rainfall in August")
plt.xlim(50,300)
plt.ylim(50,300)
ax2 = plt.gca()
x = np.linspace(50,300)
ax2.plot(x, x,linestyle='dashed',color = "black")

# y=df['Actual Rainfall: AUG']
# plt.subplot(2, 2, 3)
# plt.scatter(x,y,color = 'green')
# plt.title(label="Rainfall in Peninsular India for August for 116 years")

# y=df['Actual Rainfall: SEPT']
# plt.subplot(2, 2, 4)
# plt.scatter(x,y,color = 'yellow')
# plt.title(label="Rainfall in Peninsular India for September for 116 years")

plt.savefig("scatter_rainfall.jpg")
plt.show()


# In[119]:


#box plot
box_plot_JUN=df["Actual Rainfall: JUN"]
box_plot_JUL=df["Actual Rainfall: JUL"]
box_plot_AUG=df["Actual Rainfall: AUG"]
box_plot_SEPT=df["Actual Rainfall: SEPT"]
plt.figure(figsize=(10, 10))
plt.title("Rainfall (in mm) for various months",fontsize =14)
plt.boxplot([box_plot_JUN,box_plot_JUL,box_plot_AUG,box_plot_SEPT])
plt.xticks([1,2,3,4],["June","July","August","September"])
plt.ylabel("Rainfall (in mm)")
plt.savefig("box_rainfall.jpg")
plt.show()


# In[ ]:




