#create a list to store the list of things in it

list = []
#a loop to keep the program running
while True:
    print("\nType","\ndone:to save and exit","\nadd:to add something to the list","\nremove: to take something out\n")#instructions to help the user
    
    inst_input = input("pick one: ")#ask the user to pick one so the computer know what do with the item
    if inst_input == "done":#This is to exit when the user type in done
        task_input = input("did you finish the task(y/n): ")
        if task_input == "y":
            print("Good job!")
            break
        else:
            print("you sure")
            continue
#This is allow the computer to choice what to do with the item
    if inst_input == "add":
        user_input = input("what do you want to add to the list: ")
        list.append(user_input)
        print("\n",list,"\n")

    elif inst_input == "remove":
        user_input = input("what do you want to remove from the list: ")
        if user_input in list:
            list.remove(user_input)
            print("\n",list,"\n")
        else:
            print("\nThat's not in the list")
    else:
        print("\nPick: add,remove or done")
#print the list at the end so the user know what to do
print("\n",list)




