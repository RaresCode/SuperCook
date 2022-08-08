from pages.shoplist_page import ShopList
from behave import when, then

@when(u'I Tap on the shopping list category')
def tap_shopping_list(context):
    context.ShopList = ShopList(context.app)
    context.ShopList.click_shoplist()

@when(u'I type the ingredient name in the shop list search field')
def type_ingredient_name(context):
    context.ShopList.type_shoplist_ingredient()

@then(u'Ingredient will be visible in the shopping inlist section')
def get_ingredient_shoplist(context):
    ingredient = context.ShopList.verify_shoplist_ingredient_existence()
    context.Ingredients.closeapp()
    assert ingredient == "Found"
