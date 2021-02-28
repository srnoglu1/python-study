#fuel consumption cost calculation#

gasolinePrice = 6.69
dieselPrice = 5.86
totalFuelCost = 0

averageFuelConsumption = float(input('What is your average fuel consumption per 100 kilometers?: '))
theWayToGo = float(input('what is your travel distance?: '))
fuelType = input('what is your fuel type?: ')

averageFuelConsumption = theWayToGo * (averageFuelConsumption / 100)

if(fuelType == "gasoline"):
    totalFuelCost = gasolinePrice * averageFuelConsumption
elif (fuelType == "diesel"):
    totalFuelCost = dieselPrice * averageFuelConsumption
else:
    print('You entered the wrong fuel type.')

if (totalFuelCost != 0):
    print(totalFuelCost)
