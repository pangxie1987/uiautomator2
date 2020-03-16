import requests
import time

url = 'http://a.huodong.mi.com/activity/live/submit/antiuid/0'
datas = {
	'content': '小米10梦幻之作',
	'code': 'live202002mi10',
	'channel': 'pc',
	'callback': '__jp2'
}
headers = {
	"user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36", 
	"Cookie":"xmuuid=XMGUEST-14248DE0-4E33-11EA-B018-A951C7EAE64E; XM_agreement=0; mstuid=1581579195717_7985; client_id=180100041080; masid=2110.0001; Hm_lvt_c3e3e8b3ea48955284516b186acf0f4e=1581579203,1581579278,1581579494; hd_log_code=3113969pcactivitycells_auto_fill001003%23t%3Dnormal%26act%3Dother%26page%3Dactivity%26page_id%3D13969%26bid%3D3598092.1; log_code=8acad50869b3e00b-2fb8fe17b035b8b4|http%3A%2F%2Fwww.mi.com%2Fa%2Fh%2F13969.html; lastsource=account.xiaomi.com; cUserId=S-_XBINgfLVCKgHy8QJ61xCfpHA; euid=9G9o49GmLdPvz8Nk6khCCQ%3D%3D; serviceToken=0ILTwoieVvtcOa376BghOr%2Fn76jCuAOaFKwPNE1W8BDO8qy5xo%2FHkpOiOrOwJK3AqB2rQdEujVx6OvDZgh%2FeHdzKmmpEg%2BDh2SZE%2F8QD2ZLSA8Gf0jOjR7T6bZwKcNY5SRE02qAgEPnNHJhsHn5F00cR%2BP1V3V%2FTEBsupqURdN0%3D; mUserId=iOqxJcFJpQsXWfbsKWAQX8RnlAlxKJ%2BhknCCdxYzx7o%3D; msttime=https%3A%2F%2Fwww.mi.com%2F%3Fclient_id%3D180100041080%26masid%3D2110.0001%26gsadid%3Dgad_472_jnrx4c1y%26utm_Account%3DDefault%26utm_Campaign%3D2020%25e5%25b9%25b4%25e5%2585%25a8%25e5%25b9%25b4%25e7%2599%25be%25e5%25ba%25a6%25e6%258a%2595%25e6%2594%25be%25e9%25a1%25b9%25e7%259b%25ae%26utm_Medium%3DDisplay%26utm_Channel%3D%25e7%2599%25be%25e5%25ba%25a6PC%26utm_Source%3D%25e7%2599%25be%25e5%25ba%25a6%25e5%2593%2581%25e4%25b8%2593%26utm_Term%3D%25e7%2599%25be%25e5%25ba%25a6PC; msttime1=https%3A%2F%2Fwww.mi.com%2F%3Fclient_id%3D180100041080%26masid%3D2110.0001%26gsadid%3Dgad_472_jnrx4c1y%26utm_Account%3DDefault%26utm_Campaign%3D2020%25e5%25b9%25b4%25e5%2585%25a8%25e5%25b9%25b4%25e7%2599%25be%25e5%25ba%25a6%25e6%258a%2595%25e6%2594%25be%25e9%25a1%25b9%25e7%259b%25ae%26utm_Medium%3DDisplay%26utm_Channel%3D%25e7%2599%25be%25e5%25ba%25a6PC%26utm_Source%3D%25e7%2599%25be%25e5%25ba%25a6%25e5%2593%2581%25e4%25b8%2593%26utm_Term%3D%25e7%2599%25be%25e5%25ba%25a6PC; Hm_lpvt_c3e3e8b3ea48955284516b186acf0f4e=1581579661; XM_1519529235_UN=1519529235; pageid=81190ccc4d52f577; mstz=||1427222336.46|||; xm_vistor=1581579195717_7985_1581579195717-1581579667233"
}

while 1:

	r = requests.get(url=url, params=datas, headers=headers)
	print(r.text)
	time.sleep(10)
