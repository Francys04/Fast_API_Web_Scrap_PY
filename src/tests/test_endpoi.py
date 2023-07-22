import requests
import pytest

"""first example of simple test
HTTP GET request to an endpoint and checks if the response status code is 200 using the requests library"""
ENDPOINT = "http://127.0.0.1:8000/"

# response = requests.get(ENDPOINT)
# print(response)

# data = response.json()
# print(data)

# status_code = response.status_code
# print(status_code)

"""pytest
call endpooint"""

"""Check status_code of endpoint get request"""
def test_call_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    
