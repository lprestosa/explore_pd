"""
20 Must-Know Pandas Function for Exploratory Data Analysis
https://www.analyticsvidhya.com/blog/2021/04/20-must-known-pandas-function-for-exploratory-data-analysis-eda/
chirag_goyal
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as plt
import os


def main():
    ##OK  get_titanic_csv()

    df = pd.read_csv('data/titanic.csv')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nhead()\n', df.head())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\ntail()\n', df.tail())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\ninfo()\n', df.info())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nshape()\n', df.shape)
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nndim\n', df.ndim)
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\ndescribe()\n', df.describe())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nsample()\n', df.sample())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nisnull().sum()\n', df.isnull().sum())
    os.system('cls' if os.name == 'nt' else 'clear')
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\nnunique().sum()\n', df.nunique())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\ncolumns\n", df.columns)
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nindex\n",df.index)
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nmemory_usage\n",df.memory_usage)
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nisna().head()\n", df.isna().head())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\ndropna()\n",df.dropna())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nduplicated()\n",df.duplicated())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\ncorr()\n",df.corr())
    input("Press Enter to continue...")
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\ndtypes\n",df.dtypes)
    input("Press Enter to continue...")

    exit()

    # print(df.nlargest(5,'Age'))

def get_titanic_csv():
    # Load titanic dataset from seaborn
    titanic = sns.load_dataset('titanic')
    titanic.to_csv('titanic.csv')



if __name__ == '__main__':
   main()
