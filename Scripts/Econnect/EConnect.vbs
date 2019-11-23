dim program		'自动登录EasyConnect
CreateObject("WScript.Shell").Run "taskkill /f /im SangforCSClient.exe", 0	'kill SangforCSClient.exe
wscript.Sleep 2000
program="C:\Program Files (x86)\Sangfor\SSL\SangforCSClient\SangforCSClient.exe" '本地程序安装路径
set Wshell=CreateObject("Wscript.Shell")
set oexec=Wshell.Exec(program)
wscript.Sleep 5000
Wshell.AppActivate "SangforCSClient.exe"
wscript.Sleep 1000
Wshell.SendKeys "autotest5"		'修改为自己用户名
wscript.Sleep 200
Wshell.SendKeys "+{TAB}"
wscript.Sleep 200
Wshell.SendKeys "+{TAB}"
'wscript.Sleep 200
'Wshell.SendKeys "+{TAB}"
wscript.Sleep 200
Wshell.SendKeys "liupb123456#"	 '修改为自己密码
wscript.Sleep 200
Wshell.SendKeys "{ENTER}"
'保存为VBS文件运行ECAgent.exe