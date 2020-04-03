'''
微博开发平台-网站接入
开发平台地址：https://open.weibo.com/apps/1841398159/info/basic
网站接入官方文档：https://open.weibo.com/wiki/%E7%BD%91%E7%AB%99%E6%8E%A5%E5%85%A5%E4%BB%8B%E7%BB%8D
微博API：https://open.weibo.com/wiki/%E5%BE%AE%E5%8D%9AAPI
参考：
https://www.cnblogs.com/reblue520/p/11188752.html
https://www.cnblogs.com/codestack123/p/10816013.html
https://www.cnblogs.com/lfri/p/12208789.html
'''
import json
import requests

'''pangxie1987'''
# app_key = '1841398159'
# app_secret = '9ff061953885bcc57b948c57e9cbab35'
# code = 'd9afe1b4e3afa6a20e70e254df4d75b2'
# redirect_uri = 'https://www.sina.com.cn'

'''pangxie_web'''
app_key = '3839876533'
app_secret = 'd21dff94846a51f5aa62b0018ccecb96'
code = 'f016933f9986d02580663de0afd74274'
redirect_uri = 'http://www.dygang.com'


authorize_url = 'https://api.weibo.com/oauth2/authorize'
token_url = 'https://api.weibo.com/oauth2/access_token'

def get_ticket():
	'''引导用户授权-用户浏览器中授权后，会在redirect_uri中回调code'''
	authorize_url = "https://api.weibo.com/oauth2/authorize?client_id=3839876533&redirect_uri=http://www.dygang.com"
	url1 = 'https://api.weibo.com/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_url}'.format(client_id = app_key,redirect_url = redirect_uri)
	r = requests.get(url=url1)
	print(r.url)
	print(r.text)

def get_token():
	'''根据授权后的code获取access_token'''
	url2 = "https://api.weibo.com/oauth2/access_token?client_id={client_id}&client_secret={client_secret}&grant_type=authorization_code&redirect_uri={redirect_url}&code={code}".format(client_id = app_key,client_secret = app_secret,redirect_url = redirect_uri,code = code)
	r = requests.post(url=url2)
	print(r.url)
	print(r.text)
	access_token = r.json()['access_token']
	print(access_token)
	return access_token

def share(access_token):
	'第三方分享一条连接到微博-发送微博'
	'''
	access_token: 授权信息
	status:  分享内容（必须添加应用基本信息中的 安全域名）
	'''
	share_url = "https://api.weibo.com/2/statuses/share.json"
	ployd = {'access_token':access_token, 'status':'微博发送测试：http://www.dygangs.com'}
	r = requests.post(url=share_url, data=ployd)
	print(r.text)

if __name__ == '__main__':
	# get_ticket()
	# get_token()
	share('2.001FjejFTSjrLE9d1ba955fbWio98C')