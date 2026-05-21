print('''THIS IS TO DO LIST APP
Press 1 : if you want to add any new task
Press 2 : if you want to update any task
Press 3 : if you want to delete any task
Press 4 : if you want to show tasks''')

to_do_list = []

def add_task():
    task = input("Enter your new task : ")
    to_do_list.append({task : "Pending"})

def update_status():
    task_no = int(input("Enter which no of task, you want to update : "))
    status = input(f"what is your updated status for task no {task_no} : ")
    if task_no <= len(to_do_list):
        task = list(to_do_list[task_no-1].keys())[0]
        to_do_list[task_no-1][task] = status
    else:
        pass

def delete_task():
    delete_task = int(input("Enter which no of task, you want to delete : "))
    if delete_task <= len(to_do_list):
        to_do_list.pop(delete_task-1)
    else:
        pass

def show_tasks():
    print("\n============= YOUR TO DO LISTS 👇=============\n1")
    i = 0
    while (i < len(to_do_list)):
        task = list(to_do_list[i].keys())[0]
        status = to_do_list[i][task]
        if status == "done" or status == "Done":
            print(f"{i+1}. {task} - {status}✅")
        else:
            print(f"{i+1}. {task} - {status}⏳")
        i += 1
    print("\n==============================================\n")

while True:
    try:
        user_input = int(input("What do you want to do : "))
        if(user_input == 1):
            while True:
                add_more_task = int(input('''Do you want to add more task?
Press 1, otherwise Press 2 : '''))
                if(add_more_task == 1):
                    add_task()
                elif(add_more_task == 2):
                    show_tasks()
                    break
                else:
                    break

        elif(user_input == 2):
            while True:    
                update_more_task = int(input('''Do you want to update more task?
Press 1, otherwise Press 2 : '''))
                if(update_more_task == 1):
                    update_status()
                elif(update_more_task == 2):
                    show_tasks()
                    break
                else:
                    show_tasks()
                    break

        elif(user_input == 3):
            while True:    
                delete_more_task = int(input('''Do you want to delete more task?
Press 1, otherwise Press 2 : '''))
                if(delete_more_task == 1):
                    delete_task()
                elif(delete_more_task == 2):
                    show_tasks()
                    break
                else:
                    show_tasks()
                    break

        elif(user_input == 4):
            show_tasks()

    except Exception as Value_error:
        print("Enter valid number between 1 to 4")