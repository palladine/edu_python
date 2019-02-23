import requests

# GET
response = requests.get('https://httpbin.org/get')
print(response.text)
print(response.json())
print(response.headers)
print(response.status_code)


# POST
# response_post = requests.post(url, json=data_utf8, headers=headers_utf8)
response_post = requests.post('https://httpbin.org/post')
print(response_post.json())
print(response_post.json()['url'])
print(response_post.headers)
print(response_post.status_code)
