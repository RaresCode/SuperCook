Feature: Test of ingredient removal from pantry

    Background: common steps
        Given I open the app
        And I skip intro

    Scenario: Remove the unwanted ingredient from pantry
        When I tap on the desired ingredient from the available categories
        And I Press on My Pantry
        And I Press on the delete button of the ingredient
        Then The ingredient will be successfully removed from the pantry section

    Scenario: Remove ingredient available in the pantry
        When I tap on the desired ingredient from the available categories
        And I tap on more options
        And I Press on remove all ingredients
        And I Press on OK button
        And I Press on My Pantry
        Then The ingredient will be successfully removed from the pantry section
    