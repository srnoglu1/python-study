a, b, c = 2, 5, 12

# 1- What is the difference between the product of the two numbers you get from the user and the sum a, b, c ?
x = int(input("x: "))
y = int(input("y: "))

result = (x * y) - (a+b+c)

# 2- Calculate the part of c without remainder to b ?
result = c // b

# 3- What is mod 3 of the sum of a, b, c ?

result = (a+b+c) % 3

# 4- What is mod 3 of the sum of a, c, b ?
result = b ** a

# 5- a,*b,c what is the cube of C according to the operation of numbers ?
numbers = 1, 5, 7, 10, 3
a, *b, c = numbers
print(c ** 3)

# 6- a, *b, c what is the sum of the values of b according to the number operation? ?
a, *b, c = numbers
print(b[0] + b[1] + b[2])
