def get_curl(request):
    try:
        headers_str = process_headers(request)
        data = get_json_data(request)

        return f"curl {request.url} {headers_str} {data}"
    except:
        raise Exception("Requires a requests object")
        return False

def process_headers(request):
    headers = request.request.headers
    headers_str = ""
    for key, value in headers.items():
        headers_str += f" -H \"{key}:{value}\" "
    return headers_str

def get_json_data(request):
    data = request.request.body
    if data:
        return f" -d '{data}'"
    else:
        return ""

def generate_curl_str():
    command = "curl "