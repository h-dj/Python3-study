#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import random

import os
import requests
import time

' a test module '

__author__ = 'H_DJ'

'''
请求头
'''
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Host': 'view55.book118.com',
    'Referer': 'https://view55.book118.com/?readpage=9p2dtoBbU7n4Mtr1xjFVCg==&furl=o4j9ZG7fK95dS7wYrAN0MnYqzG1T0OIsJHGIUe54h13R6@kUibFpZF6ep9pLJeCfcsQ7UZaCoZz6lGeBl6LsJfLMWD49Qdv75CxyoEUqzFuNqgsRJRZV7Q==&n=1',
    'Accept': '*/*'
}
'请求参数'
params = {
    'f': 'dXAxNC0yLmJvb2sxMTguY29tLjgwXDM5NzE1NzAtNWE2ODk5NjgxNDliOC5wZGY=',
    'img': '',
    'isMobile': 'false',
    'readLimit': '9p2dtoBbU7n4Mtr1xjFVCg==',
    'sn': '0',
    'furl': 'o4j9ZG7fK95dS7wYrAN0MnYqzG1T0OIsJHGIUe54h13R6@kUibFpZF6ep9pLJeCfcsQ7UZaCoZz6lGeBl6LsJfLMWD49Qdv75CxyoEUqzFuNqgsRJRZV7Q==',
}

imgparams = {
    'img': '',
    'tp': ''
}
'''
请求url
'''
imgurl = 'https://view55.book118.com/img'

pageurl = 'https://view55.book118.com/PW/GetPage'

'''
请求时间间隔
'''
sleep_time = 15

'''
构造请求队列url
'''

# 页面队列url
print('开始下载')
for i in range(404):
    file_name = 'ch_%s.png' % str(i)
    save_file = 'E:/pdf/dsje2/' + file_name
    params_file = '../resource/params/%s.json' % str(i)
    is_file = os.path.isfile(params_file)
    if is_file:
        with open(params_file, 'r') as load_f:
            params = json.load(load_f)
    if is_file and os.path.isfile(save_file):
        print('skip')
        continue
    # 睡眠5~10秒
    time.sleep(random.randint(5, 7))
    # 请求页面
    params['sn'] = i

    resp = requests.get(pageurl, params=params, headers=headers, timeout=60)
    if resp.status_code == 200:
        result = resp.json()
        if result['NextPage'] is not None and result['NextPage'] is not '':
            imgparams['img'] = result['NextPage']
            params['img'] = result['NextPage']
            if os.path.isfile(save_file) is False:
                print('download img')
                r = requests.get(imgurl, params=imgparams, timeout=60)
                if r.status_code == 200:
                    with open(save_file, 'wb') as f:
                        f.write(r.content)
    else:
        print('page ', i, 'download error')
    print(params)
    with open(params_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(params))

print('完成下载')
