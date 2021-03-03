# 1)(?) Print the numbers you receive from the user on the screen in order.

numbers = []

x = 0

while (x<5):
    number = int(input('number: '))
    numbers.append(number)
    x +=1
numbers.sort()
print(numbers)

# 2)(?) Print the list of numbers on the screen.

numbers = [15,45,13,5,6,12,78,96]
x = 0

while (x<len(numbers)):
    numbers.sort()
    print(numbers[x])
    x += 1

# 3)(?) Retrieve start and end dates from user and print all odd numbers in between.

startDate = int(input("start date: "))
finish = int(input("finish date: "))
x = startDate
while x<finish:
    x+=1
    if x%2==1:
        print(x)

# 4)(?) Sort the numbers 1 to 100 in descending order.

x = 100
while x>0:
    print(x)
    x-=1
