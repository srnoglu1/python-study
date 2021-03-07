name = ["Ahmet","Mehmet","Aslı","Burcu","Kemal"]
string = "Hello 123456 World"
years = [1972,1985,1998,2003]
degree = [1,7,5,3,-4,-7,0,-12]

#1)(?) According to the air temperature information in the "degree" list, print the frost danger for the negative value.

result = [x if x>0 else "icing hazard !" for x in degree]
print(result)

#2)(?) Make a list of age information for each year of birth in the "years" array.

import datetime
now = datetime.datetime.now().year
result = [now - year for year in years]
print(result)

#3)(?) Create a list containing the numbers in the given "string".

result = [x for x in string if x.isdigit()]
print(result)

#4)(?) Convert each name in the list of names to lowercase.

result = [x.lower() for x in name ]
print(result)

#5)(?) Create a list of numbers between "1-100" that can be divided into 12.

result = [x for x in range(1,101) if x%3==0 if x%4==0]
print(result)
