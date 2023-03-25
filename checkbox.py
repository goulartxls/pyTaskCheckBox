import os
import time
global Tasks 
global CheckBox
global Running
Running = True
Tasks = []
CheckBox = []
def RenderMenu(list):
    os.system('cls')
    print("-----------List----------")
    RenderTasks(list)
    print("-------------------------")
    print("1 - Add Task")
    print("2 - Finish Task")
    print("3 - Remove Task")
    print("0 - Exit")
def RenderTasks(list):
    if len(list) != 0:
        for position, task in enumerate(list):
            Check = ''
            if CheckBox[position] == False :
                Check = 'X'
            else:
                Check = '✓'
            print(f"{position + 1}  - {task} - [{Check}]")
    else: 
        print("No items in the list!")
def RemoveTask(index):
    Tasks.pop(index)
    CheckBox.pop(index)
def NewTask():
    NewTask = input("Inform the new task: ")
    Tasks.append(NewTask)
    CheckBox.append(False)
def CheckTask(index):
    CheckBox[index] = True
def Main():
    global Running
    RenderMenu(Tasks)
    choice = int(input("What you want to do : "))
    if choice == 1:
        NewTask()
    elif choice == 2:
        TaskChoice = int(input("Inform the new task: "))
        if (TaskChoice) <= len(Tasks):
            CheckTask(TaskChoice - 1)
        else:
            print("This choice not exist!")
    elif choice == 3:
        TaskIndex = int(input("Inform the new task: "))
        if (TaskIndex) <= len(Tasks):
            RemoveTask(TaskIndex - 1)
        else:
            print("This choice not exist!")
            time.sleep(2)
    elif choice == 0:
        Running = False
    else:
        print("Invalid choice!")
        time.sleep(2)
while True:
    if Running:
        Main()
    else:
        break