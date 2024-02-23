import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns
import vizualize as viz

# Data Import
df2=pd.read_csv("/content/scaled_standard_dataset.csv",index_col=0,na_values="??")
df=df2.copy(deep=True)

df.head()

df.info()

df.isnull().sum()

df.describe(include='all')

raw_correl=df.corr(method='spearman').round(2)
viz.heatmap(raw_correl)

threshold=0.11
relative_correl=raw_correl['cardio']
raw_cols=relative_correl[abs(relative_correl)>threshold].index.tolist()
raw_features=df[raw_cols]
raw_features.head()

new_correl=raw_features.corr(method='spearman').round(2)
viz.heatmap(new_correl)

for col in raw_cols:
  viz.histplot(df[col])

def scatter(col):
  plt.figure(figsize = (8,8))
  sns.scatterplot(data= raw_features, x= col, y = raw_features.cardio)
  plt.show()

for cols in raw_cols:
  scatter(cols)

raw_features.head()

raw_features.to_csv("feature_extracted_raw.csv")
