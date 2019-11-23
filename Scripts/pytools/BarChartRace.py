'''
超火动态排序图
https://zhuanlan.zhihu.com/p/82710274?utm_source=wechat_session&utm_medium=social&utm_oi=563854400989364224
'''

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML

df = pd.read_csv('citydata.csv', usecols=['name', 'group', 'year', 'value'])
(df.head(5))

colors = dict(zip(
    ['India', 'Middle East', 'Asia'],
    ['#adb0ff', '#ffb3ff', '#90d595']
))
group_lk = df.set_index('name')['group'].to_dict()

# current_year = 2018
# dff = (df[df['year'].eq(current_year)].sort_values(by='value', ascending=True).head(10))
# print(dff)

# fig, ax = plt.subplots(figsize=(15, 8))
# dff = dff[::-1]
# ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])

# for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
#     ax.text(value, i,       name,               ha='right')
#     ax.text(value, i-.25,   group_lk[name],     ha='right')
#     ax.text(value, i,       value,              ha='left')

# ax.text(1, 0.4, current_year, transform=ax.transAxes, size=46, ha='right')

# plt.show()

fig, ax = plt.subplots(figsize=(15, 8))
def draw_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], dff['value'], color=[colors[group_lk[x]] for x in dff['name']])
    dx = dff['value'].max()/200
    for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
        ax.text(value-dx, i,       name,            size=14,    weight=600,      ha='right', va='bottom')
        ax.text(value-dx, i-.25,   group_lk[name],  size=10,    color='#444444', ha='right', va='baseline')
        ax.text(value+dx, i,       f'{value:,.0f}', size=14,                     ha='left',  va='center')

    ax.text(1, 0.4, year, transform=ax.transAxes, color='#777777', size=46, ha='right', weight=800)
    ax.text(1, 1.06, 'Population(thousands)', transform=ax.transAxes, size=16, color='#777777')
    ax.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(axis='x', colors='#777777', labelsize=12)
    ax.set_yticks([])
    ax.margins(0, 0.01)
    ax.grid(which='major', axis='x', linestyle='-')
    ax.set_axisbelow(True)
    ax.text(0, 1.12, '1500~2018', transform=ax.transAxes, size=24, weight=600, ha='left')
    plt.box(False)


# draw_barchart(2017)

animator = animation.FuncAnimation(fig, draw_barchart, range(1996, 2018))
HTML(animator.to_jshtml())
plt.show()