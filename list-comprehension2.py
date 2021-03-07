numbers = []
for x in range(3):
    for y in range(3):
        numbers.append((x,y))

result = [(x,y)for x in range(3) for y in range(3)]
print(result)


prices = [1000,6200,1300,0,26,0,5000]
taxes = []
for x in prices:
    if (x >0):
        taxes.append(x*1.18)
        print(x)


taxes = [x*1.18 for x in prices if x>0]
taxes = [x*1.18 if x>0 else "tax cannot be calculated" for x in prices]
print(taxes)

numbers = [1,5,9,30,17,14]
result = []
for x in numbers:
    if (x%2==1):
        result.append(x)
        print(x)

result = [x for x in numbers if x%2==0]
result = [x if x%2==0 else "number is odd number." for x in numbers]
print(result)
