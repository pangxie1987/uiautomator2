#! /usr/bin/env python
#coding=utf-8
#pywinauto自动化操作微信号
import pyperclip
import win32clipboard as wc
import win32api,win32gui,win32con
import sys,os;
from pywinauto.application import *
import pyautogui as pag
from PIL import ImageGrab
import time
import os

headpath = os.path.join(os.path.dirname(os.path.abspath(__file__)),'head')
print(headpath)

class WinChat(object):

   def __init__(self, url, args):
       self.url = url
       self.args = args.split(',')
       print(self.url)
       print(self.args)

   def paste(self, groupid):
       pyperclip.copy(groupid)
       pag.hotkey('ctrl', 'v')

   def send_msg(self):
       app = Application().start(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
       if not app.windows():
            app = Application().connect(path=r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
       app.window(title=u"微信",class_name="WeChatMainWndForPC").move_window(0,0)
       while True:
       # 截取屏幕，这只是缓存，如果要保存截图，可以带上参数，即要保存的路径
           pag.screenshot()
           print('url===========%s'%self.url)
       # 在屏幕截图中找到微信联系人的按钮图标，找到的话返回坐标如(42, 405, 27, 28)，找不到返回 None
         #   pointLeft1 = pag.locateOnScreen('head/square.png')
         #   pointLeft2 = pag.locateOnScreen('head/square2.png')
           pointLeft1 = pag.locateOnScreen(os.path.join(headpath,'square.png'))
           pointLeft2 = pag.locateOnScreen(os.path.join(headpath,'square2.png'))
           if pointLeft1 is not None:
              pointLeft=pointLeft1
              break
           if pointLeft2 is not None:
              pointLeft=pointLeft2
              break
       print(pointLeft)
       # 找到按钮后，就能取得它的坐标，横坐标 +100，即在联系人上点击右键
       pag.click(pointLeft[0] + 10, pointLeft[1]+10)
       time.sleep(1)
       while True:
       # 截取屏幕，这只是缓存，如果要保存截图，可以带上参数，即要保存的路径
           pag.screenshot()
       # 在屏幕截图中找到微信联系人的按钮图标，找到的话返回坐标如(42, 405, 27, 28)，找不到返回 None
           pointLeft1 = pag.locateOnScreen(os.path.join(headpath,'new.png'))
         #   pointLeft1 = pag.locateOnScreen('head/new.png')
    
           if pointLeft1 is not None:
                pointLeft=pointLeft1
                break
    
       print(pointLeft)
       # 找到按钮后，就能取得它的坐标，横坐标 +100，即在联系人上点击右键
       pag.click(pointLeft[0] + 20, pointLeft[1]+5)
       time.sleep(1)
       win = app.window(title=u"笔记",class_name="FavNoteWnd")
       while True:
           if win==0:
              pag.click(pointLeft[0] + 20, pointLeft[1]+5)
              time.sleep(1)
              win = app.window(title=u"笔记",class_name="FavNoteWnd")
           if win!=0:
              break
       app.window(title=u"笔记",class_name="FavNoteWnd").move_window(0,0)
       app.window(title=u"微信",class_name="WeChatMainWndForPC").minimize()
       app.window(title=u"笔记",class_name="FavNoteWnd").type_keys(self.url).type_keys("{LEFT}").type_keys("{ENTER}")
       time.sleep(4)
       app.window(title=u"笔记",class_name="FavNoteWnd").close()


       while True:
       # 截取屏幕，这只是缓存，如果要保存截图，可以带上参数，即要保存的路径
           pag.screenshot()
       # 在屏幕截图中找到微信联系人的按钮图标，找到的话返回坐标如(42, 405, 27, 28)，找不到返回 None
         #   pointLeft1 = pag.locateOnScreen('head/out.png')
           pointLeft1 = pag.locateOnScreen(os.path.join(headpath,'out.png'))
           if pointLeft1 is not None:
               pointLeft=pointLeft1
               break

       print(pointLeft)
       # 找到按钮后，就能取得它的坐标，横坐标 +100，即在联系人上点击右键
       pag.click(pointLeft[0] + 10, pointLeft[1]+10)
       time.sleep(4)

       win=app.window(title=u"微信",class_name="SelectContactWnd")
       print('===============================',self.args)

       for groupid in self.args:
            print('groupid=======',groupid)
            while True:
            # 截取屏幕，这只是缓存，如果要保存截图，可以带上参数，即要保存的路径
                  pag.screenshot()
            # 在屏幕截图中找到微信联系人的按钮图标，找到的话返回坐标如(42, 405, 27, 28)，找不到返回 None
                  # pointLeft1 = pag.locateOnScreen('head/searchall.png')
                  # pointLeft2 = pag.locateOnScreen('head/searchall2.png')
                  pointLeft1 = pag.locateOnScreen(os.path.join(headpath,'searchall.png'))
                  pointLeft2 = pag.locateOnScreen(os.path.join(headpath,'searchall2.png'))
                  if pointLeft1 is not None:
                     pointLeft=pointLeft1
                     break
                  if pointLeft2 is not None:
                     pointLeft=pointLeft2
                     break
            print(pointLeft)
            pag.click(pointLeft[0] + 100, pointLeft[1]+5)
            #time.sleep(1)
            # self.paste(groupid)
            pyperclip.copy(groupid)
            pag.hotkey('ctrl', 'v')
            time.sleep(1)
            pag.keyDown('enter')
            time.sleep(1)
            pag.click(pointLeft[0] + 100, pointLeft[1]+5)
            pag.hotkey('ctrl', 'a')
            pag.keyDown('delete')
            time.sleep(1)


       while True:
        # 截取屏幕，这只是缓存，如果要保存截图，可以带上参数，即要保存的路径
           pag.screenshot()
        # 在屏幕截图中找到微信联系人的按钮图标，找到的话返回坐标如(42, 405, 27, 28)，找不到返回 None
         #   pointLeft1 = pag.locateOnScreen('head/btn.png')
           pointLeft1 = pag.locateOnScreen(os.path.join(headpath,'btn.png'))
           if pointLeft1 is not None:
              pointLeft=pointLeft1
              break
       print(pointLeft)
       pag.click(pointLeft[0] + 20, pointLeft[1]+10)
       time.sleep(1)

       try:
          win=app.window(title=u"微信",class_name="SelectContactWnd").close()
       except:
          print("close win")

       try:
          win=app.window(title=u"微信",class_name="CefWebViewWnd").close()
       except:
          print("close win")

       app.window(title=u"微信",class_name="WeChatMainWndForPC").restore()
if __name__ == '__main__':
      Test = WinChat("http://www.baidu.com",'zixuntest','杨治邦')
      Test.send_msg()
