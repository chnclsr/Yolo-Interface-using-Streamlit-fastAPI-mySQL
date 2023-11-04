import requests, json

class HttpClient:
    def __init__(self, url = "http://127.0.0.1:8000"):
        self.base_url = url
        self.headers = {'Content-type': 'application/json',
                        'Accept': 'application/json'}

    def post_request(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, data=json.dumps(data), headers=self.headers)
        return response