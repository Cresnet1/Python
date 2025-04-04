count = 0
for number in range(1,20):
   if number % 2 == 0:
      print(number)# displaying numbers

for number in range(4):
    print("after",number +1)#loops create repetition
    print("after", number + 1 , (number + 1) * ".")

for numbers in range(1, 4 ,):
   print("After",number,number * ".")


successful = True
for number in range (3):
   print("Attempt")
   if successful:
      print("successful")#first attemt successful
      break
   
   successful = False
   for number in range(3):
      print("Attempt")
      if successful:
         print("successsful")
         break
else:
      print("Attempt 3 times and failed")

for x in range(5):
   for y in range(3):
      print(f"({x},{y})")#outer and inner loop

      i = 1
      while i < 6:
         print(i)
         i += 1
