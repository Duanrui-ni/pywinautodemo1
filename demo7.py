from pywinauto.application import Application
import time

app = Application('uia').start('"D:\\Program Files\\PremiumSoft\\Navicat Premium 15\\navicat.exe"')

# 选择窗口
dlg = app["Navicat Premium"]
# 选择菜单
menu = dlg["menu"]
# 选择菜单项：文件
file = menu.child_window(title="文件")
# print(menu.items())


# 通过下标选择菜单项
# m = menu.item_by_index(0)
# print(m)


# 通过路径选择菜单项
# m2 = menu.item_by_path("文件->新建连接")
# print(m2)

# 菜单项的操作方法
# 获取子菜单项的方法
# print(file.items())

# 点击菜单项的方法:

file.click_input()

menu.item_by_path("文件->新建连接").click_input()

menu.item_by_path("文件->新建连接->MySql...").click_input()

time.sleep(2)
mm = app["MySQL - 新建连接"]

mm.wait(wait_for="ready", timeout=3, retry_interval=1)
print("等待通过，当前新建连接的窗口处于可见")

# 等待窗口处于可见状态
# mm.wait_not(wait_for_not="ready", timeout=3, retry_interval=1)
# # print("等待通过，当前新建连接的窗口处于不可见")

# app = Application().connect(process=17260)
# app.wait_cpu_usage_lower(threshold=20, timeout=5, usage_interval=1)
# print("等待通过，当前进程CPU占用低于20%")
