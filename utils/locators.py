from selenium.webdriver.common.by import By
from csv import DictReader

# Mainatin a sperate class for locators

class MainPageLocators(object):
    with open('data.csv', 'r') as read_obj: 
        csv_dict_reader = DictReader(read_obj)
        for row in csv_dict_reader:
            print(row['city'])
            city_name = row['city']
            flat_type = row['Flat Type1']
            flat_type1 = row['Flat Type2']
            locality1 = row['Locality1']
            locality2 = row['Locality2']


    SIGNUP = (By.ID, 'commingSoonSignUp')
    SIGNUP_TEXT_ON_POPUP = (By.CLASS_NAME,'phone-verification-title')
    SIGNIN_WITH_PHONE = (By.ID,'contactNumber')
    CONTINUE_BUTTON = (By.ID, 'checkPhoneNumber')
    CITY_DROPDOWN = (By.CLASS_NAME, 'selectedcity')
    SEARCH_CITY_LIST = (By.XPATH, "//a[contains(text(), ""'" + city_name + "'"")]")
    INPUT_TEXT = (By.ID,'locationGoogle')
    LOCALITY_SEARCH = (By.ID, 'locationGoogleClickWrapper')
    BUY_BUTTON = (By.XPATH,'//button[contains(text(), "Buy")]')
    BHK = (By.CLASS_NAME,'nbBHKText')
    BHK_2 = (By.XPATH,"//label[@for = ""'" + flat_type + "'""]")
    BHK_3 = (By.XPATH,"//label[@for = ""'" + flat_type1 + "'""]")
    SELECT_LOCALITY1 = (By.XPATH, "//span[@class = 'normal-text'][contains(text(),""'" + locality1 + "'"")]")
    SELECT_LOCALITY2 = (By.XPATH, "//span[@class = 'normal-text'][contains(text(),""'" + locality2 + "'"")]")
    SEARCH_BUTTON = (By.CLASS_NAME,'icon-search')
    DESCRIPTION1 = "//a[@class = 'card-link-detail'][@href]"
    MINIMIZE_POPUP = (By.XPATH, '//div[@class = "card rent-property-card"][itemprop(text(),"description")]')  
    CHECK_DESCRIPTION_TAG = (By.ID, "shortDesc")
    CHECK_TAG = (By.XPATH, '//h4[@class = "normal-text"][contains(text(),"Flat Description")]')


class LoginPageLocators(object):
    LOGIN_BUTTON = (By.ID,'Login / Sign Up')
    EMAIL = (By.ID, 'ap_email')
    PASSWORD = (By.ID, 'ap_password')
    SUBMIT = (By.ID, 'signInSubmit-input')
    ERROR_MESSAGE = (By.ID, 'message_error')
