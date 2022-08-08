from behave import when
    
@when(u'I tap on the desired ingredient from the available categories')
def tap_wanted_ingredient(context):
    context.Ingredients.select_ingredient()
