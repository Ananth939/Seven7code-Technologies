# -*- coding: utf-8 -*-
"""Mall_Customer_Segmentation_Data

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Fq0_LZVe-IcQ1x5qXeHelfeGoufbUHYO
"""

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import plotly as py
import plotly.graph_objs as go
import warnings

df=pd.read_csv('Mall_Customers.csv')
df.head()

df.info()

df.describe()

df.isnull().values.any()

df.drop(['Gender'],axis=1,inplace=True)
df

sns.distplot(df['Age'])

sns.distplot(df['Annual Income (k$)'])

sns.distplot(df['Spending Score (1-100)'])

df1=df[["Annual Income (k$)","Spending Score (1-100)"]]
df1

df1.plot(kind="scatter",x="Annual Income (k$)",y="Spending Score (1-100)",figsize=(10,7))
plt.show()

df3=df[["Age","Spending Score (1-100)"]]
df3

df3.plot(kind="scatter",x="Age",y="Spending Score (1-100)",figsize=(10,7))
plt.show()

sum_of_sqr_dist={}
for k in range(1,10):
    km=KMeans(n_clusters=k,init='k-means++',max_iter=1000)
    km=km.fit(df1)
    sum_of_sqr_dist[k]=km.inertia_

sns.pointplot(x=list(sum_of_sqr_dist.keys()),y=list(sum_of_sqr_dist.values()))
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Sum of square distances")
plt.title("Elbow curve")
plt.show()

model=KMeans(n_clusters=5,init="k-means++",max_iter=150)
model.fit(df1)

print("labels", model.labels_)

print("Centroids",model.cluster_centers_)

centroids=model.cluster_centers_

df1_cluster=df1.copy()
df1_cluster["cluster"]=model.fit_predict(df1)

df1_cluster.head()

color=['red','yellow','green','blue','pink']
df1_cluster['color']=df1_cluster['cluster'].map(lambda p:color[p])

plt.figure(figsize=(20,10))
plt.scatter(df1["Annual Income (k$)"],df1["Spending Score (1-100)"],c=df1_cluster["color"])
plt.scatter(centroids[:,0], centroids[:,1],c='black',s=200)

labels=model.labels_

silhouette_score(df1,labels)

