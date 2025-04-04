# Online Python - IDE, Editor, Compiler, Interpreter

def Add_sum():
  numbers = int(input("Enter number:"))
  num =  int(input("Enter number:"))
  sum = numbers + num
  print("sum is ", sum)

Add_sum()



def add_sum(a, b):
    return a + b 
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

result = add_sum(num1, num2)
print("The sum is :", result)



















def validation(pin):
    passcode = "1234"
    if passcode == pin:
        print("Success")
    else:
        print("Incorrect PIN. Try again.")
        new_pin = input("Enter your PIN: ")
        return validation(new_pin)
        
validation("*151#")