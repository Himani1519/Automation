import unittest
from tests.base_test import BaseTest
from pages.main_page import *
from utils.test_cases import test_cases
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains


class TestNoBrokerPage(BaseTest):
  
    def test_mainPage(self):
        print("\n" + str(test_cases(0)))
        page = MainPage(self.driver)

        # step1: user click on dropdown to select city Mumbai from list
        click_dropdown = page.click_dropdown()
        search_result = page.search_city()
        validate_city = page.valiate_selected_city()
        self.assertEqual("Mumbai", validate_city)

        #step2 : select buy property related option
        print("\n" + str(test_cases(1)))
        buy_button = page.click_Buy_Button()


        # step3: Type malad in search box and select MaladEast-Malkani Estate and MaladWest-SundarLn
        print("\n" + str(test_cases(2)))
        search_result = page.search("Malad")
        locality_click = page.click_dropdown_select_locality()
        select_locality = page.select_locality1()
        time.sleep(5)
        search_result = page.search("Malad")
        select_locality = page.select_locality2()
        time.sleep(2)

        #step4: select 2BHK and 3 BHK from the BHK type
        print("\n" + str(test_cases(3)))
        Bhk_dropdown = page.click_BHK_dropdown()
        time.sleep(5)
        select_1bhk = page.select_2BHK()
        select_2bhk = page.select_3BHK()

        #step5: Click on serach button after selecting 2bHK and 3bHK
        print("\n" + str(test_cases(4)))
        search_property = page.click_search_button()

        #step6: Scroll down on property listing page and click on 4th property
        print("\n" + str(test_cases(5)))
        scroll_page = page.scrol_page()    
        time.sleep(5)
        self.driver.implicitly_wait(10)
        click_4th_property = page.click_4th_property()
        time.sleep(10)

        #step7: scroll down and check description tag is there or not 
        print("\n" + str(test_cases(6)))
        self.driver.switch_to.window(self.driver.window_handles[1])
        scroll_page = page.scrol_page()  
        time.sleep(10)
        description_tag = page.check_description_tag()
        print(description_tag)
        self.assertNotEqual("", description_tag) 
        if(description_tag != ""):
            print("Test case Pass")
        else:
            print("Fail")



    


   



  

    