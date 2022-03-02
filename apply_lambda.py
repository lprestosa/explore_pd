"""
apply-and-lambda-usage-in-pandas
https://towardsdatascience.com/apply-and-lambda-usage-in-pandas-b13a1ea037f7
Rahul_Agarwal
https://www.kaggle.com/mlwhiz/apply-and-lambda-for-pandas
"""


"""
Say, If the movie is of the thriller genre, I want to add 1 to the
IMDB rating subject to the condition that IMDB rating remains less than or equal to 10. 
And If a movie is a comedy I want to subtract 1 from the rating.
"""
def custom_rating(genre, rating):
    if 'Thriller' in genre:
        return min(10, rating + 1)
    elif 'Comedy' in genre:
        return max(0, rating - 1)
    else:
        return rating

df['CustomRating'] = df.apply(lambda x: custom_rating(x['Genre'], x['Rating']), axis=1)


# Avg Rating
df['AvgRating'] = (df['Rating'] + df['Metascore'] / 10) / 2

# Single condition: dataframe with all movies rated greater than 8
df_gt_8 = df[df['Rating']>8]

# Multiple conditions: AND - dataframe with all movies rated greater than 8 and having more than 100000 votes
And_df = df[(df['Rating']>8) & (df['Votes']>100000)]

# Multiple conditions: OR - dataframe with all movies rated greater than 8 or having a metascore more than 90
Or_df = df[(df['Rating']>8) | (df['Metascore']>80)]

# Multiple conditions: NOT - dataframe with all emovies rated greater than 8 or having a metascore more than 90 have to be excluded
Not_df = df[~((df['Rating']>8) | (df['Metascore']>80))]

# filter those rows where the number of words in the movie title is greater than or equal to than 4.
new_df = df[df.apply(lambda x : len(x['Title'].split(" "))>=4,axis=1)]


# find dmovies for which the revenue is less than the average revenue for that particular year?
year_revenue_dict = df.groupby(['Year']).agg({'Rev_M': np.mean}).to_dict()['Rev_M']

def bool_provider(revenue, year):
    return revenue < year_revenue_dict[year]

new_df = df[df.apply(lambda x: bool_provider(x['Rev_M'], x['Year']), axis=1)]

df['Price'] = df.apply(lambda x: int(x['Price'].replace(',', '')),axis=1)

# apply progress bar
from tqdm import tqdm, tqdm_notebook
tqdm_notebook().pandas()
df.progress_apply(lambda x: custom_rating_function(x['Genre'],x['Rating']),axis=1)