# accept an integer and check wheather it is an even or odd

value1 = int(input("enter the number "))  

if value1 % 2 ==0 :
    print("the number is even " , value1)

else:
    print("the number is odd " , value1)


# accept name and age from the user check if the user is a valid voter or not

name = str(input("enter the user name : "))
age = int(input("enter the age of user : "))

if age > 18: 
    print(f"this user {name} is valid for voting coz his/her age is {age}")

else:
  print(f"this user {name} is not valid for voting coz his/her age is {age}")


# accept a year and check if it is a leap year or not 

year = int(input("Enter the year: "))

if year % 400 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year} is not a leap year")
elif year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

    # codeeeee

temp = int(input("enter the temperature of the city : "))

if temp < 0:
    print("this is a freezing cold temp ")

elif temp < 10:
    print(" this is a very good temp ")

elif temp <20:
    print("this is cold temp ")

elif temp <30 :
    print (" this is less cold temp ")

else:
    print("average or hot temp")    

