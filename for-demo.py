# 1)(?) Print each element in the list of numbers.

numbers = [1,2,3,4,5,10,15]
for n in numbers:
    print(n)

# 2)(?) Which numbers in the list of numbers are a multiple of 5?

for n in numbers:
    if (n %5 == 0):
        print(n)

# 3)(?) What is the sum of the numbers in the list of numbers?

total = 0
for n in numbers:
    total = total + n
print(total)

# 4)(?) Square the even numbers in the list of numbers.

for n in numbers:
    if(n%2==0):
        print(n,n*n)

# 5)(?) How many products are there with 'iphone' in the list of products?

products = ['iphone 8','iphone 7','iphone X','iphone XR','samsung S10']  

count = 0
for x in products:
    index = (x.find('iphone'))  
    if (index >-1 ):
        count += 1
print(count)   
        
