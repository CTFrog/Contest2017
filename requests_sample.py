# pip install requests

import requests

# GET
# 支店内CTF問題一覧
r = requests.get('http://10.132.83.231/ctf/question')
print(r.text)
print(r.status_code)
print(r.headers)
print(r.encoding)

# POST
# 支店内CTF第一問目
r = requests.post('http://10.132.83.231/ctf/question/1',
                   params={'flag': 'sasakama@matsushima'},
                   allow_redirects=False)
print(r.status_code) # 302
print(r.headers)     # 'Location': 'http://10.132.83.231/ctf/question/1/good'
print(r.cookies)

# Set Cookie
"""
cookie = {'JSESSIONID': '17ab96bd8ffbe8ca58a78657a918558'}
r = requests.post('http://XXX/XXX', cookies=cookie)
"""

# Session
"""
login_url = 'http://xxx/login'
want_to_acess_url =  'http://xxx/want'
payload = {
    'userid': 'my_id',
    'password': 'my_pass'
}
s = requests.Session()
p = s.post(login_url, data=payload)
r = s.get(want_to_access_url)
"""



