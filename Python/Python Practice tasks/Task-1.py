#Grocery list manager

grocery_list = []
item_count = 0

amount = int(input("How many items do you want to add? "))


for count in range(amount):
    list = input(f"Enter item {item_count+1} ")
    grocery_list.append(list)
    item_count += 1


if item_count == amount:
    remove = input("Do you want to remove an item? (Yes/No) ")
    if remove == "Yes":
        removed_item = input("Enter item to remove: ")
        try:
            if removed_item == grocery_list: #Solve this
                grocery_list.remove(removed_item)
                print(grocery_list)
        except:
            print("That isn't in the grocery list.")
    else:
        print("Shopping list: ", grocery_list)
