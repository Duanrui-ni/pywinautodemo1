from pywinauto.application import Application

# 打开指定程序

# 1.打开Windows自带应用
# app = Application(backend='uia').start("notepad.exe")


# 2.打开任意一个应用程序
app = Application(backend='uia').start('"D:\\Program Files\\PremiumSoft\\Navicat Premium 15\\navicat.exe"')
