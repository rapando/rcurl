#rcurl

A simple package of generating curl statements from requests.

For now the supported methods are limited. Checl the samples in `usage`

## Installation
```bash
pip install rcurl
```

## Usage
```py
import json

import requests

from rcurl import get_curl

req_one = requests.get("https://google.com")
curl_command_one = get_curl(req_one)

req_two = requests.post("https://google.com")
curl_command_two = get_curl(req_two)

data = json.dumps({'a': 'b', 'x': 45})
headers = {
    'content-type': 'application/json',
    'authorization': 'Bearer dhsfdJGHGDH'
}
req_three = requests.post("https://google.com", data=data, headers=headers)
curl_command_three = get_curl(req_three)

print (curl_command_one)
print (curl_command_two)
print (curl_command_three)
```