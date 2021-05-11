from selenium import webdriver
import time
driver = webdriver.Chrome()
time.sleep(3)
url = "https://www.baidu.com/"
time.sleep(3)
driver.get(url)
time.sleep(3)
# 用id定位百度搜索框
# driver.find_element_by_id("kw").send_keys("王一博")
# driver.find_element_by_id("su").click()

# 用class name来定位----不能唯一定位到某个元素
# driver.find_element_by_xpath("//*[@id='form']/span[1]").send_keys("杨洋")
# driver.find_element_by_xpath("//*[@id='su']").click()


# 用link—text来定位
driver.find_element_by_link_text("新闻").click()

# 用partial link text定位
driver.find_element_by_partial_link_text("123").click()

# 用tag name定位
driver.find_element_by_tag_name("input").send_keys("白雪公主")
driver.find_element_by_tag_name("input").click()

# 用xpath定位
driver.find_element_by_xpath("//*[@id='kw']").send_keys("七仙女")
driver.find_element_by_xpath("//*[@id='su']").click()

# 用css path来定位
driver.find_element_by_css_selector("#kw").send_keys("童话故事")
driver.find_element_by_css_selector("#su").click()

# 用text获取文本内容
text = driver.find_element_by_id("s-top-left").text
print(text)

time.sleep(6)
driver.quit()




