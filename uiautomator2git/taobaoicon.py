'''
glax:   4d007003b2464067
Mi: f89bb868
leidian: emulator-5554
淘宝领取瞄币
'''

import os
import pprint
import time
import unittest
import uiautomator2 as u2

waittime = 22

class TaoBao(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.d = u2.connect_usb('4d007003b2464067')     # usb连接方式;adb devices 获取设备信息
        # self.d = u2.connect('172.27.177.9')     # IP连接方式；adb devices 获取设备信息
        self.d.healthcheck()  # 检查并维持设备端守护进程处于运行状态
        # self.d.disable_popups(True)   # 允许自动处理弹出框 
        # self.d.disable_popups(False)  # 禁用自动跳过弹出窗口
        # self.d.toast.show("Hello world")    # 手机屏幕显示
        # self.d.press("home") # 返回home页
        self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").wait(timeout=10.0)
        self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").click()    # 从home进入应用程序
        self.d(text="手机淘宝").click()
        time.sleep(8)
        # # 进入红包界面
        # self.d.xpath('//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[5]/android.widget.FrameLayout[1]/android.widget.FrameLayout[3]/android.widget.FrameLayout[1]').click()
        # time.sleep(8)
        # # 进入领取喵币页面
        # self.d.xpath('//*[@resource-id="6616644718"]/android.view.View[2]/android.view.View[1]/android.view.View[4]').click()
        # '进入红包页面'
        # self.d.xpath('//*[@resource-id="com.taobao.taobao:id/rv_main_container"]/android.widget.FrameLayout[4]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.FrameLayout[6]').click()
        # print('进入红包')
        # time.sleep(8)

    # def tearDown(self):
    #     # 返回
    #     # self.d(text="返回").click()
    #     self.d.press('back')

    def test_a_qiandao(self):
        '签到'
        try:
            self.d(text='签到').click()
            print('签到成功')
        except:
            print('签到失败')
            self.d.screenshot(os.path.join('taobao', '签到'))

    @classmethod
    def test_d0_shop(self):
        '领取上限15000个'
        self.setUpClass()
        self.d(text="上限15000").click()
        print('领取上限15000的喵币')
        self.d.screenshot(os.path.join('taobao', '上限1500.jpg'))
        time.sleep(4)

    def test_d1_shoplist(self):
        '进入店铺列表'
        self.d.xpath('//*[@resource-id="6616644718"]/android.view.View[1]/android.view.View[1]/android.view.View[4]').click()
        print('进入店铺列表')
        time.sleep(4)

    def test_f_back(self):
        '返回红包页面'
        self.d.xpath('//android.widget.Button').click()
        time.sleep(3)
    
    def test_d2_shop(self):
        '第一个店铺领取喵币'
        for k in range (20):
            for i in range(8):
                # # 进入店铺
                # self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.view.View[1]/android.view.View[8]/android.view.View[2]/android.view.View[3]').click()
                # # 等待10S获取瞄币
                # print('第一个店铺领取喵币')
                # time.sleep(waittime)
                ## self.d(description="转到上一层级").click()
                # self.d.press('back')

                '第二个店铺领取喵币'
                # 进入店铺
                self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.view.View[1]/android.view.View[8]/android.view.View[3]/android.view.View[3]').click()
                # 等待10S获取瞄币
                print('第二个店铺领取喵币')
                time.sleep(waittime)
                # self.d(description="转到上一层级").click()
                self.d.press('back')

                # '第三个店铺领取'
                # self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.view.View[1]/android.view.View[8]/android.view.View[4]/android.view.View[3]').click()
                # print('第三个店铺领取')
                # time.sleep(waittime)
                ## self.d(description="转到上一层级").click()
                # self.d.press('back')

                '第四个店铺领取'
                # self.d.xpath('//*[@text="去浏览"]').click()
                self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.view.View[1]/android.view.View[8]/android.view.View[5]/android.view.View[3]').click()
                print('第四个店铺领取')
                time.sleep(waittime)
                # self.d(description="转到上一层级").click()
                self.d.press('back')

                '第五个店铺领取'
                # self.d(text="去进店").click()
                self.d.xpath('//*[@resource-id="taskBottomSheet"]/android.view.View[1]/android.view.View[8]/android.view.View[6]/android.view.View[3]').click()
                print('第五个店铺领取')
                time.sleep(waittime)
                #self.d(description="转到上一层级").click()
                self.d.press('back')
                time.sleep(3)

            self.test_f_back()
            self.test_d0_shop()
            self.test_d1_shoplist()


if __name__ == '__main__':
    suit = unittest.TestSuite()
    # suit.addTest(TaoBao('test_d0_shop'))
    # suit.addTest(TaoBao('test_d1_shoplist'))
    suit.addTest(TaoBao('test_d2_shop'))
    #suit.addTest(TaoBao('test_d3_shop'))
    # suit.addTest(TaoBao('test_d1_shop'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    # unittest.main()