#using for-loop

num = int(input("Enter a number  "))
 
factorial = 1

#checking conditions 
if num == 0:
     print("The factorial of", num, "is 1")
elif num < 1:
    print("Negative number should not be entered for factorial")
else:
     for i in range(1, num + 1):
         factorial = factorial * i
     print("The factorial of", num, "is",  factorial )
