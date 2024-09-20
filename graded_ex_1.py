# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def display_sorted_products(products_list, sort_order):
    sorted_list = sorted(products_list, key=lambda x: x[1], reverse=(sort_order == 2))
    display_products(sorted_list)

def display_products(products_list):
    for index, (product, price) in enumerate(products_list, start=1):
        print(f"{index}. {product} - ${price:.2f}")

def display_categories():
    for index, category in enumerate(products.keys(), start=1):
        print(f"{index}. {category}")
    return len(products)

def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    total_cost = 0
    for product, quantity in cart:
        cost = product[1] * quantity
        total_cost += cost
        print(f"{product[0]} - ${product[1]:.2f} x {quantity} = ${cost:.2f}")
    print(f"Total cost: ${total_cost:.2f}")

def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Customer: {name}")
    print(f"Email: {email}")
    print("Items Purchased:")
    for product, quantity in cart:
        print(f"{quantity} x {product[0]} - ${product[1]:.2f} = ${product[1] * quantity:.2f}")
    print(f"Total: ${total_cost:.2f}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days.")
    print("Payment will be accepted upon delivery.")

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    if "@" not in email or email.count("@") != 1:
        return False
    username, domain = email.split("@")
    return username and "." in domain and domain.count(".") >= 1

def main():
    name = input("Enter your name (First Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name (First Last).")
        name = input("Enter your name (First Last): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email address: ")

    cart = []
    while True:
        print("\nAvailable Categories:")
        display_categories()
        category_choice = input("Select a category by number (or 'exit' to finish shopping): ")
        if category_choice.lower() == 'exit':
            break
        try:
            category_choice = int(category_choice)
            categories = list(products.keys())
            selected_category = categories[category_choice - 1]
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")
            continue

        print(f"\nProducts in {selected_category}:")
        display_products(products[selected_category])
       
        while True:
            print("\nOptions:")
            print("1. Select a product to buy")
            print("2. Sort the products according to the price")
            print("3. Go back to the category selection")
            print("4. Finish shopping")
            option = input("Select an option by number: ")

            if option == '1':
                product_choice = input("Enter the product number to buy: ")
                try:
                    product_choice = int(product_choice)
                    product = products[selected_category][product_choice - 1]
                    quantity = input("Enter the quantity you want to buy: ")
                    if not quantity.isdigit() or int(quantity) <= 0:
                        print("Invalid quantity. Please enter a positive number.")
                        continue
                    quantity = int(quantity)
                    add_to_cart(cart, product, quantity)
                    print(f"Added {quantity} of {product[0]} to your cart.")
                except (ValueError, IndexError):
                    print("Invalid choice. Please try again.")

            elif option == '2':
                sort_order = input("Sort by price (1 for ascending, 2 for descending): ")
                if sort_order in ['1', '2']:
                    display_sorted_products(products[selected_category], sort_order)
                else:
                    print("Invalid choice. Please try again.")

            elif option == '3':
                break
           
            elif option == '4':
                if cart:
                    total_cost = sum(product[1] * quantity for product, quantity in cart)
                    address = input("Enter your delivery address: ")
                    display_cart(cart)
                    generate_receipt(name, email, cart, total_cost, address)
                else:
                    print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                return

            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
