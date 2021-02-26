#1)(?) Which of the 2 numbers entered is greater?

number1 = int(input("number1: "))
number2 = int(input("number2: "))

result = number1 > number2
print(f'{number1} {number2} "is greater than: "{result}')

#2)(?) Ask for password and email information and check their accuracy?
_email = "emir236@gmail.com"
_password = "159951"

email = input("email: ")
password = input("password: ")

isEmail = (email.lower().split() == _email)
isPassword = (password.split() == _password)
print(f'"email accuracy:"{isEmail} "and password accuracy: "{isPassword}')

#3)(?) Print whether a number entered is odd or even?

numbers = int(input("number: "))

result = (numbers % 2 == 0) 
print(f'{numbers} "is even number: " {result}')

#4)(?) Take 2 visa (60%) and final (40%) grades from the user and calculate the average. if the average is 50 or more, print the one that failed.

exam1 = float(input("visa1: "))
exam2 = float(input("visa2: "))
final = float(input("final: "))

average = (((exam1+exam2) *0.6)/2) + (final *0.4)
print(f'"exam average: " {average} "average validity status: "{average >= 50}')
