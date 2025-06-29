# List of Tasks , 4 Different options
#1. Add a new task
#2. Show tasks
#3. Mark task as done
#4. Exit
#------------------------

# suzdavane na opciite

def add_new_task(message:str, tasks:list):
    tasks.append(message )
    print("New Note added!")


def show_tasks(tasks:list):
    counter = 1
    for task in tasks:
        print(f"{counter}: {task}")
        counter+=1

def mark_as_done(index:int, tasks:list):
    message = tasks[index-1]
    if "✔" not in message:
        tasks[index-1] += " ✔"

options = (
            "1.Add new task",
            "2.Show tasks" ,
            "3.Mark task as done",
            "4.Exit" )
notes = []
print(options)
choice = int(input("Enter a choice? 1/2/3/4: "))
while choice!=4:
    if choice == 1:

        message = input("Note: ")
        add_new_task(message,notes)
    elif choice ==2:
        show_tasks(notes)
    elif choice == 3:
        print(notes)
        print("Which note do you want to mark as Done?")
        index = int(input(("Type the number: ")))
        mark_as_done(index,notes)

    print(options)
    choice = int(input("Enter a choice? 1/2/3/4: "))
for number,value in enumerate(notes):
    print(f"{number}: {value}")
print("You stopped the program! Goodbye :)")