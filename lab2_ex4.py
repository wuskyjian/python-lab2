#  Exercise 4


def find_urgent_tasks(dictionaries):
    urgent_tasks = {}
    if not isinstance(dictionaries, dict):
        print("Wrong input parameter!")
        return 1

    for (key, value) in dictionaries.items():
        if value["urgent"]:
            urgent_tasks[key] = value

    return urgent_tasks


def print_2d_dictionary(dictionaries):
    for (key, value) in dictionaries.items():
        print(key + ":", value)


tasks = {
    'task1': {'todo': 'call John for AmI project organization', 'urgent': True},
    'task2': {'todo': 'buy a new mouse', 'urgent': True},
    'task3': {'todo': 'find a present for Angelina’s birthday', 'urgent': False},
    'task4': {'todo': 'organize mega party (last week of April)', 'urgent': False},
    'task5': {'todo': 'book summer holidays', 'urgent': False},
    'task6': {'todo': 'whatsapp Mary for a coffee', 'urgent': False}
}

print("The original tasks are:")
print_2d_dictionary(tasks)

print("\nThe urgent tasks are:")
print_2d_dictionary(find_urgent_tasks(tasks))
