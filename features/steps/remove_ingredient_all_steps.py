from behave import when

@when(u'I tap on more options')
def more_options(context):
    context.Ingredients.press_more_options()

@when(u'I Press on remove all ingredients')
def remove_all_ingredients(context):
    context.Ingredients.press_remove_ingredients()

@when(u'I Press on OK button')
def confirm_deletion(context):
    context.Ingredients.press_confirm_remove()
