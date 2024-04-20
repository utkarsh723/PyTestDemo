from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def do_click(self,bylocator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(bylocator)).click()

    def do_sendkeys(self,bylocator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(bylocator)).send_keys(text)

    def get_element_text(self,bylocator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(bylocator))
        return element.text

    def is_enabled(self,bylocator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(bylocator))
        return bool(element)

    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title

    def double_click(self,bylocator):
        ele = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(bylocator))
        action = ActionChains(self.driver)
        action.double_click(ele).perform()
