Feature: Test of ingredient addition to pantry

    Background: common steps
        Given I open the app 
        And I skip intro

    Scenario: Add ingredient to pantry through manual entry
        When I type the ingredient name in the search field
        And I Tap on the desired ingredient displayed after the search
        And I Press on My Pantry
        Then Ingredient will be visible in the pantry section

    Scenario: Add ingredient to pantry through manual item picking 
        When I tap on the desired ingredient from the available categories
        And I Press on My Pantry
        Then Ingredient will be visible in the pantry section
