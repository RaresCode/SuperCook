Feature: Test of shoplist inlist and finished sections

    Background: common steps
        Given I open the app 
        And I skip intro

    Scenario: Add ingredients to inlist shop list section
        When I Tap on the shopping list category
        And I type the ingredient name in the shop list search field
        And I Tap on the desired ingredient displayed after the search
        Then Ingredient will be visible in the shopping inlist section

    Scenario: Add ingredients to finished shop list section
        When I Tap on the shopping list category
        And I type the ingredient name in the shop list search field
        And I Tap on the desired ingredient displayed after the search
        And I Tap on the ingredient to switch it to the finished section
        Then Ingredient will be visible in the shopping finished section
