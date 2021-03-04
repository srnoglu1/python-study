product = []
x = 0
number = int(input("How many product information do you want to enter?: "))
while (x<number):
    name = input("Name of the product: ")
    price = input("The price of the product: ")
    product.append({
        "Name of the product" : name,
        "The price of the product" : price
    })
    x += 1
for p in product:
    print(f"Name of the product: {p['Name of the product']} The price of the product: {p['The price of the product']}")
