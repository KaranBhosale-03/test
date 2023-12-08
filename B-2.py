#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:21:54 2023

@author: karanbhosale
"""
#B-2
import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

survival_percentages = titanic.groupby(['sex', 'class'])['survived'].mean() * 100

survival_percentages = survival_percentages.reset_index()

sns.barplot(x='class', y='survived', hue='sex', data=survival_percentages)
plt.title("Percentage of Passengers Who Survived by Sex and Class")
plt.xlabel("Class")
plt.ylabel("Survival Percentage")
plt.show()
