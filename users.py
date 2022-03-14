from urllib import response
import requests
import os


class Users:
    def __init__(self, url=None, access_token=None, headers=None):
        self.url = 'https://gorest.co.in/public/v2/users'
        self.access_token = os.environ.get('GOREST_ACCESS_TOKEN', '')
        if url:
            self.url = url
        if access_token:
            self.access_token = access_token
        self.headers = {'Authorization': f'Bearer {self.access_token}'}
        if headers:
            self.headers = headers

        
    def create_user(self, user_data):
        url = f'{self.url}'
        print(self.headers)
        response = requests.post(url, data=user_data, headers=self.headers)
        api_output = response.json()
        return response.status_code, api_output


    def get_users(self, user_id=None):
        url = f'{self.url}/{user_id}' if user_id else self.url
        response = requests.get(url, headers=self.headers)
        api_output = response.json()
        return response.status_code, api_output


    def update_user(self, user_id, user_data):
        url = f'{self.url}/{user_id}' if user_id else self.url
        response = requests.patch(url, data=user_data, headers=self.headers)
        return response.status_code


    def delete_user(self, user_id):
        url = f'{self.url}/{user_id}'
        try:
            response = requests.delete(url, headers=self.headers)
        except:
            print('there\'s exception')
        return response.status_code
