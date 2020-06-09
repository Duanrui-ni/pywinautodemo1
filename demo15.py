import pywinauto
from pywinauto.keyboard import send_keys
from selenium import webdriver


# "D:\MyFiles\OneDrive\桌面\视频会员"
# 多文件上传
def upload_files(file_path, file, *args):
    url = "https://www.layui.com/demo/upload.html"
    chrome_driver = r"D:\chromedriver.exe"
    browser = webdriver.Chrome(executable_path=chrome_driver)
    browser.get(url=url)

    # 点击图片上传按钮，打开文件选择窗口
    browser.find_element_by_css_selector(".layui-btn#test2").click()

    # 使用pywinauto来选择文件

    app = pywinauto.Desktop()
    # 选中文件上传的窗口 打开
    dlg = app["打开"]
    dlg.print_control_identifiers()

    # 选中文件地址输入工具框
    dlg["Toolbar3"].click()
    send_keys(file_path)
    send_keys("{VK_RETURN}")

    # 选中文件名输入框
    # 输入第一个文件名
    dlg["Edit"].type_keys('"{}"'.format(file))
    # 遍历不定长参数文件名
    for i in args:
        send_keys('"{}"'.format(i))
    # 输入第二个文件名采取键盘操作
    dlg["打开(&O)"].click()


upload_files("D:\MyFiles\OneDrive\桌面\视频会员", "8.jpg", "9.jpg")
