from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils.locators import *
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

# Page objects are covered in this file

class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)  

    def check_description_tag(self):
        return self.find_element(*self.locator.CHECK_DESCRIPTION_TAG).text

    def scrol_page(self):
        self.driver.maximize_window()
        ActionChains(self.driver).send_keys(Keys.PAGE_DOWN).click().perform()
        time.sleep(5)

    def click_4th_property(self):
        self.driver.find_elements_by_xpath(self.locator.DESCRIPTION1)[3].click()
                
    def minimize_popup_window(self):
        self.find_element(*self.locator.MINIMIZE_POPUP).click()
    
    def click_search_button(self):
        self.find_element(*self.locator.SEARCH_BUTTON).click()

    def select_locality1(self):
        self.driver.implicitly_wait(10)
        self.find_element(*self.locator.SELECT_LOCALITY1).click()
    
    def select_locality2(self):
        self.driver.implicitly_wait(10)
        self.find_element(*self.locator.SELECT_LOCALITY2).click()

    def click_BHK_dropdown(self):
        return self.find_element(*self.locator.BHK).click()
    
    def select_2BHK(self):
        return self.find_element(*self.locator.BHK_2).click()

    def select_3BHK(self):
        return self.find_element(*self.locator.BHK_3).click()

    def click_Buy_Button(self):
        return self.find_element(*self.locator.BUY_BUTTON).click()

    def click_dropdown_select_locality(self):
        return self.find_element(*self.locator.LOCALITY_SEARCH).click()

    def search(self, item):
        self.driver.implicitly_wait(10)
        self.find_element(*self.locator.INPUT_TEXT).send_keys(item)
        self.find_element(*self.locator.INPUT_TEXT).send_keys()
    
    def valiate_selected_city(self):
        return self.find_element(*self.locator.CITY_DROPDOWN).text
    
    def search_city(self):
        self.find_element(*self.locator.SEARCH_CITY_LIST).click()

    def click_dropdown(self):
        self.find_element(*self.locator.CITY_DROPDOWN).click()

    




   
    

    
