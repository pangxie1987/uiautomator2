# coding=utf-8

'''
bilibili数据
'''
import requests

header3 = {'User-Agent': 'bili-universal/8230 CFNetwork/974.2.1 Darwin/18.0.0Buvid: f1ade0f34876e459d9a768614cdc3629'}


def popular():
    '热门'
    url3 = 'https://app.bilibili.com/x/v2/show/popular/index?access_key=a60b7e74dd582e3c3ed298353a9a2131&actionKey=appkey&appkey=27eb53fc9058f8c3&build=8230&device=phone&idx=0&last_param=&login_event=0&mobi_app=iphone&platform=ios&sign=ccf2c0eeccb6a54716572538d646ef7e&ts=1553339057&ver='
    t = requests.get(url=url3, headers=header3)

    contents = t.json()['data']
    for content in contents:
        if 'up_name' not in content['args']:
            print(content['item'][0]['title'])
            print(content['item'][0]['args']['up_name'])
        else:
            print(content['title'])
            print(content['args']['up_name'])
            print(content['cover_left_text_2'])
            print(content['cover_left_text_3'])
        print('='*30)


def room():
    '直播'
    url = 'https://api.live.bilibili.com/room/v2/AppIndex/getAllList?access_key=a60b7e74dd582e3c3ed298353a9a2131&actionKey=appkey&appkey=27eb53fc9058f8c3&build=8230&device=phone&mobi_app=iphone&module_id=3&platform=ios&scale=2&sign=5bfd5078ebfe3c41188dad850d5324b4'

    r = requests.get(url=url, headers=header3)
    module_list = r.json()['data']['module_list']
    for moduleinfo in module_list:
        print(moduleinfo['module_info']['title'])
        for content in moduleinfo['list']:
            print(content['roomid'])
            print(content['title'])
            print(content['uname'])
            print('='*20)

if __name__ == '__main__':
    room()