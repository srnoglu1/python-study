# 1)(?) After getting her name from the user, check her age and education status to see if she can get a driver's license.
#   (!) User age must be at least 18 for driving license.
#   (?) User training for driver's license must be high school and above.

name = (input("Name: "))
surname = (input("Surname: "))
age = int(input("Age: "))
lisans = (input("what is your graduation?: "))

if (age >= 18):
    print("your age is sufficient to get a driver's license.")
    if (lisans=="highschool" or lisans=="university"):
        print("Your graduation knowledge is enough to get a driver's license.")
    else:
        print("Your graduation information is not enough to get a driver's license.")
else:
    print("your age is not enough to get a driver's license.")


# 2)(?) Take the written and verbal grades of the student and print the grade information corresponding to the grade range according to the calculated average.

written1 = float(input("Written1:"))
written2 = float(input("Written2:"))
verbal = float(input("Verbal:"))

result = (written1 + written2 + verbal ) /3
if (result >0) and (result<25):
    print(f'your exam average:{result} your grade: 0')
elif (result >25) and (result<45):
    print(f'your exam average:{result} your grade: 1')
elif (result >45) and (result<55):
    print(f'your exam average:{result} your grade: 2')
elif (result >55) and (result<70):
    print(f'your exam average:{result} your grade: 3')
elif (result >70) and (result<85):
    print(f'your exam average:{result} your grade: 4')
elif (result >85) and (result<=100):
    print(f'your exam average:{result} your grade: 4')
else:
    print("You entered incorrect information.")
