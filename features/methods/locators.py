from selenium.webdriver.common.by import By


# Locators which will be used when interacting with various elements
class Locators(object):
    # INTRO
    SKIP_INTRO_BTN = (By.XPATH, "//*[@text='214.skip']")

    # SELECT INGREDIENTS THROUGH SEARCH INPUT
    SEARCH_INPUT = (By.CLASS_NAME, "android.widget.EditText")
    FIND_RESULTS_BOX = (By.XPATH, "//*[ends-with(@text, 'add')]")
    FIRST_RESULT_COORDONATES = (144, 575)
    
    # SELECT INGREDIENTS THROUGH THE CHECKBOXES MAIN SECTION
    SELECT_INGREDIENT_CB = (By.XPATH, "//*[@text='milk'][@index='3']")
    
    # PANTRY
    MY_PANTRY_BTN = (By.XPATH, "//*[starts-with(@text, 'My Pantry')][@clickable='true']")
    PANTRY_INGREDIENT_TEXT = (By.XPATH, "//*[@text='milk']")
    PANTRY_ADDSHOPLIST_COORDONATES = (822, 832)
    
    # DELETE INGREDIENT PASTRY SECTION
    DELETE_INGREDIENT_COORDONATES = (983, 823)
    
    # DELETE INGREDIENT MAIN SECTION
    MORE_OPTIONS_BTN = (By.XPATH, "//android.view.View/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[3]")
    REMOVE_ALL_INGREDIENTS = (515, 393)
    CONFIRM_REMOVE_BTN = (By.XPATH, "//*[@text='OK']")

    # SHOPLIST
    SHOPLIST_CATEGORY_BTN = (By.XPATH, "//*[@text='Shopping List']")
    SHOPLIST_INPUT = (By.CLASS_NAME, "android.widget.EditText")
    SHOPLIST_RESULTS_BOX = (By.XPATH, "//android.webkit.WebView/android.view.View/android.view.View[3]")
    SHOPLIST_FIRST_RESULT_COORDONATES = (144, 575)

    # CHANGE STATE OF INGREDIENTS IN SHOPLIST
    SHOPLIST_INLIST_BTN = (By.XPATH, "//*[contains(@text, 'milk')][@index='1']")
    SHOPLIST_FINISHED_TEXT = (By.XPATH, "//*[contains(@text, 'milk')][@index='2']")

    # RECIPES
    INGREDIENT_BUTTER_BTN = (By.XPATH, "//android.view.View[2]/android.view.View[6]/android.view.View[1]")
    INGREDIENT_MILK_BTN = (By.XPATH, "//*[@text='milk'][@index='3']")
    RECIPES_CATEGORY_BTN = (By.XPATH, "//*[@text='See Recipes'][@index='1']")
    RECIPES_SEEALL_BTN = (By.XPATH, "//android.view.View/android.view.View[1]/android.view.View[3]/android.view.View[5]")
    RECIPES_SEARCH_INPUT = (By.CLASS_NAME, "android.widget.EditText")
    RECIPES_FIRST_RESULT_COORDONATES = (144, 575)
    RECIPES_RESULTS_BOX = (By.XPATH, "//android.webkit.WebView/android.view.View/android.view.View[3]")
    RECIPES_NAME_TEXT = (By.XPATH, "//android.view.View[3]/android.view.View[2]/android.view.View[1][@text='Scrambled Eggs']")
    RECIPES_ENOUGH_INGREDIENTS_TEXT = (By.XPATH, "//android.view.View[3]/android.view.View[2]/android.view.View[4]")