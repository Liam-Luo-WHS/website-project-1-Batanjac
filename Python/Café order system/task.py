menu_items = ["Coffee", "Tea", "Muffin", "Sandwich"] 
prices = [3.5, 2.5, 4.0, 6.0]

print("Welcome to the café! ")
name = input("What is your name? ")
print("This is our menu:")
print(menu_items[0], "-", prices[0]) #Figure out how to shorten this
print(menu_items[1], "-", prices[1])
print(menu_items[2], "-", prices[2])
print(menu_items[3], "-", prices[3])
total_cost = []

for item in menu_items:

    order = input("What would you like to order? ")
    if order == menu_items:
        total_cost.append(int(menu_items.values())) #Figure out how to get the price of the menu item as the total cost
        print(order + " added to your order.")
    elif order != menu_items:
        print("This isn't on the menu.")
    elif order == "Exit":
        print(total_cost)
        break