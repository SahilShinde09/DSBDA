# -*- coding: utf-8 -*-
"""Experiment_1_Data_wrangling.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1N0vunx_e4sKdNkFP-j873u23OOIDjtjV
"""

pip install pandas

import pandas as pd

df = pd.read_csv(r"D:\College\TE\SEM-2\Practical\DSBDA\1\StudentsPerformance.csv")

print(df)

df.head(10)

df.isnull().sum()

print(df.describe())

df.dtypes

df.dropna(axis=1)

y = df.iloc[:, 0:1]
print(y)

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y = le.fit_transform(y)
print(y)

print(df['race/ethnicity'].value_counts())

df_Lunch = pd.get_dummies(df['lunch'])
df_new = pd.concat([df, df_Lunch], axis=1)
print(df_new)

