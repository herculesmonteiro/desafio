Feature: Sortable Items

  Scenario: Sort items in ascending order
    Given I am on the DemoQA homepage
    When I navigate to the Sortable page
    Then I should be able to sort the items in ascending order using drag and drop
