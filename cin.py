# coding=utf-8
import requests
import time
from bs4 import BeautifulSoup
import re

user = 'kof2001kopkpr@gmail.com'
pw = 'nmpvvg'
start_time = time.time()
login = requests.post('https://cccat.io/user/_login.php',
                      data={'email': user, 'passwd': pw, 'remember_me': 'week'})


def info():
    user_info = requests.get('https://cccat.io/user/index.php', cookies=login.cookies)
    parser = BeautifulSoup(user_info.text, 'html.parser')
    rule = re.compile('Remaining Transfer')
    transfer = str(parser.find('p', text=rule)).split()[3]
    return transfer


checkin = requests.get('https://cccat.io/user/_checkin.php', cookies=login.cookies)
results = checkin.json()
user_transfer = info()
