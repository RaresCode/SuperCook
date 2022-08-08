from pages.recipes_page import Recipes
from behave import when, then

@when(u'I Select milk and butter as ingredients')
def select_all_ingredients(context):
    context.Ingredients.select_all_ingredients()

@when(u'I Open all recipes')
def open_recipes_category(context):
    context.Recipes = Recipes(context.app)
    context.Recipes.open_recipes()
    context.Recipes.show_all_recipes()

@when(u'I search for scrambled eggs in the search field')
def select_dish(context):
    context.Recipes.type_recipe_name()
    context.Recipes.select_first_recipe_entry()

@then(u'The recipe that match my available ingredients will be displayed')
def get_recipe(context):
    match_recipe = context.Recipes.get_match_recipe()
    context.Ingredients.closeapp()
    assert match_recipe == "Recipe available with the current ingredients"