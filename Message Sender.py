import requests
import json
url = "https://www.fast2sms.com/dev/bulk"

my_data = {
    'sender Id': 'FSTSMS',
    'message': 'This is a test message',
    'language': 'english',
    'route': 'p',
    'numbers': '9841895444'
}
headers = {
    'authorization': 'XdM5pG2AowisHkn0gCP7OVURcIx34rvFaJN8tT9ZumfKBjbLW1uofail4d3QBFORkTXKWJ0rzn9vjZUw',
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache"
}
response = requests.request("POST",
                            url,
                            data=my_data,
                            headers=headers)
returned_msg = json.loads(response.text)
print(returned_msg['message'])
