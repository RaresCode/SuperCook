from features.methods.main_methods import MainMethods
from features.methods.locators import Locators
import time


class Recipes(MainMethods):

    # Set the mobile driver and get the available locators
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locators
    
    # Open the recipes category
    def open_recipes(self):
        self.click_on_element(self.locator.RECIPES_CATEGORY_BTN)
    
    '''
    Because the input box on recipes list and the one on the main page are the same 
    we will need to wait for that one to dissapear from dom
    first before finding the one from the shopping list
    '''
    
    # Show all recipes and wait for the input box in the main page to dissapear from dom
    def show_all_recipes(self):
        self.click_on_element(self.locator.RECIPES_SEEALL_BTN)
        time.sleep(5)
    
    # Type the recipe name in the input box, click on it to load the results and wait for the results dropdown to load
    def type_recipe_name(self):
        self.click_on_element(self.locator.RECIPES_SEARCH_INPUT)
        self.input(self.locator.RECIPES_SEARCH_INPUT, "scrambled eggs")
        self.find_element(self.locator.RECIPES_RESULTS_BOX)
    
    # Select first recipe by tapping on coordonates
    def select_first_recipe_entry(self):
        self.tap_coordonates(self.locator.RECIPES_FIRST_RESULT_COORDONATES)
    
    # Check If there is a recipe that it's available with the given search term and also the ingredients are available
    def get_match_recipe(self):
        recipe_name = self.find_element_text(self.locator.RECIPES_NAME_TEXT)
        recipe_availability = self.find_element_text(self.locator.RECIPES_ENOUGH_INGREDIENTS_TEXT)
        if recipe_name == "Scrambled Eggs" and recipe_availability.startswith("You have") == True:
            return "Recipe available with the current ingredients"
        else:
            return "There are no recipe available with the current ingredients"