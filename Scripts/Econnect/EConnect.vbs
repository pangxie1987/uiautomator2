dim program		'�Զ���¼EasyConnect
CreateObject("WScript.Shell").Run "taskkill /f /im SangforCSClient.exe", 0	'kill SangforCSClient.exe
wscript.Sleep 2000
program="C:\Program Files (x86)\Sangfor\SSL\SangforCSClient\SangforCSClient.exe" '���س���װ·��
set Wshell=CreateObject("Wscript.Shell")
set oexec=Wshell.Exec(program)
wscript.Sleep 5000
Wshell.AppActivate "SangforCSClient.exe"
wscript.Sleep 1000
Wshell.SendKeys "autotest5"		'�޸�Ϊ�Լ��û���
wscript.Sleep 200
Wshell.SendKeys "+{TAB}"
wscript.Sleep 200
Wshell.SendKeys "+{TAB}"
'wscript.Sleep 200
'Wshell.SendKeys "+{TAB}"
wscript.Sleep 200
Wshell.SendKeys "liupb123456#"	 '�޸�Ϊ�Լ�����
wscript.Sleep 200
Wshell.SendKeys "{ENTER}"
'����ΪVBS�ļ�����ECAgent.exe