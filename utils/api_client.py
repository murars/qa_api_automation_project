import requests


class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    
    def __init__(self):
        self.header = {
            "Content-Type":"application/json"  # gercek projelerde 8 , 9 heder imiz oluyor.Min 3 or 4 headers olur.
        }
        
    def get(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.get(url=url, headers = self.header)
        return response
    
    def post(self, endpoint,data):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.post(url=url, headers = self.header, json = data)
        return response
    
    def put(self, endpoint,data):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.put(url=url, headers = self.header, json = data)
        return response
    
    def delete(self, endpoint):
        url = f'{self.BASE_URL}/{endpoint}'
        response = requests.delete(url=url, headers = self.header)
        return response