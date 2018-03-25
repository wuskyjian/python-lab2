#  Exercise 2 and 3

from sys import argv
# Open file
script, filename = argv
file = open(filename, "r+")

# Initialize variables
choice = '-1'

# Read file
task = file.readlines()

print("""
Insert the number corresponding to the action you want to perform: 

   1. insert a new task; 
   2. remove a task; 
   3. show all the tasks; 
   4. remove tasks contain key word.
   5. close the program;
""")

while True:
    choice = input("Your choice: ")
    if choice == '1':
        task_insert = input("Please enter one task: ")
        task.append(task_insert + "\n")
        print("Task:\"", task_insert, "\"is inserted.")

    elif choice == '2':
        task_removed = input("Please enter the task you want to remove: ") + "\n"
        if task_removed in task:
            task.remove(task_removed)
            print("Task is removed.")
        else:
            print("Task doesn't exist.")

    elif choice == '3':
        number = 1
        print("The whole task list is:\n")
        for line in sorted(task):
            print(str(number) + ":", line)
            number += 1

    elif choice == '4':
        key_word = input("Please enter the key word:")
        for t in task:
            if key_word in t:
                task.remove(t)
                print("Task:\n", t, "\n is removed")

    elif choice == '5':
        # Clear the file
        file.seek(0)
        file.truncate()
        # Write tasks
        for t in task:
            file.write(t)
        file.close()
        print("Program closed.")
        break

    else:
        print("""
        Wrong input, please follow the input rules

        1. insert a new task; 
        2. remove a task; 
        3. show all the tasks; 
        4. remove tasks contain key word.
        5. close the program;
        """)
