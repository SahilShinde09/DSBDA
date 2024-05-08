# -*- coding: utf-8 -*-
"""Experiment_5_Data_AnalyticsII.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LTKCAMheq84Aru4QUZ5s3y3VYDKxFyr7
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\College\TE\SEM-2\Practical\DSBDA\5\Social_Network_Ads.csv")

dataset.head()

dataset.info()

dataset.isnull().sum()

dataset.shape

x = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values

print(x)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

print(y_pred)

print(y_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

Accuracy=(74+31)/120
Accuracy

Error_rate=(5+10)/120
Error_rate

from sklearn.metrics import precision_score, recall_score
precision_score(y_test, y_pred)

recall_score(y_test, y_pred)

from sklearn.metrics import f1_score
f1_score(y_test, y_pred)

