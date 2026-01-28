# Take 3 positive integer inputs
num1 = int(input("Enter first num: "))
num2 = int(input("Enter second num: "))
num3 = int(input("Enter third num: "))

# Compare and find the greatest
if num1 >= num2 and num1 >= num3:
    print("The greatest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("The greatest number is:", num2)
else:
    print("The greatest number is:", num3)