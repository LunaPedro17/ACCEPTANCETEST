from todo_list import ToDoList

def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Clear All Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date (optional, format YYYY-MM-DD): ") or None
            priority = input("Enter priority (High/Medium/Low, default Medium): ") or "Medium"
            todo_list.add_task(description, due_date, priority)
            print("Task added successfully!")
            
        elif choice == "2":
            tasks = todo_list.list_tasks()
            if not tasks:
                print("No tasks in the list.")
            else:
                print("\nTasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                    
        elif choice == "3":
            description = input("Enter task description to mark as completed: ")
            if todo_list.mark_task_completed(description):
                print("Task marked as completed!")
            else:
                print("Task not found.")
                
        elif choice == "4":
            todo_list.clear_all_tasks()
            print("All tasks cleared!")
            
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()