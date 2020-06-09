import pywinauto

app = pywinauto.Application(backend="uia").connect(process=16320)

app["Navicat Premium"].print_control_identifiers()

# P25 之前  Navicat左侧菜单栏识别失败