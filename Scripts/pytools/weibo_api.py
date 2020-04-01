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
app_secret = '15f0f548f1793e6a0eac105a8264ab4'
code = 'd9afe1b4e3afa6a20e70e254df4d75b2'
redirect_uri = 'https://www.sina.com.cn'

authorize_url = 'https://api.weibo.com/oauth2/authorize'
token_url = 'https://api.weibo.com/oauth2/access_token'

'''授权-目前代码无法获取，使用浏览器获取code'''
# datas = {'client_id':'1841398159', 'redirect_uri':'https://api.weibo.com/oauth2/default.html', 'response_type':'code'}
# url = 'https://api.weibo.com/oauth2/authorize?client_id=1841398159&redirect_uri=https://www.sina.com.cn&response_type=code'
# r = requests.get(url=url)
# print(r.url)
# print(r.text)

'''授权后获取access_token'''
token_ploy = {
		'client_id':app_key, 
		'client_secret':app_secret, 
		'grant_type':'authorization_code', 
		'code':code, 
		'redirect_uri':redirect_uri
		}
token_response = requests.post(url=token_url, params=token_ploy)
print(token_response.url)
print(token_response.text)