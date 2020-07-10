from selenium import webdriver

#引入ActionChains类
from selenium.webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Chrome()
driver.get("https://pan.baidu.com/")
driver.implicitly_wait(30)
driver.maximize_window()

driver.find_element_by_link_text("帐号密码登录").click()
driver.find_element_by_name("userName").clear()
driver.find_element_by_name("userName").send_keys("18221251607")
driver.find_element_by_name("password").send_keys("244479430qq")
driver.find_element_by_id("TANGRAM__PSP_4__submit").click()

#鼠标右击操作
#定位到要右击的元素
right_click=driver.find_element_by_link_text("我的收藏")
ActionChains(driver).context_click(right_click).perform()
#对定位到的元素执行鼠标右键操作
#ActionChains(driver)调用ActionChains()类将浏览器驱动driver作为参数传入
#context_click(right_click),context_click()方法用户模拟鼠标右击，在调用时要指定定位元素
#perform()执行所有ActionChains中存储的行为，可以理解成是对整个操作的提交动作

#鼠标双击操作
double=driver.find_element_by_xpath(".//*[@id='dynamicLayout_0']/div/div/dl/dd[2]/span/span[2]")
ActionChains(driver).double_click(double).perform()

#鼠标悬停操作
move=driver.find_element_by_xpath(".//*[@id='dynamicLayout_0']/div/div/dl/dd[2]/span/span[2]")
ActionChains(driver).move_to_element(move).perform()

#鼠标拖放操作
tuo=driver.find_element_by_link_text("我的收藏")
fang=driver.find_element_by_link_text("我的资源")
#drag_and_drop(source,target)  source：鼠标拖动的源元素  target：鼠标释放的目标元素
ActionChains(driver).drag_and_drop(tuo,fang).perform()
