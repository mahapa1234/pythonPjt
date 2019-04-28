#Feature，Scenario，Given，When，Then等第一个字母大写的，这些都是关键字，不能变

Feature: Compute factorial#计算阶乘
  #备注，描述说明
  In order to play with Lettuce
  As beginners
  We'll implement factorial

  #场景1，就是第一个测试用例
  Scenario: Factorial of 0#0的阶乘
    Given I have the number 0
    When I compute its factorial
    Then I see the number 1

  Scenario: Factorial of 1
    Given I have the number 1
    When I compute its factorial
    Then I see the number 1

  Scenario: Factorial of 2
    Given I have the number 2
    When I compute its factorial
    Then I see the number 2

  Scenario: Factorial of 3
    Given I have the number 3
    When I compute its factorial
    Then I see the number 6
