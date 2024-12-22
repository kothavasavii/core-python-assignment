def add_item(list, elem):
    list.append(elem)

def remove_item(list, elem):
    if availability(list, elem):
        list.remove(elem)
    else:
        print("The item to be removed is not available")

def availability(list, elem):
    if elem in list:
        return True

l = ["Pizza", "Burger", "Pasta", "Salad"]
print("initial_menu =",l)

add = input("add_item = ")
add_item(l, add)

remove = input("remove_item = ")
remove_item(l, remove)

check = input("check_item = ")
print("updated menu = ", l)
if availability(l, check):
    print('Availability: "', check, 'is available"')
else:
    print('Availability:"', check, 'is not available"')
