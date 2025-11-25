print("Welcome to the Grocery Store")
items = ["bananas", "apples", "raw steak", "orange juice", "eggs", "rotisserie chicken", "rice", "loaf of bread" ]
prices = [1.75, 1.5, 4.75, 2.5, 3.5, 10.99, 6.5, 4, 2]
cart = {}

check = False
while not check:
    for i in range(len(items)):
        print(f"{items[i]} - ${prices[i]:}")
    
    print("1. Add to cart")
    print("2. Remove from cart")
    print("3. View cart")
    print("4. Checkout")
    option = input("Choose an option (or type 'quit' to exit): ")

    if option == "1":
        name = input("Enter item: ")
        if name in items:
            amt = int(input("Amount: "))
            cart[name] = cart.get(name, 0) + amt
            print(f"Added {amt} {name} to cart.")
        else:
            print("Out of Stock.")

    elif option == "2":
        name = input("Enter item to remove: ")
        if name in cart:
            amt = int(input("Quantity to remove: "))
            if amt >= cart[name]:
                del cart[name]
            else:
                cart[name] -= amt
            print(f"Removed {amt} {name} from cart.")
        else:
            print("Item not in cart.")

    elif option == "3":
        print("Your cart:")
        for item, amt in cart.items():
            print(f"{amt} x {item}")

    elif option == "4":
        subtotal = sum(prices[items.index(item)] * amt for item, amt in cart.items())
        tax = subtotal * 0.06
        total = subtotal + tax
        print(f"Subtotal: ${subtotal:}")
        print(f"Tax: ${tax:}")
        print(f"Total: ${total:}")
        check = True

    elif option == "quit":
        check = True
        print("Thank you for visiting the Grocery Store!")