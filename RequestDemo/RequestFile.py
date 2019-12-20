import requests, pprint, os, re
from requests.auth import HTTPBasicAuth

# data = {'name': 'germey', 'age': 23 }
#
# repuest = requests.get('http://httpbin.org/get', params=data)
# pprint.pprint(repuest.status_code)
# pprint.pprint(type(repuest.text))
# pprint.pprint(repuest.text)
#
# pprint.pprint(type(repuest.json()))
# pprint.pprint(repuest.json())


# headers = {'User-Agent ' :'Mozilla/5.0 (Macintosh; Intel Mac 05 X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/52.0.2743.116 Safari/537.36'}
#
# r = requests.get('https://www.zhihu.com/explore', headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r .text)
# print(titles)
# pprint.pprint(requests.codes.ok)
#
# reqs = requests.get('https://www.baidu.com')
# pprint.pprint(type(reqs.cookies))
# # pprint.pprint(reqs.cookies)
# jar = requests.codes.RequestsCookieJar()
#
# pprint.pprint(jar)
# for (key, val) in reqs.cookies.items():
#     pprint.pprint(key + '  ' + val)


# req = requests.session()
# req.get('http:/bin.org/cookies/set/number/123456789')
# p = req.get('http://httpbin.org/cookies')
# pprint.pprint(p.text)

# req = requests.get('https://www.taobao.com', proxies=False, auth=HTTPBasicAuth())
# pprint.pprint(req.status_code)
# pprint.pprint(req.text)

contentSte = 'Hello zhu 13434 gin 2324334 we will come'
matchStr = '^Hello.*?(\d+).*come$'
match = re.match(matchStr, contentSte)
pprint.pprint(match)
