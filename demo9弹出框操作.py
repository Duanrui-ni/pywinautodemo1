import pywinauto

app = pywinauto.Application().start("notepad.exe")

dlg = app["无标题 - 记事本"]

# 选择编辑框
# dlg.print_control_identifiers()

dlg["Edit"].type_keys("python做自动化非常方便,666")

# 替换操作

# 通过菜单选择替换

dlg.menu_select("编辑->替换(R)...")

app["替换"].print_control_identifiers()

# 选中查找编辑框
app["替换"]["Edit"].type_keys("666")

app["替换"]["Edit2"].type_keys("999")

app["替换"]["Button3"].click()

