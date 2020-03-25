'''
streamlit是一个用于构建机器学习、数据可视化的python框架。如果你想快速部署自己的机
器学习应用，或者给小伙伴直观展示你的数据，但是没有web开发的经验，streamlit绝对是你
的不二选择。只要你会使用python，你会发现利用streamlit开发一个web app是一件及其简
单的事情
https://zhuanlan.zhihu.com/p/110816628?from_voters_page=true
安装： pip install streamlit
启动
streamlit run app_name.py
'''

import streamlit as st
import pandas as pd
import numpy as np

# 表格控件
st.title('streamlit test')
st.write(pd.DataFrame({
	'first column': [1,2,3,4],
	'second colum': [10,20,30,40]
	}))


# 图表控件
chart_data = pd.DataFrame(
	np.random.randn(20, 3),
	columns=['a','b','c'])

st.line_chart(chart_data)

# 数据控件
st.json({
	"name": "test",
	"age": 30,
	"relations":{
		"aaa": 11,
		"bbb": 22,
		"ccc": 33
		},
	"phone":[1,2,3,4]
})