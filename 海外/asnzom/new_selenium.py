from selenium import webdriver

# 创建 webdriver 对象，并打开浏览器
driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")

# 获取 cookie
cookie = driver.get_cookies()

# 打印 cookie 列表
print(cookie)
