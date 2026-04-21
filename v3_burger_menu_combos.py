"""VERSION 3 - LAST TOUCHES:
Add input validation, Refine UI, Add order function"""

import easygui

def display_menu(menu, prices):
    if not menu:
        easygui.msgbox("Menu is empty.")
        return
    output = ""
    for combo_name, items in menu.items():
        total = sum(prices[item] for item in items)
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
        if not any(items_list):
            easygui.msgbox("You must enter at least one item.")
            continue
        invalid = [item for item in items_list if item not in prices]
        if invalid:
            easygui.msgbox(f"Invalid items: {', '.join(invalid)}")
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

def detect_auto_combo(selected_items, menu):
    """Return combo name if selected items match a combo exactly."""
    for combo_name, combo_items in menu.items():
        if sorted(combo_items) == sorted(selected_items):
            return combo_name
    return None

def order_food(menu, prices):
    # Step 1: Choose combos
    combo_choices = easygui.multchoicebox(
        "Select combos to order:",
        choices=list(menu.keys())
    )
    if combo_choices is None:
        return
    item_choices = easygui.multchoicebox(
        "Select individual items:",
        choices=list(prices.keys())
    )
    if item_choices is None:
        return
    auto_combo = detect_auto_combo(item_choices, menu)
    if auto_combo:
        convert = easygui.buttonbox(
            f"You selected items that match the '{auto_combo}' combo.\n"
            "Convert items into this combo?",
            choices=["Yes", "No"]
        )
        if convert == "Yes":
            combo_choices.append(auto_combo)
            item_choices = []

    total = 0
    order_summary = "ORDER SUMMARY:\n\n"
    for combo in combo_choices:
        items = menu[combo]
        price = sum(prices[item] for item in items)
        total += price
        order_summary += f"{combo} Combo: ${price:.2f}\n"
    for item in item_choices:
        total += prices[item]
        order_summary += f"{item}: ${prices[item]:.2f}\n"
    order_summary += f"\nTOTAL: ${total:.2f}"
    easygui.msgbox(order_summary, "Order Complete")

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
            choices=["Display Menu", "Add Combo", "Search/Edit", "Delete", "Order", "Exit"]
        )

        if choice == "Display Menu":
            display_menu(menu, prices)
        elif choice == "Add Combo":
            add_combo(menu, prices)
        elif choice == "Search/Edit":
            search_combo(menu, prices)
        elif choice == "Delete":
            delete_combo(menu)
        elif choice == "Order":
            order_food(menu, prices)
        else:
            easygui.msgbox("Goodbye!")
            break

if __name__ == "__main__":
    main()