from pywinauto.application import Application
import time

app = Application('uia').start('"D:\\Program Files\\PremiumSoft\\Navicat Premium 15\\navicat.exe"')

# app = Application("uia").connect(process=12060)

dlg = app["Navicat Premium"]
# 窗口最大化
dlg.maximize()
# 窗口最小化
# dlg.minimize()
time.sleep(1)
# 窗口恢复
dlg.restore()
# 显示窗口状态：最大化是1，正常0
# status = dlg.get_show_state()
# print(status)
# 关闭窗口
# dlg.close()

# 获取当前窗口显示的坐标
rect = dlg.rectangle()
print(rect)


