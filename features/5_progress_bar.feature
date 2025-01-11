Feature: Progress Bar

  Scenario: Control progress bar
    Given I am on the DemoQA homepage
    When I navigate to the Progress Bar page
    And I start the progress bar
    And I stop the progress bar before 25%
    Then the progress value should be less than or equal to 25%
    When I restart and complete the progress bar
    Then I should be able to reset the progress bar
