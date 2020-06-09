import pywinauto
from pywinauto.keyboard import send_keys
from selenium import webdriver

url = "https://www.layui.com/demo/upload.html"
chrome_driver = r"D:\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chrome_driver)
browser.get(url=url)

# 点击图片上传按钮，打开文件选择窗口
browser.find_element_by_css_selector(".layui-btn#test1").click()


# 使用pywinauto来选择文件

app = pywinauto.Desktop()
# 选中文件上传的窗口 打开
dlg = app["打开"]
dlg.print_control_identifiers()

# 选中文件地址输入工具框
dlg["Toolbar3"].click()
send_keys("D:\MyFiles\OneDrive\桌面\视频会员")
send_keys("{VK_RETURN}")

# 选中文件名输入框
dlg["Edit"].type_keys("1068010679.jpg")
dlg["打开(&O)"].click()

# .layui-btn#test2