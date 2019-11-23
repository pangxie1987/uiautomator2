'''
查询所有专业id（分页查询）
'''

import requests

url = 'https://api.eol.cn/gkcx/api/'
headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"
          }

datas = {

    "access_token": "",
    "keyword": "",
    "level1": "",
    "level2": "",
    "page": 1,
    "size": 99999999,
    "uri": "apidata/api/gk/special/lists"
}

spicallist = [] # 专业id列表
for i in range(1, 67):  # 共66页
    datas['page'] = i
    r = requests.get(url=url, params=datas, headers=headers)
    spicalitem = r.json()['data']['item']
    for spical in spicalitem:
        print('专业类别：%s'%spical['level3_name'])
        print('专业名称：%s'%spical['name'])
        print('专业编号：%s'%spical['special_id'])
        spicallist.append(spical['special_id'])
        print('='*20)
print(spicallist)