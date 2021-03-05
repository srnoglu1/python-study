#continue#

x = 0
total = 0

while (x <= 100):
    x+=1
    if (x%2==1):
        continue
    total += x
print(f'"Toplam: "{total}') 

#range#

for r in range(100,200):
    if (r %2==0):
        print(r)
