# Question: Write a Python program using a for loop to print the sum of all even numbers from 1 to 20.

sum = 0
for number in range(2, 21, 2):
    sum += number
print(f"The sum of all even numbers between 1 to 20 is {sum}")