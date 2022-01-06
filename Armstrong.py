num = int(input("Enter a number "))
copy = num
sum = 0
while num > 0:
    r = num % 10
    sum = sum + (r * r * r)
    num //= 10
#checking conditions
if sum == copy:
    print(copy, "is an armstrong number")
else:
    print(copy, "is not an armstrong number")
