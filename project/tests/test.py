from ..my_app.connect_to_movies import API
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.environ.get('API_KEY')

def test_key():
    assert api_key != None

class TestAPI():

    def setup_method(self):
        self.test_api = API('http://www.omdbapi.com/')

    def test_get_request(self):

        self.setup_method()

        self.test_api.get_request(params_value = {'apikey' : api_key, 't' : 'Avatar'})

        assert self.test_api.get_status() == 200