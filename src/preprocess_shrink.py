# purpose:
# select subset of users and movies
# subset should: users who ratd the most movies
#                and movie has be the most rating
import pickle
import numpy as numpy
import pandas as pd
from collections import Counter

df = pd.read_csv('../large_files/movielens-20m-dataset/edited_rating.csv')

N = df.userId.max() + 1
M = df.movie_idx.max() + 1

user_ids_count = Counter(df.userId)
movie_ids_count = Counter(df.movie_idx)

n = 10000
m = 2000

# var u,c in user_ids_count.most_common(n), output u
user_ids = [u for u, c in user_ids_count.most_common(n)]
# var m,c in movie_ids_count.most_common(m), output m
movie_ids = [m for m, c in movie_ids_count.most_common(m)]

#choose only small set user_ids && small set movie idx exists together

df_small = df[df.userId.isin(user_ids) & df.movie_idx.isin(movie_ids)].copy()

new_user_id_map = {}
i = 0
for old in user_ids:
    new_user_id_map[old] = i
    i += 1

new_movie_id_map = {}
j = 0
for old in movie_ids:
    new_movie_id_map[old] = j
    j += 1

df_small.loc[:, 'userId'] = df_small.apply(lambda row: new_user_id_map[row.userId], axis=1)
df_small.loc[:, 'movie_idx'] = df_small.apply(lambda row: new_movie_id_map[row.movie_idx], axis=1)
df_small.to_csv('../large_files/movielens-20m-dataset/very_small_rating.csv', index = False)