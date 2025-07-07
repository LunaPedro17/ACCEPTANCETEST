Feature: To-Do List Manager
  As a user
  I want to manage my tasks
  So I can organize my daily activities

  Background:
    Given I have an empty to-do list

  @happy_path
  Scenario: Add a basic task
    When I add the task "Buy milk"
    Then the to-do list should contain "Buy milk"

  @happy_path
  Scenario: Add a task with priority
    When I add a new task "Finish project" with "High" priority
    Then the to-do list should contain task "Finish project" with "High" priority

  @happy_path
  Scenario: List all tasks
    Given my to-do list contains:
      | Task          | Priority |
      | Buy groceries | Medium   |
      | Pay rent      | High     |
    When I list all tasks
    Then I should see:
      """
      Tasks:
      1. Buy groceries - Pending (Priority: Medium)
      2. Pay rent - Pending (Priority: High)
      """

  @happy_path
  Scenario: Mark task as completed
    Given my to-do list contains:
      | Task          | Status   |
      | Write report  | Pending  |
    When I mark "Write report" as completed
    Then the task "Write report" should show status "Completed"

  @edge_case
  Scenario: Try to complete non-existent task
    When I try to mark "Ghost task" as completed
    Then I should see the error "Task not found"

  @happy_path
  Scenario: Clear all tasks
    Given my to-do list contains:
      | Task          |
      | Call mom      |
      | Walk the dog  |
    When I clear the to-do list
    Then the to-do list should be empty