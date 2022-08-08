from pages.ingredients_page import Ingredients
from pages.pastry_page import Pastry
from methods.get_driver import OpenApp
from behave import given, when, then

@given(u'I open the app')
def open_app(context):
    context.app = OpenApp().get_driver()
    context.Ingredients = Ingredients(context.app)

@given(u'I skip intro')
def skip_intro(context):
    context.Ingredients.intro_load()
    context.Ingredients.press_skip_intro()
    
@when(u'I type the ingredient name in the search field')
def type_ingredient_name(context):
    context.Ingredients.search_for()

@when(u'I Tap on the desired ingredient displayed after the search')
def tap_first_result(context):
    context.Ingredients.open_first_result()

@when(u'I Press on My Pantry')
def press_on_pastry(context):
    context.Pastry = Pastry(context.app)
    context.Pastry.open_pastry()

@then(u'Ingredient will be visible in the pantry section')
def get_ingredient(context):
    ingredient = context.Pastry.find_ingredient()
    context.Ingredients.closeapp()
    assert ingredient == "Found"
