import os
import pytest
import requests #requests.models.Response
import urllib.parse


@pytest.mark.parametrize(
    'payload,expected', [
        ("Mark", "Hello Mark!"),
        ("123", "Hello 123!"),
        ("?@#", "Hello ?@#!"),
        ("   ", "Hello    !"),
])
def test_basic_route(host, payload, expected):
    endpoint = os.path.join(host, urllib.parse.quote(payload))
    response = requests.get(endpoint)
    assert response.status_code == 200
    data = response.text
    assert data == expected
