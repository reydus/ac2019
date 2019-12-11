#download website 

modules = open("modules.txt", "r")
modules = modules.read()

print(modules)

print("aa")
print(type(modules))

a= modules.split()
modules = []
fuel = []
for i in a:
    modules.append(int(i))

for i in modules:
    i = (float(i)/3)//1 -2
    a = i//1
    fuel.append(a)

def get_fuel_of_fuel(fuel):
    summation = 0
    fuel_of_fuel = (float(fuel)/3)//1 -2
    while fuel_of_fuel > 0:
        summation += fuel_of_fuel
        print("Summ is "+str(fuel_of_fuel))
        fuel_of_fuel = (float(fuel_of_fuel)/3)//1 -2
    return summation


print("Basic fuel req is "+str(fuel))

added_fuel = fuel

for i in range(0, len(fuel)):
    fuelForGood = get_fuel_of_fuel(fuel[i])
    fuel[i] += fuelForGood

print("Fuel accounted for fuel is "+str(fuel))

# sum everything
theGreatSummation = 0
for i in fuel:
    theGreatSummation += i

print("Finally, the sum of fuel for fuel is "+str(theGreatSummation))

'''
sum = 0

for i in fuel:
    sum += i

cachee = sum
for i in range(0,len(fuel)):
    #fuel[i] = 33583
    newish = (float(fuel[i])/3)//1 -2
    summation = 0
    while newish > 0:
        summation += newish
        print("extra fuel is "+str(newish))
        print("summation is "+str(summation))
        newish = (float(newish)/3)//1 -2
    fuel[i] += summation
    print("FUEL IS "+str(fuel[i]))

for i in fuel:
    sum += i


print(sum)
print(cachee)
#threshold = input("select threshold")

#difference = 100
#sum = 1969
fuel_of_fuel = (float(sum)/3)//1 -2
extra = 0


while fuel_of_fuel > 0:
    #old_fuel = sum
    print("extra fuel is "+str(fuel_of_fuel))
    extra += fuel_of_fuel
    fuel_of_fuel = (float(fuel_of_fuel)/3)//1 -2

print("fuel of fuel is")

print(sum)
print(extra)
input()
'''