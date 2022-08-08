from features.methods.main_methods import MainMethods
from features.methods.locators import Locators


class Pastry(MainMethods):
    
    # Set the mobile driver and get the available locators
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators
    
    # Open the pastry section
    def open_pastry(self):
        self.click_on_element(self.locator.MY_PANTRY_BTN)

    # Find the given ingredient in the pantry section, return it if found
    def find_ingredient(self):
        ingredient =  self.find_element_text(self.locator.PANTRY_INGREDIENT_TEXT)
        if ingredient != "milk":
            return "Not Found"
        else:
            return "Found"
    
    # Delete the ingredient available in the pantry section
    def pastry_delete_ingredient(self):
        self.tap_coordonates(self.locator.DELETE_INGREDIENT_COORDONATES)
    
    # Check if ingredient has successfully been deleted and not available in the dom
    def check_ingredient_deletion(self):
        ingredient =  self.find_element_absence(self.locator.PANTRY_INGREDIENT_TEXT)
        return ingredient
