
# its a block of reusable code that we create whenever we want to call it then only it will work 

# def hello():
#     print("this is a hello fucntion ")

# hello()



# create a function for sum of given integer 

def sum(a,b):
    print(f"the sum of your numbers is {a+b}")

sum(12,3)   
sum(69,88)

#   types of parameter 

# positional arguments 

def sub(a,b):
    print(f"the subtraction of two number : {a-b}")

sub(19,2)
sub(15,5)


# default arguments 

def introduce(name,age):
    print(f"i am {name} and i am {age} years old .")

introduce("poorvi",20)   


# keyword argumnets 

def greet(uname,agee):
    print(f"your name is {uname} and your age is {agee}")

greet (agee = 22 , uname = "akarsh")

# use of return 
def gud():
    return "good morning bro"

print(gud())