from pywinauto.application import Application

app = Application(backend='uia').start('"D:\\Program Files\\PremiumSoft\\Navicat Premium 15\\navicat.exe"')

dlg = app["Navicat Premium"]

# 打印窗口所有的控件
# kon = dlg.print_control_identifiers()
# print(kon)

# 选择菜单
menu = dlg['menu']

file = menu.child_window(title="文件")

# 查看控件类型
# print(dlg.wrapper_object())
# print(menu.wrapper_object())
# print(file.wrapper_object())

# dir查看对象所支持的方法
# print(dir(dlg.wrapper_object()))


# 控件的文本类型获取
# print(file.texts())


# 获取控件子元素
# print(dlg.children())


# 获取菜单子元素
# print(file.children())

# 获取控件类名
# print(menu.class_name())

# 获取控件的属性,返回字典
print(menu.get_properties())
