# recommender-systems-movielens-20m-dataset
recommender-systems-movielens-20m-dataset
#download data set to large_files
- https://www.kaggle.com/grouplens/movielens-20m-dataset
- save to  large_files/movielens-20m-dataset/xxx.csv

# src 

```
python preprocess.py #for refined id to index
python preprocess_shrink.py # for extract small data set
python preprocess2dict.py # csv to array and save as binary json file
python userbased.py # user user collaborative filter

```
