# -*- coding: utf-8 -*-
"""10Jul_House_Price_Prediction.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WCfhtko588V4s-EO_uC1JXz7SVJ93vO6
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('Housing.csv')
df.head()

df.shape

df.isnull().sum()

df.dtypes

cat_cols = [i for i in df.columns if df[i].dtypes=='object']
cat_cols

df['mainroad'].value_counts()

df['guestroom'].value_counts()

df['basement'].value_counts()

df['hotwaterheating'].value_counts()

df['airconditioning'].value_counts()

df['prefarea'].value_counts()

df['furnishingstatus'].value_counts()

from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()
for i in cat_cols:
    df[i] = lb.fit_transform(df[i])

# df['mainrod'] = lb.fit_transform(df['mainroad'])
# df['guestroom'] = lb.fit_transform(df['guestroom'])
# df['basement'] = lb.fit_transform(df['basement'])

df.dtypes

x = df.drop('price',axis=1)
y = df['price']
print(type(x))
print(type(y))

print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.25)
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

"""#### Linear Regression"""

from sklearn.linear_model import LinearRegression

m1 = LinearRegression()
m1.fit(x_train,y_train)

# r2 score
print('Training score',m1.score(x_train,y_train))
print('Testing score',m1.score(x_test,y_test))

ypred_m1 = m1.predict(x_test)
print(ypred_m1)

from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

print('MSE',mean_squared_error(y_test,ypred_m1))
print('RMSE',np.sqrt(mean_squared_error(y_test,ypred_m1)))
print('MAE',mean_absolute_error(y_test,ypred_m1))
print('r2_Score',r2_score(y_test,ypred_m1))

