from features.methods.main_methods import MainMethods
from features.methods.locators import Locators
import time


class ShopList(MainMethods):
    
    # Set the mobile driver and get the available locators
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators
        
    '''
    Because the input box on shopping list and the one on the main page are the same 
    we will need to wait for that one to dissapear from dom
    first before finding the one from the shopping list
    '''

    # Click on shoplist button and wait for the input field from the main page to dissapear from dom
    def click_shoplist(self):
        self.click_on_element(self.locator.SHOPLIST_CATEGORY_BTN)
        time.sleep(5)
    
    # Type ingredient name and click on it, wait for the result dropdown to load
    def type_shoplist_ingredient(self):
        self.find_element(self.locator.SEARCH_INPUT)
        self.click_on_element(self.locator.SHOPLIST_INPUT)
        self.input(self.locator.SHOPLIST_INPUT, "coconut milk")
        self.find_element(self.locator.SHOPLIST_RESULTS_BOX)
    
    # Select ingredient by coordonates
    def select_shoplist_ingredient(self):
        self.tap_coordonates(self.locator.SHOPLIST_FIRST_RESULT_COORDONATES)
    
    # Verify if the ingredient has been added to the list sucessfully
    def verify_shoplist_ingredient_existence(self):
        ingredient = self.find_element_text(self.locator.SHOPLIST_INLIST_BTN)
        if ingredient != "coconut milk":
            return "Not Found"
        else:
            return "Found"
    
    # Mark the ingredient as bought by clicking on it
    def click_shoplist_ingredient(self):
        self.click_on_element(self.locator.SHOPLIST_INLIST_BTN)
    
    # Verify if the ingredient has been sucessfully added to the finished/bought section
    def verify_shoplist_ingredient_state(self):
        ingredient = self.find_element_text(self.locator.SHOPLIST_FINISHED_TEXT)
        if ingredient != "coconut milk":
            return "Not Found"
        else:
            return "Found"
    