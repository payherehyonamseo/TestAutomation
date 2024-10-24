# features/click_button.feature

Feature: Button click functionality
  This feature verifies that the button click works correctly.

  Scenario: Button click test
    Given I have launched the app
    When I click the product management button
    Then I should see the sound button