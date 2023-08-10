# Origami dataset generator for a fictional origami store
# Quick way to generate large example datasets for demos

# import libraries
import pandas as pd
import numpy as np
import datetime

# Define the dataset parameters
dates = pd.date_range(start="2015-01-01", end="2019-12-31")
countries = ['Canada', 'United Kingdom', 'United States', 'France', 'Germany', 'Italy', 'Japan', 'China', 'India']
cost_data = [['Origami Crane', 7.0, 4.0], 
             ['Origami Flower', 9.0, 5.5], 
             ['Origami Boat', 6.0, 4.0],
             ['Origami Dragon', 10.25, 9.75],
             ['Origami Penguin', 8.5, 3.5]]
products = [item[0] for item in cost_data]
df_columns = ['Date', 'Country', 'Product']
cost_columns = ['Product', 'Revenue per unit', 'Cost per unit']
np.random.seed(42)

# Construct the dataframe
permutations = [[i, j, k] for i in dates for j in countries for k in products]
df = pd.DataFrame(data=permutations, columns=df_columns)
units_sold = np.random.lognormal(1, 2, len(df))
df['Units sold'] = [round(x) for x in units_sold]
cost_df = pd.DataFrame(data=cost_data, columns=cost_columns)
df = pd.merge(df, cost_df)
df['Profit'] = (df['Revenue per unit'] - df['Cost per unit']) * df['Units sold']
df['Day'] = df.Date.dt.day
df['Month'] = df.Date.dt.month
df['Month name'] = df.Date.dt.month_name()
df['Year'] = df.Date.dt.year

# output the dataset as a csv
df.to_csv('origami-dataset.csv', index=False)