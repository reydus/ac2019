#download website 

modules = open("modules.txt", "r")
modules = modules.read()

print(modules)

print("aa")
print(type(modules))
input()

a= modules.split()
modules = []
fuel = []
for i in a:
    modules.append(int(i))

for i in modules:
    i = (float(i)/3)//1 -2
    a = i//1
    fuel.append(a)

sum = 0

for i in fuel:
    sum += i

print(sum)

#print(modules)
input()

