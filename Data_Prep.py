import pandas as pd

anime = pd.read_csv('archive/anime.csv')
cols = list(anime.columns.values)
anime_df = anime[cols[0:3] + cols[5:6]]

rating_df = pd.read_csv('archive/rating.csv')

df = pd.merge(anime_df, rating_df)

# df.tail(20)

user_ratings = df.pivot_table(index=['user_id'], columns=['name'], values='rating')
user_ratings.head(10)
corr_matrix = user_ratings.corr()
