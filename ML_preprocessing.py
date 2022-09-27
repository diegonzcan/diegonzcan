# -*- coding: utf-8 -*-
"""Data Science CoderHouse 2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DQIFdmFklpr5ZApnH3rVuLRJK_zQweaE
"""

import pandas as pd
import numpy as np

#para montar en drive
from google.colab import drive
import os
drive.mount('/content/gdrive')
# Establecer ruta de acceso en drive
import os
print(os.getcwd())
os.chdir("/content/gdrive/My Drive")

import matplotlib.pyplot as plt

df = pd.read_csv('/content/gdrive/MyDrive/Data Science CoderHouse/store_train.csv')

from datetime import datetime
df.dtypes
df['Order Date'] = pd.to_datetime(df['Order Date']) ### Convertimos Order Date a tipo date

df['year'] = pd.DatetimeIndex(df['Order Date']).year
df['month'] = pd.DatetimeIndex(df['Order Date']).month
df['month_year'] = pd.to_datetime(df['Order Date']).dt.to_period('M') ### creamos columna month_year para poder usarla en un group by

df['month_year']

my_df = df.groupby(df['month_year'])['Sales'].sum() ### Sacamos la suma de las ventas agrupadar por mes
#df.groupby(df.your_date_column.dt.month)['values_column'].sum()

my_df = my_df.to_frame()
my_df.plot() ### podemos ver que las ventas suben un poco con el tiempo por lo que buscaremos sacar la diferencia de un mes al anterior

def get_diff(data):
    data['sales_diff'] = data.Sales.diff()    
    data = data.dropna()      
    return data
diff_df = get_diff(my_df)

promedio = diff_df.mean(axis=0)
diff_mean = promedio[1]
print(f'La cantidad prmedio de mes a mes es de {diff_mean} dolares' )

plot_df.plot() ### Podemos ver el cambio en relación con el mes anterior

"""Modelos de Regresión"""

df_model = df[['month_year','Order Date', 'Ship Mode', 'Sub-Category','Quantity','Region','Discount','Sales','Profit']]

df_model.head()

from sklearn.preprocessing import OrdinalEncoder
classes = ['Standard Class', 'Second Class', 'First Class', 'Same Day'] ## [0,1,2,3]
orden = OrdinalEncoder(categories=[classes])
orden.fit_transform(df_model[['Ship Mode']])
df_model['Ship_Mode_'] = orden.fit_transform(df_model[['Ship Mode']])

from sklearn.preprocessing import OrdinalEncoder
regiones = ['South', 'West', 'Central', 'East'] ## [0,1,2,3]
reg = OrdinalEncoder(categories=[regiones])
reg.fit_transform(df_model[['Region']])
df_model['Region_'] = reg.fit_transform(df_model[['Region']])

get_diff(df_model) ### reusamos la funcion

df_model.dropna(inplace=True)

df_model.columns

df_model.drop(columns=['month_year','Ship Mode','Sub-Category', 'Region'], axis=1, inplace=True)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_model.drop(['Profit'], axis=1), df_model['Profit'], test_size=0.2, random_state=0)

print(X_train.head())
print(y_train.head())

df_model.corr()