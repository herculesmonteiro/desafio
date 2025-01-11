Feature: Browser Windows

  Scenario: Open and close new window
    Given I am on the DemoQA homepage
    When I navigate to the Browser Windows page
    And I click on the New Window button
    Then a new window should open
    And I should be able to close the new window
