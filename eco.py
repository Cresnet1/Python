pin = "1995"
balance = 0  
recharge_pin = input("Enter your recharge PIN : ")

if recharge_pin ==  "*153#":  
    amount_recharged = 100  
    balance += amount_recharged
    
else:
    print("Invalid recharge PIN. Please try again.")
    exit()

print("\nEcoCash Menu:\n1. Send Money\n2.Make Payment\n3.Cash Out\n4.Airtime ans Bundle\n5.Diaspora Services\n6.Financial Services\n7.Wallet Services\n8.Banking Services")
option = input("Select an option (1 to 8): ")

if option == "1":
     recipient = input("Enter recipient phone number: ") 
     amount = input("Enter amount")

elif option == "3":  
    Please_Select = input("\n1.Cash-out - From agent\n2.Cash-out - From ATM: ")
    Option = input("Select an option(1 or 2): ")
    
    if "amount" <= 0:
        print("Invalid amount. Please enter a valid amount.")
    elif "amount" > balance:
        print("Insufficient balance.")
    else:
        entered_pin = input("Enter your PIN to confirm transaction: ")
        
        if entered_pin == pin:
            balance -= "amount"
            print(f"Transaction successful! You sent ${"amount"} to  Tiffany Hardish.")
            print(f"New balance: ${balance}")
        else:
            print("Incorrect PIN. Transaction failed.")
else:
    print("Invalid option. Please try again.")

print("Thank you for using EcoCash!") 