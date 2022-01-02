#program to print ASCII value of a character

val = input("Enter the value ")
val1 = ord(val)
print(val1)


# using for loop for string of characters
val = input("Enter a characters ")
for i in val:
    val1 = ord(i)
    print(i, "\t", val1)
