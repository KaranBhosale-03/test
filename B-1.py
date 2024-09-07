#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:20:32 2023

@author: karanbhosale
"""
#B-1


import seaborn as sns

titanic_data = sns.load_dataset('titanic')

grouped_data = titanic_data.groupby('class')

average_age = grouped_data['age'].mean()

filtered_groups = average_age < 30

print(filtered_groups)
print()

for group_name in filtered_groups[filtered_groups].index:
    t1=titanic_data[titanic_data['class'] == group_name]
    print(t1[['age','sex','class','fare','survived']].head())
    print()

Karan

