import requests


class ApiClient:
    """A client for interacting with an API, providing methods to send HTTP requests
    (GET, POST, DELETE, PUT) and manage session data."""

    def __init__(self):
        self.session = requests.session()
        self.api_url = "https://petstore.swagger.io/v2"
        self.response = None
        self.json_headers = {"Content-Type": "application/json"}
        self.formdata_headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def get(self, url, endpoint, body=None, params=None, headers=None):
        self.response = self.session.get(
            url=url + endpoint,
            data=body,
            params=params,
            headers=self.json_headers if not headers else headers,
        )

    def post(self, url, endpoint, body=None, params=None, headers=None):
        self.response = self.session.post(
            url=url + endpoint,
            data=body,
            params=params,
            headers=self.json_headers if not headers else headers,
        )

    def delete(self, url, endpoint, body=None, params=None):
        self.response = self.session.delete(
            url=url + endpoint, data=body, params=params, headers=self.json_headers
        )

    def put(self, url, endpoint, body=None, params=None):
        self.response = self.session.put(
            url=url + endpoint, data=body, params=params, headers=self.json_headers
        )

    def clean_session_cookies(self):
        self.session.cookies.clear()
        self.json_headers = {"Content-Type": "application/json"}
