'''
matplotlib学习
漫威英雄能力值绘制
https://www.cnblogs.com/chenqionghe/p/12376528.html
'''



import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.colors as mcolors

# 导入中文
import matplotlib.font_manager as font_manager

abilities = ['智力', '力量', '速度', '耐力', '能量', '技能']
super_heros = {
    '美国队长': [5, 4, 3, 4, 3, 7],
    '钢铁侠': [6, 3, 5, 5, 3, 3],
    '绿巨人': [6, 7, 3, 7, 1, 5],
    '蜘蛛侠': [5, 4, 5, 4, 2, 5],
    '灭霸': [7, 7, 7, 7, 7, 7],
    '雷神': [2, 5, 6, 7, 6, 6],
    '绯红女巫': [3, 3, 3, 3, 7, 3],
    '黑寡妇': [5, 3, 2, 3, 3, 7],
    '鹰眼': [5, 3, 3, 2, 2, 7],
}
# 生成战力图(能力指标,超级英雄能力值)

font_dirs = ['./font']
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)
plt.rcParams['font.family'] = 'SimHei'

# 启用主题
plt.style.use('ggplot')

# 获取极径范围
def get_range(data_list):
    max = min = 0
    for _, data in data_list.items():
        for v in data:
            if v < min:
                min = v
            if v > max:
                max = v
    return [min, max]

# 生成能力分布图
def generate_ability_map(abilities, data_list, rows=3):
    min, max = get_range(data_list)
    # 根据能力项等分圆
    angles = np.linspace(0, 2 * np.pi, len(abilities), endpoint=False)
    angles = np.append(angles, angles[0])
    # 生成n个子图
    fg, axes = plt.subplots(math.ceil(len(data_list) / rows), rows, subplot_kw=dict(polar=True))
    # 调整子图间距
    plt.subplots_adjust(wspace =0.6, hspace =0.6)
    # 打散为一维数组
    axes = axes.ravel()
    # 获取所有支持的颜色
    colors = list(mcolors.TABLEAU_COLORS)
    # 循环绘制
    i = 0
    for name, data in data_list.items():
        data = np.append(np.array(data), data[0])
        ax = axes[i]
        # 绘制线条
        ax.plot(angles, data, color=colors[i])
        # 填充颜色
        ax.fill(angles, data, alpha=0.7, color=colors[i])
        # 设置角度
        ax.set_xticks(angles)
        # 设置坐标轴名称
        ax.set_xticklabels(abilities)
        # 设置名称
        ax.set_title(name, size=10, color='black', position=(0.5, 0.4))
        # 设置极径最小值
        ax.set_rmin(min)
        # 设置极径最大值(最大值加0.1，要不线条最外圈线显示不完全)
        ax.set_rmax(max + 0.1)
        i = i + 1
    plt.show()

if __name__ == '__main__':
	generate_ability_map(abilities, super_heros)
