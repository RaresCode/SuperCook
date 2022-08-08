from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


# Main methods used when interacting with the elements
class MainMethods():

    # Initialize the app and set the webdriverwait
    def __init__(self, driver):
        self.driver = driver
        self.WebDriverWait = WebDriverWait(self.driver, 20)
    
    # Wait until the app loaded the intro
    def wait_intro_load(self, locator):
        # time.sleep(5)
        self.WebDriverWait.until_not(EC.text_to_be_present_in_element_value((locator), '214.skip'))

    # Wait until the given element is not visible anymore
    def find_element_absence(self, locator):
        try:
            self.WebDriverWait.until(EC.invisibility_of_element_located((locator)))
        except TimeoutException:
            return "Ingredient Not Removed"
        else:
            return "Ingredient Removed"

    # Find the given element if it's visible
    def find_element(self, locator):
        self.WebDriverWait.until(EC.visibility_of_element_located((locator)))

    # Find the given element text if it's visible
    def find_element_text(self, locator):
        return self.WebDriverWait.until(EC.visibility_of_element_located((locator))).text
    
    # Click on the given element if it's clickable
    def click_on_element(self, locator):
        self.WebDriverWait.until(EC.element_to_be_clickable((locator))).click()
    
    # Tap on the given coordonates, mostly used in cases where there is no proper element to click on
    def tap_coordonates(self, coordonates):
        self.driver.tap([coordonates])

    # Input a text into an element, clear the field and also click on it for proper load of the input boxes
    def input(self, locator, text):
        element_input = self.WebDriverWait.until(EC.visibility_of_element_located((locator)))
        element_input.clear()
        element_input.send_keys(text)
        
    # Close the app
    def closeapp(self):
        self.driver.close_app()
