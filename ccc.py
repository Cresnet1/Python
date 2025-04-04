pin = "1995"
balance = 0  
recharge_pin = input("Enter your recharge PIN: ")

if recharge_pin == "*153#":  
    amount_recharged = 100  
    balance += amount_recharged
    print(f"Recharge successful! Your new balance is ${balance}")
else:
    print("Invalid recharge PIN. Please try again.")
    exit()

print("\nEcoCash Menu:")
print("1. Send Money\n2. Make Payment\n3. Cash Out\n4. Airtime and Bundle\n5. Diaspora Services\n6. Financial Services\n7. Wallet Services\n8. Banking Services")
option = input("Select an option (1 to 8): ")

if option == "1":
    recipient = input("Enter recipient phone number: ") 
    amount = int(input("Enter amount: "))

    if amount <= 0:
        print("Invalid amount. Please enter a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        entered_pin = input("Enter your PIN to confirm transaction: ")
        if entered_pin == pin:
            balance -= amount
            print(f"Transaction successful! You sent ${amount} to Tiffany Hardish.")
            print(f"New balance: ${balance}")
        else:
            print("Incorrect PIN. Transaction failed.")

elif option == "3":  
    print("\n1. Cash-out - From agent\n2. Cash-out - From ATM")
    cashout_option = input("Select an option (1 or 2): ")
    
    if cashout_option in ["1", "2"]:
        amount = int(input("Enter amount to withdraw: "))
        
        if amount <= 0:
            print("Invalid amount. Please enter a valid amount.")
        elif amount > balance:
            print("Insufficient balance.")
        else:
            entered_pin = input("Enter your PIN to confirm transaction: ")
            if entered_pin == pin:
                balance -= amount
                print(f"Cash-out successful! You Successfuly send ${amount} to Tiffant Hardish.")
                print(f"New balance: ${balance}")
            else:
                print("Incorrect PIN. Transaction failed.")
    else:
        print("Invalid cash-out option. Please try again.")

else:
    print("Invalid option. Please try again.")

print("Thank you for using EcoCash!")