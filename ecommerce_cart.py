def calculate_price(cart):
    if len(cart) == 0:
        print("your cart is empty please enter some items")
    total = sum(cart.values())
    if len(cart) > 5:
        total *= 0.1
    print("Total price:",total)

cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
calculate_price(cart_items)