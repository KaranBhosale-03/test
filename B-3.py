#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:00:36 2023

@author: karanbhosale
"""
#B-3
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

passengers_with_age = titanic['age'].dropna()
num_passengers_with_age = len(passengers_with_age)

print("Number of passengers not missing age values:", num_passengers_with_age)
plt.figure(figsize=(8, 4))
sns.distplot(passengers_with_age, kde=False)
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

plt.figure(figsize=(8, 4))
sns.violinplot(y=passengers_with_age)
plt.title("Violin Plot of Age")
plt.ylabel("Age")
plt.show()
