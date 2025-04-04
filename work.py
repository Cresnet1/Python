Number = int(input("Enter a number: "))
if Number > 0:
    if Number % 2 == 0:
        print("The number is positive and even.")
    else:
        print("The number is positive and odd.")
elif Number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
