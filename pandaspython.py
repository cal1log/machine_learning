#!/usr/bin/env python3

import numpy as np
import pandas as pd


data = np.array([
    ['', 'Col1', 'Col2'],
    ['Fila1', 11, 22],
    ['Fila2', 33, 44]
])
print(pd.DataFrame(
    data=data[1:, 1:],
    index=data[1:, 0],
    columns=data[0, 1:]
))

print()

df = pd.DataFrame(
    np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
)

print(df)
print()

''' series '''
series = pd.Series({
    "Argentina": "Buenos Aires",
    "Colombia": "Bogota",
    "Peru": "Lima"
})

print("Series")
print(series)
print()

''' dataframe functions '''

''' shape '''
print('Shape Dataframe')
print(df.shape)
print()

''' index '''
print('indexes')
print(df.index)
print()

''' height '''
print('height dataframe')
print(len(df.index))
print()

''' statistics '''
print('statistics')
print(df.describe())
print()

''' mean '''
print('mean')
print(df.mean())
print()

''' co relation '''
print('co relation')
print(df.corr())
print()

''' not null values '''
print('not null values')
print(df.count())
print()

''' highest value in every column '''
print(' highest value')
print(df.max())
print()

''' lowest value in every column '''
print('lowest value')
print(df.min())
print()

''' median value in every column '''
print('median value')
print(df.median())
print()

''' standard deviation value in every column '''
print('standard deviation value')
print(df.std())
print()

''' first dataframe column '''
print('first dataframe column')
print(df[0])
print()

''' selecting two columns and creating a new dataframe '''
print('selecting two columns and creating new dataframe')
print(df[[0, 2]])
print()

''' select a value with its row and column dataframe'''
print('selecting a single value')
print(df.iloc[1][1])
print()

''' first row values '''
print('first row with loc')
print(df.loc[0])
print()

''' first row values '''
print('first row with iloc')
print(df.iloc[0,:])
print()

''' read a csv file '''
print('reading csv file')
print()
df = pd.read_csv('/home/calilog/Documents/train.csv')
print(df)
print()

''' null values '''
print('null values')
print()
print(df.isnull())
print()

''' null values sum '''
print('null values sum')
print()
print(df.isnull().sum())
print()

''' delete row if there is null values'''
print('delete row')
print()
print(df)
print()
print(df.dropna())
print()

''' delete column if there is null values'''
print('delete column')
print()
print(df)
print()
print(df.dropna(axis=1))
print()

''' fill null values with any value '''
print('fill null values with orlando text')
print()
print(df)
print()
print(df.fillna('orlando'))
print()
