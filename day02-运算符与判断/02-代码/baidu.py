import requests
print(requests.post(url='https://fanyi.baidu.com/sug', data={'kw':input('请输入你要翻译的单词')}).json()['data'][0]['v'])