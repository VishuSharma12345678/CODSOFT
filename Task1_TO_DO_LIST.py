def task():
    tasks = [] 
    print("Welcome to the To-Do Application!")

    total_task = int(input("How many tasks do you want to add? "))
    for i in range(1,total_task+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    
    print(f"Your tasks are\n{tasks}")

    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop: "))
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task {add} has been successfully added...")

        elif operation == 2:
            updated_val = input("Enter the task you want to update:")
            if updated_val in tasks:
                up = input("Enter new task:")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Updated task {updated_val} to {up} successfully...")
            else:
                print(f"Task '{updated_val}' not found in the list.")

        elif operation == 3:
            del_val = input("Enter the task you want to delete:")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Deleted task {del_val} successfully...")
            else:
                print(f"Task '{del_val}' not found in the list.")

        elif operation == 4:
            print(f"Total tasks = {tasks}")

        elif operation == 5:
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid operation. Please try again.")

if __name__ == "__main__":
    task()