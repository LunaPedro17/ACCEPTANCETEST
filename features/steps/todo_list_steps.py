from behave import given, when, then
from todo_list import ToDoList, Task

@given('I have an empty to-do list')
def step_impl(context):
    context.todo_list = ToDoList()

@given('my to-do list contains')
def step_impl(context):
    context.todo_list = ToDoList()
    for row in context.table:
        if 'Priority' in row.headings:
            context.todo_list.add_task(row['Task'], priority=row['Priority'])
        elif 'Status' in row.headings:
            task = Task(row['Task'], status=row['Status'])
            context.todo_list.tasks.append(task)
        else:
            context.todo_list.add_task(row['Task'])

@when('I add the task "{description}"')
def step_impl(context, description):
    context.todo_list.add_task(description)

@when('I add a new task "{description}" with "{priority}" priority')
def step_impl(context, description, priority):
    context.todo_list.add_task(description, priority=priority)

@when('I list all tasks')
def step_impl(context):
    context.output = "Tasks:\n" + "\n".join(
        f"{i+1}. {task}" for i, task in enumerate(context.todo_list.list_tasks())
    )

@when('I mark "{description}" as completed')
def step_impl(context, description):
    task = context.todo_list.find_task(description)
    assert task, f'Task "{description}" not found'
    context.mark_result = task.mark_completed()

@when('I try to mark "{description}" as completed')
def step_impl(context, description):
    context.success, context.result = context.todo_list.mark_task_completed(description)

@when('I clear the to-do list')
def step_impl(context):
    context.todo_list.clear_all_tasks()

@then('the to-do list should contain "{description}"')
def step_impl(context, description):
    task = context.todo_list.find_task(description)
    assert task is not None, f'Task "{description}" not found in the to-do list'

@then('the to-do list should contain task "{description}" with "{priority}" priority')
def step_impl(context, description, priority):
    task = context.todo_list.find_task(description)
    assert task is not None, f'Task "{description}" not found'
    assert task.priority == priority, f'Expected priority {priority}, got {task.priority}'

@then('the task "{description}" should show status "Completed"')
def step_impl(context, description):
    task = context.todo_list.find_task(description)
    assert task is not None, f'Task "{description}" not found'
    assert task.status == "Completed", f'Expected status Completed, got {task.status}'

@then('I should see the error "Task not found"')
def step_impl(context, message):
    assert not context.success, "Operation should have failed but succeeded"
    assert message in str(context.result), f'Expected error "{message}" but got "{context.result}"'

@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list.list_tasks()) == 0, "To-do list is not empty"

@then('I should see')
def step_impl(context):
    expected = "\n".join(line.strip() for line in context.text.strip().split('\n'))
    actual = "\n".join(line.strip() for line in context.output.strip().split('\n'))
    assert expected == actual, f'Expected:\n{expected}\n\nActual:\n{actual}'