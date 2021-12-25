#Swap two variables

#Using tuples
a = input("Enter a value for a ")
b = input("Enter a value for b ")

a,b = b,a
print("The value of a is after swapping",a)
print("The value of b is after swapping",b)



#using Temporary variable
a = input("Enter a value for a ")
b = input("Enter a value for b ")

temp1 = a
a = b
b = temp1

print("The value of a is after swapping",a)
print("The value of b is after swapping",b)
