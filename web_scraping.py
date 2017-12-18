import requests
import re
from bs4 import BeautifulSoup

URL_BASE = "http://XX.XX.XX.XX:XXXX"
URL_START = URL_BASE + "/XXXX/XXXX"

r = requests.get(URL_START)
soup = BeautifulSoup(r.text, "lxml")

for i in range(10):
    num = soup.find(id='number').text
    action = soup.find(id='form_challenge')['action']
    post_data = dict(input = num)
    r = requests.post(URL_BASE + action, post_data)
    soup = BeautifulSoup(r.text, "lxml")
    flag = soup.find_all(string=re.compile(".*FLAG.*", re.IGNORECASE))
    if flag:
        print(flag)
        break
