
# coding: utf-8

# In[20]:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[2]:

df = pd.read_csv("C:/Users/Krishna/Desktop/911.csv (2)/911.csv")


# In[3]:

df.head()


# In[4]:

df['title'][0].split(':')[0]


# In[7]:

df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])


# In[9]:

df['Reason'].value_counts()


# In[21]:

sns.countplot(x='Reason', data=df)


# In[14]:

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
time = df['timeStamp'].iloc[0]
time.hour


# In[15]:

df['Hour']= df['timeStamp'].apply(lambda tid: tid.hour)
df['Month']= df['timeStamp'].apply(lambda tid: tid.month)
df['Day of Week']= df['timeStamp'].apply(lambda tid: tid.dayofweek)
df.head()


# In[16]:

days = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}


# In[17]:

df['Day of Week'] = df['Day of Week'].map(days)


# In[18]:

df.head()


# In[22]:

sns.countplot(x="Day of Week", data=df, hue='Reason')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)


# In[24]:

df['Date'] = df['timeStamp'].apply(lambda dat: dat.date())
df['Date'].head()


# In[25]:

byDate = df.groupby(df['Date']).count()['lat']
byDate.head()
byDate.plot()
plt.tight_layout()


# In[26]:

# Reason of Traffic that people called 911 
df[df['Reason']=='Traffic'].groupby('Date').count()['lat'].plot()
plt.title('Traffic')
plt.tight_layout()


# In[27]:

df[df['Reason']=='Fire'].groupby('Date').count()['lat'].plot()
plt.title('Fire')
plt.tight_layout()


# In[28]:

# Reason of EMS people called 911
df[df['Reason']=='EMS'].groupby('Date').count()['lat'].plot()
plt.title('EMS')
plt.tight_layout()


# In[30]:

# Full Explanation graph for people called 911 by various reasons.
plt.figure(figsize=(12,6))
dayHour = df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()
sns.heatmap(dayHour, cmap='viridis')


# In[34]:

# Reason of calling 911 by day of month
df.groupby(by=['Day of Week', 'Hour']).count()['Reason'].unstack()


# In[ ]:



