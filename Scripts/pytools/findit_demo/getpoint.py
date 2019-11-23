'''
该工具将主要作为图像识别服务出现，用于在目标图像中寻找模板图片的位置
https://testerhome.com/topics/19218
https://github.com/williamfzc/findit

'''

import pprint
from findit import FindIt

fi = FindIt()
fi.load_template('wechat_logo', pic_path='pics/wechat_logo.png')

result = fi.find(
    target_pic_name='screen',
    target_pic_path='pics/screen.png',
)

pprint.pprint(result)