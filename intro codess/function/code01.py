# A function is a reusable block of code or programming statements designed to perform a certain task. 
# To define or declare a function, Python provides the def keyword. 
# The following is the syntax for defining a function.
#  The function block of code is executed only if the function is called or invoked.

# function without parameter

def generate_full_name ():
    first_name = 'Aaru'
    last_name = "hehehhe"
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)

generate_full_name () 


def add_twonum():
    num1 =12
    num2 = 13
    total =num1+num2
    print(total)

add_twonum()    



# Function with Parameters
# In a function we can pass different data types(number, string, boolean, list, tuple, dictionary or set) as parameters.

# one parameter

# parameter
def greeting (name): 
    message = name + " welcome to the class"
    return message

# argunmet
print(greeting("kumkaran"))


# two parameter
def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))


#Passing Arguments with Key and Value

# If we pass the arguments with key and value, the order of the arguments does not matter

def add_twonum(num1,num2):
    total = num1+num2
    return total

print(add_twonum(num1 = 45 , num2 = 55))



