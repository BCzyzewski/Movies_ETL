import pandas as pd


def load_and_create(path):
    df = pd.read_csv(path)

    list_of_movies = df['Film'].to_list()

    return list_of_movies