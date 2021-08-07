# import requests
from selenium import webdriver

# 指定驱动 下载地址：http://npm.taobao.org/mirrors/chromedriver
driver_path = "C:\\Users\\E450C-15\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\chromedriver.exe"
options = webdriver.ChromeOptions()
# 隐藏窗口
# options.add_argument('headless')
# 防止打印一些无用的日志
options.add_experimental_option("excludeSwitches", ['enable-automation','enable-logging'])
# 禁止图片的加载
options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

# 创建浏览器对象
driver = webdriver.Chrome(driver_path, options = options)
# 最大化窗口
driver.maximize_window()
# 宽480、高800
# driver.set_window_size(480, 800)
driver.get("http://43.229.185.55:8088/")

driver.find_element_by_id('txtLoginName').send_keys('admin')
driver.find_element_by_id('Password').send_keys('Aa@123456')
driver.find_element_by_id('btnLogin').click()


# 跳到ifream
# driver.switch_to.frame('id或name')
# 跳回最外层
# driver.switch_to.default_content()

# 返回（后退）
# driver.back()
# 前进
# driver.forward()
# 刷新当前页面
# driver.refresh()


# 执行JavaScript脚本
# driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# driver.execute_script('alert("To Bottom")')


# # 获得当前窗口句柄
# sreach_windows = driver.current_window_handle
# # 获得所有窗口句柄
# driver.window_handles
# # 切换到相应的窗口
# driver.switch_to.window(sreach_windows)

# 关闭当前窗口
# driver.close()
# 退出驱动关闭所有窗口
# driver.quit()

# # 获得所有cookie
# driver.get_cookies()
# # 获得cookie
# driver.get_cookie('name')
# # 添加cookie
# driver.add_cookie("{'name': 'key-aaaaaaa', 'value': 'value-bbbbbb'}")
# # 删除cookie信息
# driver.delete_cookie('name','optionsString')
# # 删除所有cookie
# driver.delete_all_cookies()