Feature: Web Tables

  Scenario: Create and delete 12 records
    Given I am on the Web Tables page
    When I create 12 new records
    Then I should see 12 new records in the table
    When I delete all 12 records
    Then the table should be empty
