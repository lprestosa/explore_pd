# Explore Pandas

## Articles



### Exploratory Data Analysis
[20 Must-Know Pandas Function for Exploratory Data Analysis](https://www.analyticsvidhya.com/blog/2021/04/20-must-known-pandas-function-for-exploratory-data-analysis-eda/)


By Chirag Goyal

```python
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt

# Load titanic dataset from seaborn
# titanic = sns.load_dataset('titanic')
# titanic.to_csv('titanic.csv')

df = pd.read_csv('data/titanic.csv')

print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.ndim)
print(df.describe())
print(df.sample())
print(df.isnull().sum())
print(df.nunique())
print(df.index)
print(df.columns)
print(df.memory_usage)
# print(df.nlargest(5,'Age'))
print(df.isna().head())
print(df.dropna())
print(df.duplicated())
print(df.corr())
print(df.dtypes)
```