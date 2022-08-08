from behave import when, then

@when(u'I Press on the delete button of the ingredient')
def delete_ingredient(context):
    context.Pastry.pastry_delete_ingredient()

@then(u'The ingredient will be successfully removed from the pantry section')
def check_ingredient(context):
    ingredient = context.Pastry.check_ingredient_deletion()
    context.Ingredients.closeapp()
    assert ingredient == "Ingredient Removed"