Feature: Test of the recipe section

    Scenario: Find a recipe with the choosen ingredients
        Given I open the app
        And I skip intro
        When I Select milk and butter as ingredients
        And I Open all recipes
        And I search for scrambled eggs in the search field
        Then The recipe that match my available ingredients will be displayed
