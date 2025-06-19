import requests 
from apikey import API_TOKEN

data = {"q" : "Osh", "appid": API_TOKEN, "units": "metric"}

headers =  {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Priority": "u=1, i",
    "Referer": "https://httpbin.org/",
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-68517389-1656517e2f1090a42480db8c"
  }


variable = requests.Session()
aaa = variable.get("https://httpbin.org/form/post")

response = variable.get("https://httpbin.org/post, headers = headers, data=data, allow_redirections = True")
# print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)
# print(response.json())
