products = [
    {'name': 'samsung A10','price': 3200},
    {'name': 'samsung A30','price': 3900},
    {'name': 'samsung J8','price': 4200},
    {'name': 'iphone 8','price': 6000},
    {'name': 'iphone 8 plus','price': 7200},
    {'name': 'iphone 7','price': 3500},
    {'name': 'iphone 6','price': 2800},
    {'name': 'iphone 6 plus','price': 3300},
    {'name': 'iphone x','price': 8000},
    {'name': 'iphone 11','price': 9800}
    
]
# 1)(?) list all product information. 

for p in products:
    print(f"Name of the product: {p['name']} and the price of the product: {p['price']} TL")

# 2)(?) What is the total price of the products ? 

total = 0
for p in products:
    total = total +int(p['price'])
print(f'total price of products: {total} TL')

# 3)(?) Show products with a price maximum of 6000 products.

for p in products:
    if int(p['price']<=6000):
        print(f"products name: {p['name']} products price: {p['price']} TL")

# 4)(?) Find products that contain the keyword received from the user.

keyWord = input('the product you want to search: ')

for p in products:
    if (p['name'].find(keyWord.lower()) > -1):
        print(f"products name: {p['name']} products price: {p['price']} TL")
