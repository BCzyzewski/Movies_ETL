import requests
import pandas as pd
from create_list_of_movies import load_and_create
from send_file import uploadToBlobStorage
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get('API_KEY')
output_file = '/home/user/Pobrane/ETL/data/result.csv'


class API:
    def __init__(self, url):
        self.url = url

    def get_request(self, params_value):
        self.response = requests.get(self.url, params = params_value)

        self.data = self.response.json()

    def get_status(self):

        self.status = self.response.status_code

        return self.status    


def create_all_df(api, path):

    list_of_movies = load_and_create(path)

    df_all = pd.DataFrame()

    for index, movie in enumerate(list_of_movies):
        api.get_request(params_value = {'apikey' : api_key, 't' : movie})

        if api.get_status() != 200:
            print(api.response)
            break 

        if api.data['Response'] == 'False':
            continue

        api.data["Ratings"] = str(api.data["Ratings"])    

        df = pd.DataFrame.from_records(api.data, index = [index])

        df_all = pd.concat([df_all, df], ignore_index = True)

    return df_all        


if __name__ == "__main__":

    Movies = API('http://www.omdbapi.com/')

    files = create_all_df(Movies, '/home/user/Pobrane/ETL/data/movies.csv')

    files.to_csv(output_file)

    uploadToBlobStorage(output_file, 'movies-data.csv')