t = int(input("How many items do you want to add?: "))
grocery = []
for i in range(t):
    item = input("What is the name of your item?: ")
    grocery.append(item)

print(grocery)