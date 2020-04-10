'''
钉钉群智能机器人推送
参考：https://v3u.cn/a_id_132
官方文档：https://ding-doc.dingtalk.com/doc#/serverapi2/qf2nxq

操作步骤：
	PC端创建钉钉群
	通过群智能助手添加钉钉机器人(webhook)
	计算签名
	发送消息
'''

import requests, json
import time
import hmac
import hashlib
import base64
import urllib.parse


headers = {'Content-Type': 'application/json'}   #定义数据类型
secret = 'SEC3b85a8c9abd4e2ca48184b86e0d6da8d2f3cff19b4a032c79850702c666821d1'		# 签名

timestamp = str(round(time.time() * 1000))
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
ham_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(ham_code))		# 签名计算
print(timestamp)
print(sign)

webhook = 'https://oapi.dingtalk.com/robot/send?access_token=e78ba828f695bc7baec9e4cf1265942ae3b69bcbbbc50e2a25c0f27818cd135e&timestamp={}&sign={}'.format(timestamp, sign)

payload = {
	"msgtype": "text",
	"text": {"content": "钉钉推送测试"},
	"isAtAll": True
}

r = requests.post(url=webhook, json=payload, headers=headers)
print(r.text)