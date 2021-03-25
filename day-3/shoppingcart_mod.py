def shopping_cart():
    print("Hello and welcome to your shopping cart!")
    #creates empty dictionary to be used as cart
    cart = {}
    
    #Tried to stylize the print-outputs to resemble a list (border to the left, top and bottom)
    while True:
        add_another = True
        # Ask the user four bits of input: Do you want to : Show/Add/Remove or Quit?
        current_choice = (input("What do you want to do next?(Show/Add/Edit/Remove or Quit): ")).lower()
        #if user returns Quit, loop will break and return current cart
        if current_choice == 'quit':
            print("You are closing your cart, here was your cart upon closing:")
            break
        #checks to see if the item the user input is already present, if so prompts them 
        elif current_choice in cart:
            print(f"You already have {current_choice} in your cart, maybe try 'Edit' option?")
        #if user returns 'show', it will check if dict is empty
        elif current_choice == 'show':
            #if cart is empty, advises user of same
            if cart == {}:
                print("Your cart is currently empty!")
            #if cart is NOT empty, shows current content
            else:
                print(f"Here is your current cart:")
                print("____________")
                for key, value in cart.items():
                    print(f"|{key.title()} -- Qty: {value}")
                print("____________")
        #if user selects 'add', prompts user for item to add and then quantity of item 
        elif current_choice == 'add':
            item = input("Enter Item to Add: ")
            #checks to see if the item the user input to add is already present, if so prompts them
            if item in cart:
                print(f"You already have {current_choice} in your cart, maybe try 'Edit' option?")
            else:
                quantity = input("Enter Quantity: ")
                cart[item] = quantity
            #prompts user if they'd like to add another, so user does not have to type 'add' each time
                while add_another == True:
                    repeat_add = input("Add another?(Y/N): ")
                    if repeat_add.lower() == 'y' or repeat_add.lower() == 'yes':
                        item = input("Enter Item to Add: ")
                        if item in cart:
                            print(f"You already have {current_choice} in your cart, maybe try 'Edit' option?")
                            add_another = False
                        else:
                            quantity = input("Enter Quantity: ")
                            cart[item] = quantity
                    #breaks out of 'add another' while loop once user inputs anything other than y/yes
                    else:
                        add_another = False
        #if user inputs 'edit', it will allow them to change quantity of an item in the list. 
        elif current_choice == 'edit':
            print(f"Here is your current cart:")
            print("____________")
            for key, value in cart.items():
                print(f"|{key.title()}-- Qty: {value}")
            print("____________")
            item_to_change = (input("What item would you like to change the quantity of?: ")).lower()
            #checks if item user is trying to edit is in cart/dictionary
            if item_to_change in cart:
            #checks if quantity they want to change to is greater than 0, if 0 it will REMOVE item from dict/cart
            #if it is greater than zero, updates qty for corresponding item
                quantity_change = input("New Quantity (enter 0 to delete): ")
                if int(quantity_change) > 0:
                    cart[item_to_change] = quantity_change
                elif int(quantity_change) == 0:
                    del cart[item_to_change]
            else:
                print("Sorry, we did not find that item in your cart.")
        #if user inputs 'remove', it will show current cart and prompt user which item they want to remove
        elif current_choice == 'remove':
            print(f"Here is your current cart:")
            print("____________")
            for key, value in cart.items():
                print(f"|{key.title()}-- Qty: {value}")
            print("____________")
            remove_item = input("What item would you like to remove?: ")
            del cart[remove_item]
        #advises user input not recognized, if they input something other than valid: show/add/edit/remove or quit
        else:
            print("Sorry, please enter a valid input: Show/Add/Edit/Remove or Quit")
    #once user quits, prints final copy of cart/dictionary
    print("____________")
    for key, value in cart.items():
        print(f"|{key.title()}-- Qty: {value}")
    print("____________")
                