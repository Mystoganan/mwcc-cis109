grocery_list = []

#Requirement 1 & 9
while(True):
    print("""Welcome to Your Shopping List! 
    
    Please make a selection from one of the following options:
    
    1. Add an item to the shopping list.
    2. Display the shopping list.
    3. Display the item count.
    4. Display the first item in the shopping list.
    5. Display the last item in the shopping list.
    6. Clear the shopping list.
    7. Exit""")
    
    selection = input("\nSelection: ")

    #Requirement 2
    if(selection == "1"): 
        item = input("Add your item: ")
        grocery_list.append(item)
        print("Item Added")
        input("Press [Enter] to Continue")

    #Requirement 3
    elif(selection == "2"):
        print(f"Grocery List: {grocery_list}")
        input("Press [Enter] to Continue")

    #Requirement 4
    elif(selection == "3"):
        print(f"The amount of items in your list is {len(grocery_list)}")
        input("Press [Enter] to Continue")

    #Requirement 5
    elif(selection == "4"):
        print(f"FIRST ITEM: {grocery_list[0]}")
        input("Press [Enter] to Continue")

    #Requirement 6
    elif(selection == "5"):
        print(f"LAST ITEM: {grocery_list[-1]}")
        input("Press [Enter] to Continue")

    #Requirement 7
    elif(selection == "6"):
        grocery_list = []
        print("Shopping List Cleared")
        input("Press [Enter] to Continue")

    #Exit Option
    elif(selection == "7"):
        input("Goodbye!\nPress [Enter] to Exit")
        break

    #requirement 8
    else:
        print(f"You entered an invalid option. \nRetry!")
        input("Press [Enter] to Retry")
