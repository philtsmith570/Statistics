# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 08:53:52 2018

@author: philt
"""

import numpy as np
import pandas as pd
from scipy import stats 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('state.csv')

print("State head:\n", df.head())
print("\nState describe:\n", df.describe())
print("\nPopulation Trim Mean (0.1): ", stats.trim_mean(df['Population'], 0.1))
print("Population Median: ", df['Population'].median())
print("Weighted Average: ",  np.average(df['Murder.Rate'], weights=df['Population']))
print("Mean Absolute Deviation (MAD): ", df['Population'].mad())
print("Mean Absolute Deviation (MAD): ", df['Population'].mad())
print("Murder Rate Percentile: ", np.percentile(df['Murder.Rate'], [5, 25, 75, 95]))

# States with largest murder rates 
df_hi_murder_rate = df.nlargest(5, columns=['Murder.Rate'])
print('States with largest Murder Rate: \n', df_hi_murder_rate  )

# Population Max
print(df['Population'].max())

# List version of 5 largest murder rates
States_Hi_MR = list(df_hi_murder_rate['State'])
print('States with largest murder rate: ', States_Hi_MR)


# Plots

# SNS Box Plot - Population
plot_dims = (10, 8)
fig, ax = plt.subplots(figsize=plot_dims)       
sns.boxplot(ax=ax, 
            y='Population',
            width=0.3,
            data=df_hi_murder_rate,)
plt.show()

# SNS Box Plot - Murder Rate
figMR, axMR = plt.subplots(figsize=plot_dims)
sns.boxplot(ax=axMR, 
            y='Murder.Rate',
            width=0.3,
            data=df_hi_murder_rate,)
plt.show()

# SNS Violin Plot - Population
fig1, ax1 = plt.subplots(figsize=plot_dims)
sns.violinplot(ax=ax1, y='Population', 
               data=df_hi_murder_rate,
               inner=None,)
plt.show()

# SNS Scatter Plot - Murder Rate Vs. Population
fig1, ax1 = plt.subplots(figsize=plot_dims)
sns.scatterplot(ax=ax1, 
                x='Murder.Rate',
                y='Population',
                data=df,)
plt.show()

# SNS Pair Plot - Murder Rate Vs. Population
sns.pairplot(data=df.loc[:, ['Murder.Rate', 'Population']],
             height=4)
plt.show()

# KDE Plot - Population Vs. Murder.Rate
fig1, ax1 = plt.subplots(figsize=plot_dims)
sns.kdeplot(df_hi_murder_rate['Population'], 
            df_hi_murder_rate['Murder.Rate'],
            cbar=True,
            shade=True,)
plt.show()

# Univariate Distribution - Population
fig1, ax1 = plt.subplots(figsize=plot_dims)
sns.distplot(df['Population'],)
plt.show()

# Univariate Distribution - Murder.Rate
fig1, ax1 = plt.subplots(figsize=plot_dims)
sns.distplot(df['Murder.Rate'],)
plt.show()

# Box Plot matplotlib - Population 
#fig1, ax1 = plt.subplots(figsize=plot_dims)
fig = plt.figure(figsize=plot_dims)
fig.suptitle('Polulation of States', fontsize=14, fontweight='bold')

ax = fig.add_subplot(111)
ax.boxplot(df['Population'])

ax.set_title('Box Plot Population')
ax.set_xlabel('All States')
ax.set_ylabel('Population (in millions)')

plt.show()