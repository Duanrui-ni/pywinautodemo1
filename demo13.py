from pywinauto import Application

app = Application("uia").connect(path="explorer")

# app["任务栏"].print_control_identifiers()

# task = app["任务栏"].child_window(title="用户提示通知区域", auto_id="1504", control_type="ToolBar")

# task.print_control_identifiers()

# task.child_window(title="QQ: Danrid(249190451)\r\n声音: 开启\r\n消息提醒框: 关闭\r\n会话消息: 自动弹出会话窗口", control_type="Button").click()

task = app["任务栏"].child_window(title="通知 V 形", auto_id="1502", control_type="Button")
task.click()
# app["通知溢出"].print_control_identifiers()
app["通知溢出"]['NVIDIA 设置'].click()