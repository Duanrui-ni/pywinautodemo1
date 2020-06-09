from pywinauto import mouse

# 鼠标左键
# mouse.click(coords=(560, 48))

# 鼠标右键
# mouse.right_click(coords=(1000, 500))

# 鼠标双击
# mouse.double_click(button="left", coords=(50, 155))

# 点击鼠标中间键盘
# mouse.wheel_click(coords=(1000, 500))

# 按下鼠标
# mouse.press(coords=(60, 10))

# 释放鼠标
# mouse.release(coords=(500, 1000))

# 滑动鼠标滚轮 负数往上滚
# mouse.scroll(coords=(1000, 350), wheel_dist=-1)

mouse.move(coords=(0, 0))

for i in range(0, 1000, 50):
    mouse.move(coords=(i, i))
