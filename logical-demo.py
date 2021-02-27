# 1)(?) Check if a entered number is between 50-100 .
number = int(input("number: "))

result = (number >50) and (number<100)
print(f'{number} "The number is between 50 and 100." {result}')


# 2)(?) Check whether a number entered is an odd positive number.

number = int(input("number: "))
result = (number>0) and (number %2 == 1)
print("the number entered is a positive odd number.",result)


# 3)(?) Compare the 3 numbers entered in terms of magnitudes.

# a = (input("1: "))
# b = (input("2: "))
# c = (input("3: "))

# result = (a>b) and (a>c)
# print("a is the largest number.",result) 
# result = (b>a) and (b>c)
# print("b is the largest number.",result) 
# result = (c>a) and (c>b)
# print("c is the largest number.",result) 



# 4)(?) Check login with username and password information.

_username = "srnoglu"
_password = "199841"

username = (input("user name: "))
password = (input("password: "))

result = (username == _username) and (password == _password)
print("the user information entered is correct." ,result)


# 5)(?) Take 2 visa (60%) and final (40%) grades from the user and calculate the average. if the average is 50 or more, print the one that failed.
    #A(?) When 70 is taken from the final, the average does not matter.

exam1 = float(input("visa1: "))
exam2 = float(input("visa2: "))
final = float(input("final: "))

average = (((exam1+exam2) *0.6)/2) + (final *0.4)
print(f'"exam average: " {average} "average validity status: "{average >= 50}')
result = ("final grade is invalid: ", final>=50)
result = (average >=50) or (final >=70)
result = (f'"average validity status: "{average} "and passing state: " {final >=50 }')
print(result)


# 6)(?) Take the name, weight and height information of the person and calculate their weight indexes.

name = (input("Name : "))
weight = float(input("weight: "))
length = float(input("length: "))

weightIndex = (weight / length **2)
weak = (weightIndex >= 0) and (weightIndex <= 18.4)
normal = (weightIndex >= 18.4) and (weightIndex <= 24.9)
overweight = (weightIndex >= 24.9) and (weightIndex <= 29.9)
obese = (weightIndex >= 29.9) and (weightIndex <= 34.9)

print(f'"Name: " {name} "your weight index: " {weightIndex} "and your weight rating is poor: "{weak}')
print(f'"Name: " {name} "your weight index: " {weightIndex} "and your weight is normal: "{normal}')
print(f'"Name: " {name} "your weight index: " {weightIndex} "and your weight is overweight: "{overweight}')
print(f'"Name: " {name} "your weight index: " {weightIndex} "and your weight is on the brink of obesity: "{obese}')
