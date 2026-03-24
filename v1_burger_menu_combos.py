"""VERSION 1 - BASIC STRUCTURE: Add menu info, import easygui"""

import easygui
def main():
    menu = {
        "Beef Burger": 5.69,
        "Chesseburger": 6.69,
        "Fries": 1.00,
        "Fizzy Drink": 1.00,
        "Smoothie": 2.00,
        "Large Fries": 2.00
    }
    combo1 = ["Beef Burger", "Fries", "Fizzy Drink"]
    combo2 = ["Cheeseburger", "Fries", "Fizzy Drink"]
    combo3 = ["Cheeseburger", "Large Fries", "Smoothie"]

    easygui.msgbox("Menu:")
    for item, price in menu.items():
        easygui.msgbox(f"{item}: ${price:.2f}")

    easygui.msgbox("\nCombos:")
    easygui.msgbox("Combo 1: " + ", ".join(combo1))
    easygui.msgbox("Combo 2: " + ", ".join(combo2))
    easygui.msgbox("Combo 3: " + ", ".join(combo3))

main()