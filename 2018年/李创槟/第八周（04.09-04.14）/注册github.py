#coding = utf-8
#为防止乱码问题，以及方便添加中文注解，通过以上语句把编码统一成UTF-8
from selenium import webdriver
import random,string, time

def createUserName():
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 10))
    return ran_str

class Register():
    def setUp(self):
        self.driver = webdriver.Chrome()#获取浏览器对象，启动浏览器
        self.driver.implicitly_wait(30)
        self.base_url = "https://github.com/"
    def register(self):
        "从主页跳转到注册页面，填写注册信息，不断下一步，注册成功"
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        ran_str = createUserName()
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div/div/div[2]/div/form/button").click()
        driver.find_element_by_id("user_login").send_keys(ran_str)
        driver.find_element_by_id("user_email").send_keys(ran_str+"@abc.com")
        driver.find_element_by_id("user_password").send_keys(ran_str+"1")
        driver.find_element_by_id("signup_button").click()
        driver.find_element_by_xpath(".// *[ @ id = 'js-pjax-container'] / div / div[2] / div / form / button").click()
        driver.find_element_by_xpath(".// *[ @ id = 'js-pjax-container'] / div / div[2] / div / form / input[3]").click()
        time.sleep(3)
    def log_out(self):
        "退出登录"
        driver = self.driver
        driver.find_element_by_class_name("logout-form").submit()
    def tearDown(self):
        "退出驱动"
        self.driver.quit()#退出并关闭窗口的每一个相关的驱动程序
if __name__ == "__main__":
    cla = Register()
    cla.setUp()
    cla.register()
    cla.log_out()
    cla.tearDown()