#1. load rating csv
#2. all user id - 1
#3. all movie id to index (becaus all movie id is not seq)
#4. save as edited_rating.csv
import pandas as pd

df = pd.read_csv('../large_files/movielens-20m-dataset/rating.csv');

df.userId = df.userId - 1 #let all user id subtract 1

#movie id no seq, use map to id -> index
unique_movies_ids = set(df.movieId)
movie2idx = {}
count = 0
for movie_id in unique_movies_ids: 
    movie2idx[movie_id] = count
    count += 1
print('processing csv...')
df['movie_idx'] = df.apply(lambda row: movie2idx[row.movieId], axis = 1)
df = df.drop(columns = ['timestamp'])
df.to_csv('../large_files/movielens-20m-dataset/edited_rating.csv', index = False)
