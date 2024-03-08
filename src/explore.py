import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from vizualize import heat_map

def univariate():
    df = pd.read_csv('merged_train_data.csv')

    """Here we are doing univariate analysis on different columns of our data set Using:
    1. We calculate mean, median, mode of the data.
    2. we calculate the frequency of the data.
    3. Then we visualise using Box plot and different graph,
    *box plot: there are 4 parts -
        1) Min/Max Point,
        2) Quartiles(Q1=25% Data and Q3=75%Data)
        3) Median Q2
        4) Outliers
        AGE COLUMN
    """

    df['age'].describe()
    df['age'].median()
    df['age'].mode()
    df['age'].value_counts()

    df.boxplot(column=['age'], grid=False, color='black')

    """There is an outlier at the age of 30 which we can find from box plot other than that min value is 38 and max is 65 which also seen from box plot and data is left skewed"""
    df.hist(column='age', grid=False, edgecolor='black')

    """Majority of age is between 40 to 64

    Height Column
    """

    df['height'].describe()

    df['height'].value_counts()

    df['height'].mode()

    df.boxplot(column=['height'], grid=False, color='black')

    """Largely the height data is between 160 to 170 cm which is visible from below graph and there are outliers from 140 for minimum and from 190 for maximum that is visible from box plot and distribution is symmetric."""

    df.hist(column='height', grid=False, edgecolor='black')

    """Weight Column"""

    df['weight'].describe()

    df['weight'].value_counts()

    df['weight'].mode()

    """Here we have almost similar frequency of people havin weight 65 and 70"""

    df.boxplot(column=['weight'], grid=False, color='black')

    """From the above box plot we can see that the distribution is right skewed.

    From the below graph we can see that there are more number of people having weight between 50 to 75 .
    """

    df.hist(column='weight', grid=False, edgecolor='black')

    """BMI Column"""

    df['bmi'].describe()

    df['bmi'].median()

    df['bmi'].value_counts()

    df.boxplot(column=['bmi'], grid=False, color='black')

    """From the below graph we can see that there are more number of  people having bmi between 22 to 30 and from the box plot we can find some outliers too along with the distribution which is right skewed"""

    df.hist(column='bmi', grid=False, edgecolor='black')

    """Alcohol Column"""

    df['alco'].value_counts()

    df.hist(column='alco', grid=False, edgecolor='black')

    """people do not consume alcohol are more than 50000 while those who consume are below 3000 which is almost 16 times of it.

    Smoke column
    """

    df['smoke'].value_counts()

    df.hist(column='smoke', grid=False, edgecolor='black')

    """The number of people who do not smoking are 10 times in number compare to those who smoke .

    Physical Activity column
    """

    df['active'].value_counts()

    df.hist(column='active', grid=False, edgecolor='black')

    """There are higher number of people who are physically active"""


def explore_hist():
    df = pd.read_csv('merged_train_data.csv')
    df

    df['gender'].mean()

    df['gender'].median()

    df['gender'].std()

    df['gender'].value_counts()

    df.hist(column='gender', grid=False, edgecolor='black', color='red')

    """There are more Females than Males."""

    df['bp_high'].mean()

    df['bp_high'].median()

    df['bp_high'].std()

    df['bp_high'].value_counts()


    df.hist(column='bp_high', grid=False, edgecolor='black', color = 'darkblue')

    df['bp_lo'].describe()

    df.hist(column='bp_lo', grid=False, edgecolor='black', color='purple')

    df.hist(column='cholesterol_1', grid=False, edgecolor='black', color='blue')

    df.hist(column='cholesterol_2', grid=False, edgecolor='blue', color='black')

    df.hist(column='cholesterol_3', grid=False, edgecolor='black', color='red')

    df.hist(column='gluc_1', grid=False, edgecolor='black', color='blue')

    df.hist(column='gluc_2', grid=False, edgecolor='black', color='blue')

    df.hist(column='gluc_3', grid=False, edgecolor='black', color='blue')

    df.hist(column='diabetic_1', grid=False, edgecolor='black', color='red')

    df.hist(column='diabetic_2', grid=False, edgecolor='black', color='red')

    df.hist(column='diabetic_3', grid=False, edgecolor='black', color='red')


def multicollinarity(data_frame):
    heat_map(data_frame, "pearson")
    heat_map(data_frame, "spearman")
    heat_map(data_frame, "kendall")


def scaled_matrix(data_frame):
    correl =data_frame.corr(method='pearson').round(2)
    plt.figure(figsize=(15,15))
    sns.heatmap(correl,annot=True)
    plt.show()

    correl =data_frame.corr(method='spearman').round(2)
    plt.figure(figsize=(15,15))
    sns.heatmap(correl,annot=True)
    plt.show()

    correl =data_frame.corr(method='kendall').round(2)
    plt.figure(figsize=(15,15))
    sns.heatmap(correl,annot=True)
    plt.show()


    # Selecting only the numeric columns for correlation calculation
    numeric_columns = data_frame.select_dtypes(include=['int64', 'float64'])

    correlation_matrix = numeric_columns.corr()
    
    return correlation_matrix