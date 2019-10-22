'''
淘宝领取瞄币
'''

import os
import pprint
import time
import unittest
import uiautomator2 as u2

class TaoBao(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.d = u2.connect_usb('emulator-5554')     # usb连接方式;adb devices 获取设备信息
        # self.d = u2.connect('172.27.177.9')     # IP连接方式；adb devices 获取设备信息
        self.d.healthcheck()  # 检查并维持设备端守护进程处于运行状态
        # self.d.disable_popups(True)   # 允许自动处理弹出框 
        # self.d.disable_popups(False)  # 禁用自动跳过弹出窗口
        # self.d.toast.show("Hello world")    # 手机屏幕显示
        # self.d.press("home") # 返回home页
        # self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").wait(timeout=10.0)
        # self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").click()    # 从home进入应用程序
        # self.d(text="手机淘宝").click()
        # # 进入红包界面
        # self.d.xpath('//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]').click()
        # time.sleep(5)
        # # 进入领取喵币页面
        # self.d.xpath('//*[@resource-id="6616644718"]/android.view.View[2]/android.view.View[1]/android.view.View[4]').click()

    # def setUp(self):
    #     self.d.press("home") # 返回home页
    #     self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").wait(timeout=10.0)
    #     self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").click()    # 从home进入应用程序

    def tearDown(self):
        # 返回
        self.d(text="返回").click()

    def test_a_qiandao(self):
        '签到'
        try:
            self.d(text='签到').click()
            print('签到成功')
        except:
            print('签到失败')
            self.d.screenshot(os.path.join('taobao', '签到'))

    def test_d1_Clinique(self):
        '第一个店铺'
        self.d(text="去进店").click()
        time.sleep(3)
        for i in range(5):
            # self.d(resourceId="com.taobao.taobao:id/bottom_right_linear").drag_to(1, 1, duration=1)   # 向上拖拽，切换视频
            self.d.xpath('//*[@resource-id="com.taobao.taobao:id/weex_render_view"]/android.widget.FrameLayout[3]/android.widget.ImageView[1]').drag_to(0,75, duration=1)
            print('滑动视频第%s次'%i)

    
    def test_d2_shop(self):
        '店铺领取喵币'
        # 进入店铺
        self.d.xpath('//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]').click()
        # 等待10S获取瞄币
        time.sleep(13)

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TaoBao('test_d_Clinique'))
    # suit.addTest(TaoBao('test_shuabao_task'))
    # suit.addTest(TaoBao('test_shuabao'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    # unittest.main()