def to_do_list():
    tasks = []

    numbers = int(input("Enter the number of tasks: "))    #5

    for i in range(1, numbers + 1):   # 1 - 5
        task = input(f"Enter the {i} task : ")
        tasks.append(task)
    
    while True:
        operations = int(input("\n 1-ADD \n 2-UPDATE \n 3-DELETE \n 4-VIEW \n 5-EXIT\n Choose anyone in the above; "))
        if operations == 1:
            add = input("Enter the name of the task to add in your to-do list : ")
            tasks.append(add)
            print(f"The {add} is successfully added to your to-do list...!")

        elif operations == 2:
            update = input("Enter the task name to update : ")
            if update in tasks:
                update_task = input("Enter the new task name :")
                ind = tasks.index(update)
                tasks[ind] = update_task
                print(f"Updated task : {update_task}")

        elif operations == 3:
            delete = input("Enter the name of the task to be deleted: ")
            if delete in tasks:
                ind = tasks.index(delete)
                del tasks[ind]
                print(f"The {delete} is deleted from the to-do list")

        elif operations == 4:
            print(f"Total tasks: {tasks}")

        elif operations == 5:
            print("Closing the program....!")
            break

        else:
            print("Invalid input! please enter a valid input.")

to_do_list()
        
