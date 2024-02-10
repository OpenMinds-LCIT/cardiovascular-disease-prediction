import pandas as pd
import xlrd

df = pd.read_excel('cleaned_data.xlsx')
df

df.head()

df.info()

my_column = df[['smoke','alco']]
#print(my_column)
my_column.head()

my_column.shape

from matplotlib import pyplot as plt
df.plot(kind='scatter', x='smoke', y='alco')
plt.gca().spines[['top', 'right',]].set_visible(False)
