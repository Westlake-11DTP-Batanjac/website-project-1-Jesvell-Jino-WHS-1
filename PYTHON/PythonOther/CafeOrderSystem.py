customerName = ""
customerOrder = []
customerTotal = 0
menuItems = ["Coffee","Tea","Sandwhich","Bread","Muffin", "Combo Deal: Muffin & Tea","Combo Deal: 10 Breads"]
menuPrices = [3.2, 2, 5.99, 5, 2.5, 4, 30]

while True:
    print("~~Welcome to Jesvell's Café!~~")
    customerName = input("What is your name?: ")
    print("Here is our menu:")

    for i in range(len(menuItems)):
        print(str((i + 1)) + ". " + menuItems[i] + " - $" + str(menuPrices[i]))

    while True:
        ask = int(input("What would you like to order?(Number): "))
        ask -= 1

        if menuItems[ask]:
            customerOrder.append(ask)
            customerTotal += menuPrices[ask]

        ask = input("Would you like to order again?: ")
        if ask.lower() != "yes":
            break

    print("--- Reciept for " + customerName + " ---")
    for i in customerOrder:
        print(menuItems[i] + " - $" + str(menuPrices[i]))

    if customerTotal > 20:
        customerTotal -= int(customerTotal * 0.10)

        print("10% Discount for being over 20$")

    print("Total: $" + str(customerTotal))
    print("Thank you for ordering at Code Café!")