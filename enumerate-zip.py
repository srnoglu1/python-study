#zip#

list1 = [1,2,3,4,5,]
list2 = ["a","b","c","d","e"]

for item in zip (list1,list2):
    print(item)


#enumerate#

brands = ["Audi","Mercedes","Bmw"]

for index,value in enumerate(brands):
    print(f"{index+1}-{value}")
