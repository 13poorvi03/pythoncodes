
# # string indexing

# # indexing start from [0] it could be negative and positive both 

# c= "hello broo what's up"


# print(c[2])
# #  //printing from lastt

# print(c[-6])
# print(c[6],c[-4])

# # ord convvert letter in unique code
# a= "A"
# print(ord(a))  

# # chr convert unique code in letter
# b = 65
# print(chr(b))


# # string slicing

# # slicing means cutting out a slice from string and this is also done using index values 
# # we have start ,stop and steps position and keep a note if we use stop at 4 will slice till 3 only 

# o = "kiii haal chaal"
# print(o[0:3:1])

# # default :: it print to end
# r = "SHER CODER"
# print(r[5::1])

# 


greeting = "hello world!"
print(greeting)
print(len(greeting))


first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)


a = 4
b = 3

print('{} + {} = {}' .format(a,b, a+b))
print('{} - {} = {}'.format(a,b,a-b))



# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
print(formated_string)



a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# slicing 
language = "python"
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)

# reversing a string 

greeting = "hello , world!"
print(greeting[::-1])

# skipping char

lannguage = "python"
pto = language[0:6:2]
print(pto)


# string method

# capitalize() - to convert the first character of the string to capital letter 

challenge = "thirty days of python "
print(challenge.capitalize())

# count() -- returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.

print(challenge.count('y'))
print(challenge.count('y',7,14))
print(challenge.count('th'))