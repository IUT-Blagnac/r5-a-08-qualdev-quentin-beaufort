Feature: Is it Friday yet?
  Everybody wants to know when it's Friday

  Scenario Outline:
    Examples:
      | day  | answer |
      | Friday | TGIF |
      | Sunday | Nope |
      | anything else! | Nope
    Given today is {day}
    When I ask whether it's Friday yet
    Then I should be told {answer}