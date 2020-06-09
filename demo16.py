import pywinauto
# from pywinauto.keyboard import send_keys

# app = pywinauto.Application("uia").start('"D:\\Program Files\\PremiumSoft\\Navicat Premium 15\\navicat.exe"')
app = pywinauto.Application(backend="uia").connect(process=16320)

# 选择主窗口
dlg = app["Navicat Premium"]
# dlg.print_control_identifiers()

# Menu = dlg["Menu"]
#
# Menu.child_window(title="文件", control_type="MenuItem").click_input()
# # 点击新建连接
# Menu.item_by_path("文件->新建连接").click_input()
# Menu.item_by_path("文件->新建连接->MySql...").click_input()
#
new_dlg = app["Navicat Premium"]["MySQL - 新建连接"]
# new_dlg.print_control_identifiers()
# 主机
new_dlg.child_window(title="常规", auto_id="527208", control_type="Pane").Edit1.type_keys("127.0.0.1")
#密码
new_dlg.child_window(title="常规", auto_id="527208", control_type="Pane").Edit2.type_keys("root")
# 用户名
new_dlg.child_window(title="常规", auto_id="527208", control_type="Pane").Edit3.type_keys("root")
# 端口
new_dlg.child_window(title="常规", auto_id="527208", control_type="Pane").Edit4.type_keys("3306")
# 连接名
new_dlg.child_window(title="常规", auto_id="527208", control_type="Pane").Edit5.type_keys("测试新建连接")

# 点解确定按钮
new_dlg.确定.click()