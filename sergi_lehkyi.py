import pandas as pd


# Global Variables
DATAPATH = 'C:\\py\\data\\algostan\\'
FILENAME = 'data/example.csv'

def main():
    print('Translating SQL to Pandas')
    print('https://medium.com/towards-data-science/translating-sql-to-pandas-8f4ae0268899')
    df = read_csv_file()
    sql_pd(df)


def read_csv_file():
    col_header = ['col1', 'col2']
    df = pd.read_csv(FILENAME, header = None, names = col_header )
    # print(df.describe())
    print(df.info())
    # print(df[['col1','col2']])
    return df


def sql_pd(df):

    # select * from tb1
    print(df.head())

    # select col1, col2 from tb1
    print(df[['col1', 'col2']])

    # select col1 col2 from tb1 where col1 = 'israel'
    print(df[['col1', 'col2']].loc[df['col1'] == 'israel'])
    # select col1 col2 from tb1 where col2 = 2
    print(df[['col1', 'col2']].loc[df['col2'] > 1 ] &  df[['col1', 'col2']].loc[df['col2'] < 25])

    # select * from tb1 where col1 > 1 AND col2 < 25
    print(df.loc[(df['col2'] > 1) & (df['col2']) < 5 ])

"""
    # select * from tb1 where col1 between 1 and 5 and col2 in(20,30,40,50) and col3 like '%arcelona%'
    df.loc[(df['col1'].between(1, 5)) & (df['col2'].isin([20, 30, 40, 50])) & (df['col3'].str.contains('arcelona'))]

    # select t1.col1 , t2.col2 from tb1 t1 inner join tb2 t2 on t1.column_id = t2.column_id
    df_joined = df1.join(df2, on='column_id', how='inner')
    df_joined.loc[['column1_df1', 'column1_df2']]

    # joins can be how=[inner | left | right | full]

    # select col1, count(*) from tb1 group by col1
    df.groupby('col1')['col1'].count()

    # SELECT store, sum(sales) FROM table1 GROUP BY store HAVING sum(sales) > 1000
    df_grouped = df.groupby('store')['sales'].sum()
    df_grouped.loc[df_grouped > 1000]

    # SELECT * FROM table1 ORDER BY column1 DESC
    df.sort_values(by=['column1'], ascending=False)
"""

if __name__ == '__main__':
   main()