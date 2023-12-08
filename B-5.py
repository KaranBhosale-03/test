#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 16:03:42 2023

@author: karanbhosale
"""
#B-5
import pandas as pd
import matplotlib.pyplot as plt


FILELOCATION = '/Users/karanbhosale/Desktop/Scripting language/vgsales.csv'

df = pd.read_csv(FILELOCATION )

publishers = ['Nintendo', 'Sony Computer Entertainment', 'Microsoft Game Studios']
filtered_df = df[df['Publisher'].isin(publishers)]

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(filtered_df[filtered_df['Publisher'] == 'Nintendo']['NA_Sales'], bins=20, alpha=0.5, color='red')
axes[0, 0].set_title('Nintendo - NA Sales')
axes[0, 0].set_xlabel('NA Sales')
axes[0, 0].set_ylabel('Frequency')

axes[0, 1].hist(filtered_df[filtered_df['Publisher'] == 'Nintendo']['EU_Sales'], bins=20, alpha=0.5, color='green')
axes[0, 1].set_title('Nintendo - EU Sales')
axes[0, 1].set_xlabel('EU Sales')
axes[0, 1].set_ylabel('Frequency')

axes[1, 0].hist(filtered_df[filtered_df['Publisher'] == 'Nintendo']['JP_Sales'], bins=20, alpha=0.5, color='blue')
axes[1, 0].set_title('Nintendo - JP Sales')
axes[1, 0].set_xlabel('JP Sales')
axes[1, 0].set_ylabel('Frequency')

axes[1, 1].hist(filtered_df[filtered_df['Publisher'] == 'Nintendo']['Global_Sales'], bins=20, alpha=0.5, color='purple')
axes[1, 1].set_title('Nintendo - Global Sales')
axes[1, 1].set_xlabel('Global Sales')
axes[1, 1].set_ylabel('Frequency')

plt.tight_layout()

plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(filtered_df[filtered_df['Publisher'] == 'Sony Computer Entertainment']['NA_Sales'], bins=20, alpha=0.5, color='red')
axes[0, 0].set_title('Sony Computer Entertainment - NA Sales')
axes[0, 0].set_xlabel('NA Sales')
axes[0, 0].set_ylabel('Frequency')

axes[0, 1].hist(filtered_df[filtered_df['Publisher'] == 'Sony Computer Entertainment']['EU_Sales'], bins=20, alpha=0.5, color='green')
axes[0, 1].set_title('Sony Computer Entertainment - EU Sales')
axes[0, 1].set_xlabel('EU Sales')
axes[0, 1].set_ylabel('Frequency')

axes[1, 0].hist(filtered_df[filtered_df['Publisher'] == 'Sony Computer Entertainment']['JP_Sales'], bins=20, alpha=0.5, color='blue')
axes[1, 0].set_title('Sony Computer Entertainment - JP Sales')
axes[1, 0].set_xlabel('JP Sales')
axes[1, 0].set_ylabel('Frequency')

axes[1, 1].hist(filtered_df[filtered_df['Publisher'] == 'Sony Computer Entertainment']['Global_Sales'], bins=20, alpha=0.5, color='purple')
axes[1, 1].set_title('Sony Computer Entertainment - Global Sales')
axes[1, 1].set_xlabel('Global Sales')
axes[1, 1].set_ylabel('Frequency')

plt.tight_layout()

plt.show()


fig, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].hist(filtered_df[filtered_df['Publisher'] == 'Microsoft Game Studios']['NA_Sales'], bins=20, alpha=0.5, color='red')
axes[0, 0].set_title('Microsoft Game Studios - NA Sales')
axes[0, 0].set_xlabel('NA Sales')
axes[0, 0].set_ylabel('Frequency')

axes[0, 1].hist(filtered_df[filtered_df['Publisher'] == 'Microsoft Game Studios']['EU_Sales'], bins=20, alpha=0.5, color='green')
axes[0, 1].set_title('Microsoft Game Studios - EU Sales')
axes[0, 1].set_xlabel('EU Sales')
axes[0, 1].set_ylabel('Frequency')

axes[1, 0].hist(filtered_df[filtered_df['Publisher'] == 'Microsoft Game Studios']['JP_Sales'], bins=20, alpha=0.5, color='blue')
axes[1, 0].set_title('Microsoft Game Studios - JP Sales')
axes[1, 0].set_xlabel('JP Sales')
axes[1, 0].set_ylabel('Frequency')

axes[1, 1].hist(filtered_df[filtered_df['Publisher'] == 'Microsoft Game Studios']['Global_Sales'], bins=20, alpha=0.5, color='purple')
axes[1, 1].set_title('Microsoft Game Studios - Global Sales')
axes[1, 1].set_xlabel('Global Sales')
axes[1, 1].set_ylabel('Frequency')

plt.tight_layout()

plt.show()





















