Feature: Tests with login page

Scenario: Login with incorrect credentials
  Given I am on ebay login page
  When I write email and password and click Sign in button
  Then I should see Oops in error message


Scenario: Check login page title
  Given I am on ebay main page
  When I click sign in button
  Then I should see Sign in or Register | eBay title
