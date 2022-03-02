# SQL
#SELECT * FROM table_df
# Pandas
table_df

# SQL
#SELECT column_a, column_b FROM table_df
# Pandas
table_df[['column_a', 'column_b']]

# SQL
# SELECT DISTINCT column_a FROM table_df
# Pandas
table_df['column_a'].drop_duplicates()

# SQL
# SELECT column_a as Apple, column_b as Banana FROM table_df
# Pandas
table_df[['column_a', 'column_b']].rename(columns={'column_a':
'Apple', 'column_b':'Banana'})

# SQL
# SELECT CASE WHEN column_a > 30 THEN "Large"
#            WHEN column_a <= 30 THEN "Small"
#            END AS Size
# FROM table_df
# Pandas
conditions = [table_df['column_a']>30, table_df['column_b']<=30]
choices = ['Large', 'Small']
table_df['Size'] = np.select(conditions, choices)


# SQL
#SELECT * FROM table_1 t1
#         LEFT JOIN table_2 t1 on t1.lkey = t2.rkey
# Pandas
table_1.merge(table_2, left_on='lkey', right_on='rkey', how='left')


# SQL
SELECT * FROM table_1
UNION ALL
SELECT * FROM table_2
# Pandas
final_table = pd.concat([table_1, table_2])


# SQL
SELECT * FROM table_df WHERE column_a = 1
# Pandas
table_df[table_df['column_a'] == 1]


# SQL
SELECT * FROM table_df WHERE column_a = 1 AND column_b = 2
# Pandas
table_df[(table_df['column_a']==1) & (table_df['column_b']==2)]


# SQL
SELECT * FROM table_df WHERE column_a LIKE '%ball%'
# Pandas
table_df[table_df['column_a'].str.contains('ball')]


# SQL
SELECT * FROM table_df WHERE column_a IN('Canada', 'USA')
# Pandas
table_df[table_df['column_a'].isin(['Canada', 'USA'])]


# SQL
SELECT * FROM table_df ORDER BY column_a DESC
# Pandas
table_df.sort_values('column_a', ascending=False)


# SQL
SELECT column_a, COUNT DISTINCT(ID)
FROM table_df
GROUP BY column_a
# Pandas
table_df.groupby('column_a')['ID'].nunique()


# SQL
SELECT column_a, AVG(revenue)
FROM table_df
GROUP BY column_a
# Pandas
table_df.groupby('column_a')['revenue'].mean()
