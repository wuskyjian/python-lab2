#  Exercise 1

print("""
Insert the number corresponding to the action you want to perform: 

   1. insert a new task; 
   2. remove a task; 
   3. show all the tasks; 
   4. close the program. 
""")

choice = '-1'
task = []

while True:
    choice = input("Your choice: ")
    if choice == '1':
        task_insert = input("Please enter one task: ")
        task.append(task_insert)
        print("Task:\"", task_insert, "\"is inserted.")

    elif choice == '2':
        task_removed = input("Please enter the task you want to remove: ")
        if task_removed in task:
            task.remove(task_removed)
            print("Task:\"", task_removed, "\"is removed.")
        else:
            print("Task doesn't exist.")

    elif choice == '3':
        print("The whole task list is:", sorted(task))

    elif choice == '4':
        print("Program closed.")
        break

    else:
        print("""
        Wrong input, please follow the input rules

        1. insert a new task; 
        2. remove a task; 
        3. show all the tasks; 
        4. close the program. 
        """)
