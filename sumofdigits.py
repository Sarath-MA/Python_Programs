#program to create sum of digits
num = int(input("Enter a number "))
copy = num
sum = 0
while num > 0:
    r = num % 10
    sum = sum + r
    num //= 10
print("Sum of digits")
print("The sum of digits are",sum)

