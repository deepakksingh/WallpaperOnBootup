"""

This contains utility functions to make api calls from https://api.unsplash.com/

"""
import requests

#TODO: use requests module to call apis

class APIFramework:
    '''contains all necessary methods to make url requests'''

    def __init__(self):
        '''initializer method'''
        pass

    def make_get_request(self, url):
        '''makes single GET request for the given url'''
        resp = requests.get(url)
        return resp.text

    def make_post_request(self, url, data_dict):
        '''makes single POST request for the given url'''
        pass
    
    def get_latest_image(self):
        '''should get the latest image on triggered'''
        pass

if __name__ == "__main__":
    obj_api_framework = APIFramework()
    res = obj_api_framework.make_get_request('https://www.google.com/')
    print(res)

