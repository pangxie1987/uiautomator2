'''
微博开发平台接入
开发平台地址：https://open.weibo.com/apps/1841398159/info/basic
授权：https://blog.csdn.net/weixin_34120274/article/details/94087982?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
参考：https://mp.weixin.qq.com/s?__biz=MzU2ODYzNTkwMg==&mid=2247486419&idx=1&sn=a196290d3f0126a71d06fdb8730e1e73&chksm=fc8bb342cbfc3a540b2d101749e634197cb43530f410e8b0ab7b632ea2912e879c9080e824a0&scene=126&sessionid=1585304678#rd
https://www.cnblogs.com/reblue520/p/11188752.html
https://www.cnblogs.com/codestack123/p/10816013.html
'''

import requests


app_key = '1841398159'
app_secret = '9ff061953885bcc57b948c57e9cbab35'
code = 'd9afe1b4e3afa6a20e70e254df4d75b2'
redirect_uri = 'https://www.sina.com.cn'
# redirect_uri = 'http://api.weibo.com/oauth2/default.html'

authorize_url = 'https://api.weibo.com/oauth2/authorize'
token_url = 'https://api.weibo.com/oauth2/access_token'

def get_ticket():

	'''授权-目前代码无法获取，使用浏览器获取code'''
	url1 = 'https://api.weibo.com/oauth2/authorize?client_id={client_id}&redirect_uri={redirect_url}'.format(client_id = app_key,redirect_url = redirect_uri)
	r = requests.get(url=url1)
	print(r.url)
	print(r.text)

def get_token():
	'''授权后获取access_token'''
	token_ploy = {
			'client_id':app_key, 
			'client_secret':app_secret, 
			'grant_type':'authorization_code', 
			'code':code, 
			'redirect_uri':redirect_uri
			}

	url2 = "https://api.weibo.com/oauth2/access_token?client_id={client_id}&client_secret={client_secret}&grant_type=authorization_code&redirect_uri={redirect_url}&code={code}".format(client_id = app_key,client_secret = app_secret,redirect_url = redirect_uri,code = code)
	token_response = requests.post(url=url2)
	print(token_response.url)
	print(token_response.text)

if __name__ == '__main__':
	# get_ticket()
	get_token()