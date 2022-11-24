import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
# % matplotlib inline
# Read csv file as a dataframe called df
df = pd.read_csv('911.csv')
# Check info and head of df
df.info()
df.head(3)

# Top 5 zip codes and townships for 911 calls 
df['zip'].value_counts().head(5)
df['twp'].value_counts().head(5)

# How many unique Title codes 
df['title'].nunique()

# Create a new feature "Reason"
df['Reason'] = df['title'].apply(lambda title: title.split(':')[0])
# Most common reason for 911 calls
df['Reason'].value_counts()

# Use seaborn to create a countplot of 911 calls by "Reason"
sns.countplot(x='Reason', data=df, palette='viridis')

