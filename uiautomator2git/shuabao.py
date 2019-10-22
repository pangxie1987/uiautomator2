'''
uiautomator2  安卓自动化测试
https://www.jianshu.com/p/e5ed2ddb3f27
glax:   4d007003b2464067
Mi: f89bb868
leidian: emulator-5554
刷宝短视频
'''
import os
import pprint
import time
import unittest
import uiautomator2 as u2


class TestWeditor(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.d = u2.connect_usb('emulator-5554')     # usb连接方式;adb devices 获取设备信息
        # self.d = u2.connect('172.27.177.9')     # IP连接方式；adb devices 获取设备信息
        self.d.healthcheck()  # 检查并维持设备端守护进程处于运行状态
        # self.d.disable_popups(True)   # 允许自动处理弹出框 
        # self.d.disable_popups(False)  # 禁用自动跳过弹出窗口
        self.d.toast.show("Hello world")    # 手机屏幕显示

    # def setUp(self):
    #     self.d.press("home") # 返回home页

    # def tearDown(self):
    #     self.d.press("home") # 返回home页

    def test_deviceinfo(self):
        '获取设备信息'
        pprint(self.d.info)
        pprint(self.d.app_info)
        pprint(self.d.device_info)

    def rtest_calculator(self):
        '计算器'
        self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").wait(timeout=10.0)
        self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").click()    # 从home进入应用程序
        self.d(text='计算器').wait(timeout=10.0)
        self.d(text='计算器').click()
        self.d(resourceId="com.sec.android.app.popupcalculator:id/bt_clear").click()
        self.d(resourceId="com.sec.android.app.popupcalculator:id/bt_07").click()
        self.d(resourceId="com.sec.android.app.popupcalculator:id/bt_add").click()
        self.d(resourceId="com.sec.android.app.popupcalculator:id/bt_08").click()
        self.d(resourceId="com.sec.android.app.popupcalculator:id/bt_equal").click()
        #self.d(resourceId="com.sec.android.app.popupcalculator:id/bt_clear").click()
        #print(self.d(resourceId="com.sec.android.app.popupcalculator:id/top_txtCalc").get_text())
        print(self.d(resourceId="com.sec.android.app.popupcalculator:id/txtCalc").get_text())
        self.d.screenshot('result.jpg')
        # self.d.press("back") # 返回应用程序页
        self.d.press("home") # 返回home页

    def rtest_chrome(self):
        'chrome'
        self.d(text="Chrome").wait(timeout=10)
        self.d(text="Chrome").click()
        self.d(resourceId="com.android.chrome:id/url_bar").wait(timeout=10)
        self.d(resourceId="com.android.chrome:id/url_bar").clear_text()
        # self.d.set_fastinput_ime(True)   # 切换输入法
        self.d(resourceId="com.android.chrome:id/url_bar").set_text('http://www.baidu.com')
        self.d(text="百度一下").click()
        self.d(resourceId="index-kw").wait(timeout=10)
        self.d.set_fastinput_ime(True)   # 切换输入法
        self.d(resourceId="index-kw").set_text('德邦证券股份有限公司')
        self.d.set_fastinput_ime(False)   # 切换输入法
        self.d(resourceId="index-bn").click()

    def test_shuabao_basic(self):
        '打开刷宝短视频'
        self.d.press("home") # 返回home页
        self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").wait(timeout=10.0)
        self.d(resourceId="com.sec.android.app.launcher:id/home_allAppsIcon").click()    # 从home进入应用程序
        self.d(text="刷宝短视频").wait(timeout=10)
        self.d(text="刷宝短视频").click()
        self.d(text='首页').click()
        time.sleep(3)
    
    def test_shuabao_leidian(self):
        '雷电模拟器'
        self.d.press("home") # 返回home页
        self.d(text="刷宝短视频").wait(timeout=10)
        self.d(text="刷宝短视频").click()
        self.d(text='首页').click()
        time.sleep(3)

    def test_shuabao_task(self):
        '刷宝短视频-签到'
        try:
            self.d(text='任务').click()
            picname = time.strftime("%Y-%m-%d-%H%M%S", time.localtime())
            print(picname)
            self.d.screenshot(os.path.join('shuabao', picname+'.jpg')) 
            self.d(description='立即签到').click()
            # time.sleep(2)
            self.d.screenshot(os.path.join('shuabao', '签到.jpg')) 
            # self.d(description='继续赚元宝').click()
            self.d.press('back')
            print('签到成功：%s'%picname)
        except:
            print('签到失败')
        finally:
            self.d(text='首页').click()


    def test_shuabao(self):
        '刷宝短视频'
        self.d(text='首页').click()
        video_titles = []
        for i in range(100000):
        # while 1:
       
            try:
                self.d(resourceId="com.jm.video:id/mask_layer").drag_to(1, 1, duration=0.5)   # 向上拖拽，切换视频
                # self.d.swipe(1, 1, 0, 849)    #滑动
                title = self.d.xpath('//*[@resource-id="com.jm.video:id/desc"]').get_text()  # 获取视频title
                video_titles.append(title)
                print(video_titles)
                self.d.screenshot(os.path.join('shuabao', title+'.jpg'))
            except:
                # video_titles.append('no tile')
                # self.d.screenshot(os.path.join('shuabao', 'notile'+str(i)+'.jpg'))
                print('获取视频出错，请检查')
                # self.test_shuabao_basic()
                self.test_shuabao_leidian()
            time.sleep(63)
            i = i+1
            print(i)

if __name__ == '__main__':
    suit = unittest.TestSuite()
    # suit.addTest(TestWeditor('test_shuabao_basic'))
    suit.addTest(TestWeditor('test_shuabao_leidian'))
    suit.addTest(TestWeditor('test_shuabao_task'))
    suit.addTest(TestWeditor('test_shuabao'))
    runner = unittest.TextTestRunner()
    runner.run(suit)
    # unittest.main()
