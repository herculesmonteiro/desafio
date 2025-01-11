Feature: Practice Form

  Scenario: Fill and submit practice form
    Given I am on the DemoQA homepage
    When I navigate to the Practice Form page
    And I fill the form with data from a text file
    And I submit the form
    Then a popup should appear
    And I should be able to close the popup
