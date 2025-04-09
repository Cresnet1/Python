def greet():
    print("Hi")
    print("Lorraine")

greet()
greet()

def show_balance():
    pass

def deposit():
    pass
def withdraw():
    pass

balance = 0
is_running = True


while is_running:
    print("Banking Progress")
    print("1.Show balance")
    print("2. deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter your choice(1,4): ")

    if choice == "1":
        show_balance()
    elif choice == "2":
         deposit () 
    elif choice == "3":
         withdraw()
    elif choice == "4":
        is_running = False
    else:
        print("That is not a valid choice")  







#Exercise: Greeting Function
#Problem Statement
#Create a Python function named greet_user that takes a single parameter, name, which is a string. The function should return a greeting message that incorporates the user's name.
#Steps to Complete the Exercise:
#1. Define the Function:
#Create a function called greet_user that accepts one argument.
#2. Build the Greeting Message:
#Within the function, use the input parameter to construct a message in the format:
#"Hello, [name]! Welcome to Python programming."
#3. Return the Message:
#Ensure that your function returns the greeting message.
#4. Test Your Function:
#Call the function with different names (e.g., "Alice", "Bob") and print the results to verify that it works correctly.






def greet_user(name):
    print(f"Hello, {name} welcome to python programming.")

greet_user("Lorraine")
greet_user("Tawanda")
greet_user("Kendra")




#Exercise: Find the Maximum of Three Numbers

#Problem Statement

#Write a function called find_max that takes three numbers as arguments and returns the largest number among them.

#Steps to Complete the Exercise:

#1. Define the function find_max(num1, num2, num3).


#2. Compare the three numbers to determine the largest.


#3. Return the largest number as the result.


#4. Test your function by calling it with different values and printing the results


 
def find_max(num1, num2, num3):
    return max(num1, num2, num3)
print(find_max(12,30,45))




def total_fruits(apples, bananas, oranges):
    Total = apples + bananas + oranges
    return Total
    print(Total)
print(total_fruits(3,6,7))

    





      

