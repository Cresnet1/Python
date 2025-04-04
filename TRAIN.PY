#Ask the user for their PIN to access the ATM.
#If the PIN is correct, ask how much they want to withdraw.
#If they have enough balance, allow the withdrawal. Otherwise, show an error message.
#If the PIN is incorrect, deny access.


pin = 2020
balance = 0
ATM_CODE =int(input("Enter ATM Code"))
if ATM_CODE == pin:
    amount_diposited = 600
    balance += amount_diposited
    withdrawal =int(input("How much do you want to withdrawal"))
    newbalance = amount_diposited - withdrawal
else:
    print("Denied access") 
    exit()
if withdrawal<= 600 and withdrawal > 0:
        print(f"Witdrawal Successful! Your balance is {newbalance}")
else:
        print("Error")


        
