import subprocess
import uiautomation

# 程序窗口:WindowControl()
# 按钮：ButtonControl()
# 文件显示：TextControl()
# 输入框：EditControl()
# 一般定位的属性有：ClassName、Name、ProcessId、AutomationId

#打开计算器进程
subprocess.Popen('calc.exe')
#定位窗口
wc=uiautomation.WindowControl(searchDepth=1,Name='计算器')
#设置为顶层
wc.SetTopmost(True)

# wc.Click() #点击；
# wc.RighClik() #右键点击
# wc.SendKeys() #发送字符
# wc.SetValue() #传值，一般对EditControl用
# wc.MenuItemControl(Name="查看(V)").Click()
wc.ButtonControl(Name='7').Click()
wc.ButtonControl(Name='加').Click()
wc.ButtonControl(Name='5').Click()
wc.ButtonControl(Name='等于').Click()
result=wc.TextControl(AutomationId='158')
print(result.Name)
# wc.CaptureToImage('1.png') #截图
wc.ButtonControl(Name='关闭').Click()