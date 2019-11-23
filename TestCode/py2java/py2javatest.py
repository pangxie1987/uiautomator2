'''
通过第三方库jpype实现python调用Java
安装：https://blog.csdn.net/qq_38934189/article/details/79460085
调用：https://www.cnblogs.com/mumuli/p/5806963.html
'''

import jpype
import os

jarpath = os.path.join(os.path.dirname(__file__), 'test.jar')
print(jarpath)

jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", "-Djava.class.path=%s"%jarpath)
Test = jpype.JClass('com.Test')

t = Test()

res = t.run('a')

print(res)

jpype.shutdownJVM()
