Feature: Web Tables

  Scenario: Manage web table entries
    Given I am on the DemoQA homepage
    When I navigate to the Web Tables page
    And I create a new record
    And I edit the created record
    Then I should be able to delete the record
