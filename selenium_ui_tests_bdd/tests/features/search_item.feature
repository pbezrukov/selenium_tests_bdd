Feature: Tests with search pages
  Scenario Outline: Test with search of items
    Given I am on ebay main page
    When I write <text> in textbox field
    And Click on search button
    Then I should see <text>
    And Sum of prices of the first 10 found items should be more 1000$

    Examples:
    |          text          |
    | Astronomical Telescope |
    |        iPhone          |