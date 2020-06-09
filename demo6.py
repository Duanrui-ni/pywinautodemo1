from pywinauto.application import Application

app = Application(backend='uia').start('"D:\\Program Files\\PremiumSoft\\Navicat Premium 15\\navicat.exe"')

# 选择窗口
dlg = app["Navicat Premium"]
# 选择菜单
menu = dlg["menu"]
# 选择菜单项：文件
file = menu.child_window(title="文件")

# 截图处理
# pic = dlg.capture_as_image()
# # print(pic)
# pic.save("01.png")

# 菜单截图
# pic = menu.capture_as_image()
# pic.save("02.png")

# 截图菜单项文件
pic3 = file.capture_as_image()
pic3.save("03.png")