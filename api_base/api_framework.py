"""
This contains utility functions to make api calls from https://api.unsplash.com/
"""
import requests
from requests.exceptions import HTTPError

#TODO: use requests module to call apis

class APIFramework:
    '''contains all necessary methods to make url requests'''

    def __init__(self):
        '''initializer method'''
        pass

    def make_get_request(self, url, params=None):
        '''makes single GET request for the given url'''
        try:
            response = requests.get(url,params = params)
            response.raise_for_status()

        except HTTPError as http_err:
            print(f'HTTP error occured: {http_err}')
        except Exception as err:
            print(f'Other error occured: {err}')
        
        else:
            if response.status_code == 200:
                print("status:" + str(response.status_code))
                return response
            else:
                print("Request Status NOT 200 but: " + str(response.status_code))
            

    def make_post_request(self, url, data_dict):
        '''makes single POST request for the given url'''
        pass
    
    def get_latest_image(self):
        '''should get the latest image on triggered'''
        pass

if __name__ == "__main__":
    obj_api_framework = APIFramework()
    params = {
        'q': 'requests+language:python'
    }
    response = obj_api_framework.make_get_request('https://api.github.com/search/repositories', params)
    json_response = response.json()
    print(json_response)
    repository = json_response['items'][0]
    print(f'Repository name: {repository["name"]}')
    print(f'Repository Description: {repository["description"]}')

