list1 =[10,8,30,12,4,56]
numbers = []

for i in list1:
    i *= 2
    numbers.append(i)
    print(i)

name = ["Ahmet","Mehmet","Gonca","Başak","Elif"]

result = [c.upper() for c in name]
result = [str(number) for number in list1]
result = [i.lower() for i in name]
print(result)
