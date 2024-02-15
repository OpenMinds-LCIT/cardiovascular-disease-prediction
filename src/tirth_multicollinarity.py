# -*- coding: utf-8 -*-
"""multiCollinarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UAfV8CrQwxsM1UJOfC-Hd75UEfs_QpDf
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns

df = pd.read_csv('scaled_dataset.csv')
df.head(7)

correl=df.corr(method='pearson').round(2)
plt.figure(figsize=(15,15))
sns.heatmap(correl,annot=True)
plt.show()

correl=df.corr(method='spearman').round(2)
plt.figure(figsize=(15,15))
sns.heatmap(correl,annot=True)
plt.show()

correl=df.corr(method='kendall').round(2)
plt.figure(figsize=(15,15))
sns.heatmap(correl,annot=True)
plt.show()