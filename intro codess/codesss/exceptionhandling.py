# errors occur due to mistakes in the code thsat preventt it from running. these can be syntax errors or logical errors 

# syntax error 
# indentation error 
# tab error - when u mix tabs and spaces
print("hello world")
a=12
if a==12:
  print("hello")





#   exceptions - are unexpected events or errors that occurs during the execution of a program which disrupts the normal flow of the program 

# a =int(input("tell your number : "))


# # raises zerodivision on error 
# print(10/a)

# # this line will never run 
# print("okay boss")

# like this these are many other exception just leaves the three errors we saw at start otherwise others are exceptions







# keywords - purpose 

# try - wrap the block of code that might cause an exception 

# except - handle the exception if it occurs 

# else - run code only if no exception occurs

# finally - run code no matter what whether there is an exception or not 

# raise - manually throw an exception 


b = int(input("enter the number : "))
try:
  print(10/b)

# except ZeroDivisionError:
except Exception as err:
  print(f"sorry there is an err as{err}")

print("okay i have done the dividion ")

# namee error 

d = int(input("tell ur name : "))
try :
  print(10/a)

except Exception as err:
  print(f"sorry there is an error as {err}")

else:
   print("good there is no exception ")
 

finally:
   print(" i will run no matter what ")

print("ok i have done the division ")    


# different code self occuuring error 

age = int(input("Tell your age: "))

try:
    if age < 10 or age > 18:
        raise ValueError("Your age must be between 10 to 18")
    else:
        print("Welcome to the club")
except Exception as err:
    print(f"An error occurred: {err}")

print("The club will start soon")
