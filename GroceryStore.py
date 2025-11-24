print("Welcome to the Grocery Store")
items = ["bananas", "apples", "raw steak", "orange juice", "eggs", "rotisserie chicken", "rice", "loaf of bread" ]
prices = [1.75, 1.5, 4.75, 2.5, 3.5, 10.99, 6.5, 4, 2]
cart = {}

check = False
while not check:
    for i in range(len(items)):
        print(f"{items[i]} - ${prices[i]:.2f}")
    
    print("1. Add to cart")
    print("2. Remove from cart")
    print("3. View cart")
    print("4. Checkout")
    option = input("Choose an option (or type 'quit' to exit): ")

    if option == "1":
        name = input("Enter item to add: ")
        if name in items:
            qty = int(input("Quantity: "))
            cart[name] = cart.get(name, 0) + qty
            print(f"Added {qty} {name} to cart.")
        else:
            print("Item not found.")

    elif option == "2":
        name = input("Enter item to remove: ")
        if name in cart:
            qty = int(input("Quantity to remove: "))
            if qty >= cart[name]:
                del cart[name]
            else:
                cart[name] -= qty
            print(f"Removed {qty} {name} from cart.")
        else:
            print("Item not in cart.")

    elif option == "3":
        print("Your cart:")
        for item, qty in cart.items():
            print(f"{qty} x {item}")

    elif option == "4":
        subtotal = sum(prices[items.index(item)] * qty for item, qty in cart.items())
        tax = subtotal * 0.06
        total = subtotal + tax
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${total:.2f}")
        check = True

    elif option == "quit":
        check = True