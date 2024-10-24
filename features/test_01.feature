# features/test01.feature

Feature: Button click functionality
  This feature verifies that the button click works correctly.

  Scenario: Click product management and view WebView
    Given the app is launched
    When I click the product management button
    Then I should see the WebView and click it