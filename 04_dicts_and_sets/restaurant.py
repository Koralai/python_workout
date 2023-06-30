MENU = {
    'bubble tea': 4,
    'herbal tea': 2,
    'coffee': 3,
    'espresso': 4,
    'latte': 4,
    'muffin': 4,
    'scone': 3,
    'breakfast burrito': 8,
    'fruit cup': 4,
    'yogurt parfait': 3
}

def get_str_from_list(list_str):
    """
    Format a list of strings using commas and 'and' before the last string in the list
    """    
    output = ''
    for item in list_str:
        if item != list_str[-1]:
            output += f"{item}, "
        else:
            output += f"and {item}"
            
    return output

def take_order(menu):
    """
    Take user input for items ordered from the menu. Keep a running
    total of the cost of the user's order.
    """
    print("Welcome to our cafe! Press 'enter' at any time to quit.\n")
    
    price = 0
    items_ordered = []
    
    while True:
        order = input("What would you like to order? ")
        if not order:
            break
        if order not in menu:
            print("Sorry, that's not available.\n")
        else:
            price += menu[order]
            items_ordered.append(order)
    
    price_message = (f"You have ordered {get_str_from_list(items_ordered)}. " 
                     f"Your total is ${price:.2f}.")
    
    if price > 0:
        return price_message
    return None
        

print(take_order(MENU))
     