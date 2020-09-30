import os
import pytest
import requests
import urllib.parse #urllib.parse.quote(payload)

@pytest.mark.parametrize(
    'expected', [
    ("You've reached the test endpoint from wordcount"),
])
def test_endpoint(host, expected):
    endpoint = os.path.join(host, 'test')
    response = requests.get(endpoint)
    assert response.status_code ==200
    json = response.json()
    assert 'msg' in json
    assert json['msg'] == expected