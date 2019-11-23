# -*- coding:utf-8 -*-
'''
folium是js上著名的地理信息可视化库leaflet.js为Python提供的接口，通过它，
我们可以通过在Python端编写代码操纵数据，来调用leaflet的相关功能，
基于内建的osm或自行获取的osm资源和地图原件进行地理信息内容的可视化，
以及制作优美的可交互地图。其语法格式类似ggplot2，
是通过不断添加图层元素来定义一个Map对象，最后以几种方式将Map对象展现出来。

https://python-visualization.github.io/folium/quickstart.html#Getting-Started
https://www.cnblogs.com/feffery/p/9282808.html
'''

import os
import folium
filepath = os.path.join(os.path.dirname(__file__), 'filium_map.html')
m = folium.Map(location=[29.488869,106.571034],
            tiles='Stamen Terrain',
              zoom_start=14)
m.save(filepath)

# import folium
# import os

# '''创建Map对象'''
# m = folium.Map(location=[29.488869,106.571034],
#               zoom_start=14)

# '''查看m的类型'''
# print(m.__class__)