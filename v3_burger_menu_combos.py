"""VERSION 3 - LAST TOUCHES:
Add input validation, Refine UI"""

import easygui


def display_menu(menu, prices):
    if not menu:
        easygui.msgbox("Menu is empty.")
        return

    output = ""
    
    for combo_name, items in menu.items():
        total = 0
        
        for item in items:
            if item in prices:
                total += prices[item]
        
        output += f"{combo_name}: {', '.join(items)}\nTotal: ${total:.2f}\n\n"
    
    easygui.msgbox(output, "Full Menu")


def get_valid_combo_name(menu, prompt):
    while True:
        name = easygui.enterbox(prompt)
        
        if name is None:
            return None
        
        name = name.strip()
        
        if name == "":
            easygui.msgbox("Name cannot be empty.")
        else:
            return name


def get_valid_items(prices):
    while True:
        items = easygui.enterbox(
            f"Enter items separated by commas.\nAvailable items:\n{', '.join(prices.keys())}"
        )
        
        if items is None:
            return None
        
        items_list = [item.strip() for item in items.split(",")]
        
        # Check for empty input
        if not any(items_list):
            easygui.msgbox("You must enter at least one item.")
            continue
        
        # Check all items exist
        invalid_items = [item for item in items_list if item not in prices]
        
        if invalid_items:
            easygui.msgbox(f"Invalid items: {', '.join(invalid_items)}")
        else:
            return items_list


def add_combo(menu, prices):
    name = get_valid_combo_name(menu, "Enter combo name:")
    if name is None:
        return
    
    if name in menu:
        easygui.msgbox("Combo already exists.")
        return
    
    items_list = get_valid_items(prices)
    if items_list is None:
        return
    
    confirm = easygui.buttonbox(
        f"{name}: {', '.join(items_list)}\nIs this correct?",
        choices=["Yes", "No"]
    )
    
    if confirm == "Yes":
        menu[name] = items_list
        easygui.msgbox(f"{name} added successfully!")
    else:
        easygui.msgbox("Combo not added.")


def delete_combo(menu):
    if not menu:
        easygui.msgbox("Menu is empty.")
        return

    name = easygui.choicebox("Select combo to delete:", choices=list(menu.keys()))
    
    if name:
        confirm = easygui.buttonbox(
            f"Are you sure you want to delete {name}?",
            choices=["Yes", "No"]
        )
        
        if confirm == "Yes":
            del menu[name]
            easygui.msgbox("Combo deleted.")


def search_combo(menu, prices):
    if not menu:
        easygui.msgbox("Menu is empty.")
        return

    name = easygui.choicebox("Select combo to view/edit:", choices=list(menu.keys()))
    
    if name:
        current = menu[name]
        
        choice = easygui.buttonbox(
            f"{name}: {', '.join(current)}",
            choices=["Edit", "Cancel"]
        )
        
        if choice == "Edit":
            new_items = get_valid_items(prices)
            
            if new_items:
                menu[name] = new_items
                easygui.msgbox("Combo updated!")


def main():
    menu = {
        "Value": ["Beef Burger", "Fries", "Fizzy Drink"],
        "Cheezy": ["Cheeseburger", "Fries", "Fizzy Drink"],
        "Super": ["Cheeseburger", "Large Fries", "Smoothie"]
    }

    prices = {
        "Beef Burger": 5.69,
        "Cheeseburger": 6.69,
        "Fries": 1.00,
        "Fizzy Drink": 1.00,
        "Smoothie": 2.00,
        "Large Fries": 2.00
    }

    while True:
        choice = easygui.buttonbox(
            "Burger Combo Manager",
            choices=["Display Menu", "Add Combo", "Search/Edit", "Delete", "Exit"]
        )

        if choice == "Display Menu":
            display_menu(menu, prices)
        elif choice == "Add Combo":
            add_combo(menu, prices)
        elif choice == "Search/Edit":
            search_combo(menu, prices)
        elif choice == "Delete":
            delete_combo(menu)
        else:
            easygui.msgbox("Goodbye!")
            break


if __name__ == "__main__":
    main()