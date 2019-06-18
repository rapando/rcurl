import pytest
import rcurl
import requests
import json

from .expected import *

def test_get():
    r = requests.get('https://google.com')
    c_type = rcurl.get_curl(r)
    c_type == expected_get

def test_blank_post():
    r = requests.post('https://google.com')
    c_type = rcurl.get_curl(r)
    assert isinstance(c_type, str)
    
def test_post_with_json():
    data = json.dumps({'c': 'd'})
    r = requests.post('https://google.com', data=data, headers={'content-type': 'application/json'})
    c_type = rcurl.get_curl(r)
    assert isinstance(c_type, str)