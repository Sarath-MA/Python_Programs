#define functions
def add(num1,num2):
    return num1 + num2
def sub(num1,num2):
    return num1 - num2
def Mul(num1,num2):
    return num1 * num2
def Div(num1,num2):
    return num1 / num2

print("Enter your operation\n" "1.Add \n" "2.Sub \n" "3.Mul \n" "4.Div\n")
select = int(input("Enter your operation\n" "1\n" "2\n" "3\n" "4\n"))

#Getting user input
num1 = int(input("Enter a first number "))
num2 = int(input("Enter a second number "))

#Checking conditions
if select == 1:
	print(num1, "+", num2, "=",
					add(num1, num2))

elif select == 2:
	print(num1, "-", num2, "=",
					sub(num1, num2))

elif select == 3:
	print(num1, "*", num2, "=",
					Mul(num1, num2))

elif select == 4:
	print(num1, "/", num2, "=",
					Div(num1, num2))
else:
	print("Invalid input")

    
    
