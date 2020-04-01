'''
疫情增长趋势动态图--海外
参考：https://mp.weixin.qq.com/s?__biz=MzA5NDk4NDcwMw==&mid=2651389307&idx=2&sn=8bf8aaa4597a5336eea7c41648e3a2fd&chksm=8bba1debbccd94fd8dbb900f305fea43994d87eb87a28784d36396b38e3c95b4422e28d5b7c1&scene=126&sessionid=1585387515&key=61c257cd8ca493f98df98132aaea78ac250d81ca318e265ba4378db2ba2b7c0130cc5f705e8de9e1b9765f1510399d7f74ba6412606ee5c511539744cff4004b58db91a0a8355c933249e38b1ec94ede&ascene=1&uin=MjU1MjExMjgxNw%3D%3D&devicetype=Windows+10&version=62080079&lang=zh_CN&exportkey=AdygyIyfJk%2BGq445lx3GLQg%3D&pass_ticket=2JV9zXhMUETFb4ql5Qovi41a52QJ4Pjyx71z%2FQJYay3trikwEgsCd62NcWUqSpel
疫情数据来源：https://news.qq.com/zt2020/page/feiyan.htm?from=timeline&isappinstalled=0#/global

绘制动态图

'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

filename = '1.xls'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
df = pd.read_excel(filename, encoding='gbk', usecols=['country', 'date', 'confirm'])
fig, ax = plt.subplots(figsize=(15,18))

def sortTime(list1):
    list2 = []
    for i in list1:
        if i in list2:
            pass
        else:
            list2.append(str(i))
    return list2

def start(date):
	'绘图'
	# 找出日期对应的数据，并以confirm人数为排序依据，取出前十名，将数据反转
	# date = '2020年3月20日'
	dff = df[df['date'].eq(date)].sort_values(by='confirm', ascending=False).head(10)
	dff = dff[::-1]		# 反转数据
	ax.clear()

	# 画出横向柱状图
	colors = ['#abd0ff', '#ffb3ff', '#90d595', '#e48381', '#aafbff', '#f7bb5f', '#eafb50', '#00BFFF', '#ADD8E6',
              '#32CD32']
	ax.barh(dff['country'], dff['confirm'], color=[colors[i] for i in range(len(dff['country']))])
	dx = dff['confirm'].max()/200

	# 将确认结果放入图形中

	for i, (num, country) in enumerate(zip(dff['confirm'], dff['country'])):
		print(num, country)
		ax.text(num+dx, i, num, size=20, color='#444444')

	# 设置标题，时间戳， 坐标轴个网格线，增加图形美观
	ax.set_title('海外疫情动态变化图', fontsize=30, color='y')
	ax.text(0.83, 1.05, date, transform=ax.transAxes, color='b', size=30)		# 将时间戳放到右上角
	ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))			# 给X轴坐标数据科学计数
	ax.xaxis.set_ticks_position('top')		# 将X轴坐标放到上端
	ax.tick_params(axis='x', colors='#777777', labelsize=12)
	ax.margins(0, 0.01)		# 缩放坐标轴
	ax.grid(which='major', axis='x', linestyle='-')  # 画网格虚线

animator = animation.FuncAnimation(fig, start, frames=sortTime(df['date']), interval=500)
plt.show()
