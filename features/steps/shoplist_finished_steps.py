from behave import when, then

@when(u'I Tap on the ingredient to switch it to the finished section')
def type_ingredient_name(context):
    context.ShopList.click_shoplist_ingredient()

@then(u'Ingredient will be visible in the shopping finished section')
def get_ingredient_shoplist(context):
    ingredient = context.ShopList.verify_shoplist_ingredient_state()
    context.Ingredients.closeapp()
    assert ingredient == "Found"
