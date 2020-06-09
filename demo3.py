from pywinauto.application import Application

Application('uia').start('"D:\\Program Files\\PremiumSoft\\Navicat Premium 15\\navicat.exe"')
app = Application("uia").connect(process=12060)
# 方式一：使用类名或标题选择窗口
# dig = app["TNavicatMainForm"]


# 方式二：通过窗口标题选择窗口
# dig = app["Navicat Premium"]


# 方式三四：使用app.类app.窗口选择窗口
dig = app.TNavicatMainForm
# 打印窗口所有的控件
dig.print_control_identifiers()
