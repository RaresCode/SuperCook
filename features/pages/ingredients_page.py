from features.methods.main_methods import MainMethods
from features.methods.locators import intro
from features.methods.locators import ingredients_section


class Ingredients(MainMethods):

    # Set the mobile driver and get the available locators
    def __init__(self, driver):
        super().__init__(driver)
        self.intro = intro
        self.ingredients = ingredients_section
    
    # Wait for intro to load
    def intro_load(self):
        self.wait_intro_load(self.intro.SKIP_INTRO_BTN)
    
    # Press skip intro
    def press_skip_intro(self):
        self.click_on_element(self.intro.SKIP_INTRO_BTN)
    
    # Ingredient addition section
    
    # Search for an ingredient in the search field, click on the field and wait for result box to load to avoid errors
    def search_for(self):
        self.click_on_element(self.ingredients.SEARCH_INPUT)
        self.input(self.ingredients.SEARCH_INPUT, "milk")
        self.find_element(self.ingredients.FIND_RESULTS_BOX)
    
    # Select ingredient checkbox
    def select_ingredient(self):
        self.click_on_element(self.ingredients.SELECT_INGREDIENT_CB)
    
    # Select all ingredients required for a recipe
    def select_all_ingredients(self):
        self.click_on_element(self.ingredients.INGREDIENT_BUTTER_BTN)
        self.click_on_element(self.ingredients.INGREDIENT_MILK_BTN)

    # Tap on the first result displayed by the result box, by coordonates
    def open_first_result(self):
        self.tap_coordonates(self.ingredients.FIRST_RESULT_COORDONATES)
        
    # Ingredient removal section
    
    # Press on more options on the main page 
    def press_more_options(self):
        self.click_on_element(self.ingredients.MORE_OPTIONS_BTN)
    
    # Press on remove all ingredients button on main page
    def press_remove_ingredients(self):
        self.tap_coordonates(self.ingredients.REMOVE_ALL_INGREDIENTS)
    
    # Press on confirm to remove all ingredients
    def press_confirm_remove(self):
        self.click_on_element(self.ingredients.CONFIRM_REMOVE_BTN)

    # Close the app
    def closeapp(self):
        self.driver.close_app()
    


