tasks = [] # store tasks using list
Filename = "tasks.txt" # saving tasks to a file

def load():
    try:
        with open(Filename, "r") as file: # read
            for line in file:
                tasks.append(line.strip()) # edit spacing
    except FileNotFoundError:
        pass

def save():
    with open(Filename, "w") as file: # write 
        for task in tasks:
            file.write(task + "\n") #new line

def showmenu():
    print( "TO-DO LIST MENU") 
    print("1. Add Task") 
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Remove Task")
    print("5. Save Tasks")
    print("6. Exit")

def add():
    name = input("Enter a new task: ")
    tasks.append(name)
    print("Task added.")

def view():
    if len(tasks) == 0:
        print("No tasks found.")
        return  # if something is wrong, it stops
    print("Your Tasks:")
    for i, task in enumerate(tasks, 1): # looked up enumerate to number tasks and to have the names.
        print(f"{i}. {task}")

def complete():
    view()
    if len(tasks) == 0:
        return
    option = input("Enter task number to mark as completed: ")
    try:
        number = int(option)
    except ValueError: #inputs that are not integers are accounted for
        print("Error.")
        return
    if number < 1 or number > len(tasks): # makes sure the number is valid
        print("Error.")
        return
    tasks[number - 1] = tasks[number - 1] + " (Completed)"
    print("Task completed.")

def delete():
    view()
    if len(tasks) == 0:
        return #
    option = input("Enter task number to delete: ")
    try:
        number = int(option)
    except ValueError:
        print("Error.")
        return
    if number < 1 or number > len(tasks):
        print("Error.")
        return
    removed = tasks.pop(number - 1) # remove task from list
    print("Removed:", removed)

if __name__ == "__main__": #
    load()
    run = True
    while run: 
        showmenu()
        option = input("What would you like to do? ")
        if option == "1":
            add()
        elif option == "2":
            view()
        elif option == "3":
            complete()
        elif option == "4":
            delete()
        elif option == "5":
            save()
            print("Saved.")
        elif option == "6":
            save()
            print("Enjoy your day!")
            running = False # exit the loop
        else:
            print("Error.")