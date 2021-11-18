# Created by dldam at 11/18/2021
Feature: User inputs year of birth

  Scenario Outline: User inputs valid range, no given step, implies user is asked for year
    When user gives "<year>"
    Then "<year>" will be returned

    Examples: Valid range
      | year |
      | 1900 |
      | 2999 |


  Scenario Outline: User inputs invalid range, no given step, implies user is asked for year
    When user give "<year>"
    Then ValueError will be returned

    Examples: Invalid range
      | year |
      | 1899 |
      | 3000 |