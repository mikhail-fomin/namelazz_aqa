import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def text_to_be_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 10).until((EC.text_to_be_present_in_element, locator), text)

    def is_element_present(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def element_are_present(self,locator, timeout=5):
        return WebDriverWait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))

    def input_text(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.clear()
        element.send_keys(text)

    def input_text_keys_enter_time_sleep_4(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.clear()
        element.send_keys(text)
        time.sleep(4)
        element.send_keys(Keys.ENTER)


    def input_text_keys_enter(self, locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)


    def click_element_without_scroll(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def click_element2(self, locator):#Клик с ожиданием 2 секунды
        element = WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def element_is_visibile(self,locator, timeout=15):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visibile(self,locator, timeout=15):
        return WebDriverWait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))

    def elements_any_are_visibile(self, locator, timeout = 10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_any_elements_located(locator))










