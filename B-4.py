#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:03:56 2023

@author: karanbhosale
"""
#B-4
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("/Users/karanbhosale/Desktop/Scripting language/vgsales.csv")
df = df.dropna(subset=['Year', 'NA_Sales'])

genres = df['Genre'].unique()

plt.figure(figsize=(10, 6))

for genre in genres:
    genre_data = df[df['Genre'] == genre]
    x = genre_data['Year']
    y = genre_data['NA_Sales']

  
    plt.scatter(x, y, label=genre)

    reg_model = LinearRegression()
    reg_model.fit(x.values.reshape(-1, 1), y)

    y_pred = reg_model.predict(x.values.reshape(-1, 1))

    plt.plot(x, y_pred)

plt.title("North American Sales by Year - Scatterplot with Best-fit Lines")
plt.xlabel("Year")
plt.ylabel("North American Sales")
plt.legend()
plt.show()
