"""VERSION 2 - ADD FUNCTIONS:
Set up combo data structure, Create add combo function,
Create search/edit function, Create delete function,
Create display menu function"""

import easygui


def display_menu(menu, prices):
    output = ""
    
    for combo_name, items in menu.items():
        total = 0
        
        for item in items:
            if item in prices:
                total += prices[item]
            else:
                easygui.msgbox(f"Warning: {item} has no price!")
        
        output += f"{combo_name}: {', '.join(items)} - Total: ${total:.2f}\n"
    
    easygui.msgbox(output, "Full Menu")


def add_combo(menu):
    name = easygui.enterbox("Enter combo name:")
    
    if not name:
        easygui.msgbox("Invalid name.")
        return
    
    items = easygui.enterbox("Enter items separated by commas:")
    
    if not items:
        easygui.msgbox("Invalid items.")
        return
    
    items_list = [item.strip() for item in items.split(",")]
    
    confirm = easygui.buttonbox(
        f"{name}: {items_list}\nIs this correct?",
        choices=["Yes", "No"]
    )
    
    if confirm == "Yes":
        menu[name] = items_list
        easygui.msgbox(f"{name} added successfully!")
    else:
        easygui.msgbox("Combo not added.")


def delete_combo(menu):
    name = easygui.enterbox("Enter combo name to delete:")
    
    if name in menu:
        confirm = easygui.buttonbox(
            f"Are you sure you want to delete {name}?",
            choices=["Yes", "No"]
        )
        
        if confirm == "Yes":
            del menu[name]
            easygui.msgbox("Combo deleted.")
    else:
        easygui.msgbox("Combo not found.")


def search_combo(menu):
    name = easygui.enterbox("Enter combo name to search/edit:")
    
    if name in menu:
        current = menu[name]
        
        choice = easygui.buttonbox(
            f"{name}: {', '.join(current)}",
            choices=["Edit", "Cancel"]
        )
        
        if choice == "Edit":
            new_items = easygui.enterbox("Enter new items (comma separated):")
            
            if new_items:
                menu[name] = [item.strip() for item in new_items.split(",")]
                easygui.msgbox("Combo updated!")
    else:
        easygui.msgbox("Combo not found.")


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
            "Select an option",
            choices=["Display Menu", "Add Combo", "Search/Edit", "Delete", "Exit"]
        )

        if choice == "Display Menu":
            display_menu(menu, prices)
        elif choice == "Add Combo":
            add_combo(menu)
        elif choice == "Search/Edit":
            search_combo(menu)
        elif choice == "Delete":
            delete_combo(menu)
        else:
            break


if __name__ == "__main__":
    main()