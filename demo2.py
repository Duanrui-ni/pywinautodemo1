from pywinauto.application import Application

# 2.打开任意一个应用程序
# app = Application(backend='uia').start('"D:\\Program Files\\PremiumSoft\\Navicat Premium 15\\navicat.exe"')

# 1.通过进程号连接进程
# app = Application("uia").connect(process=12060)
# print(app)

# 2.通过窗口句柄连接
app = Application("uia").connect(handle=788862)
print(app)
