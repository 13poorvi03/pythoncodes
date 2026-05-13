# concatenate the string "Thirty","Days","Of","Python" to a single string, "Thirty Days Of Python"

str = ['Thirty','Days','Of','Python']
res = " ".join(str)
print(res)


# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.

str = ['Coding','For','All']
res = " ".join(str)
print(res)


# Declare a variable named company and assign it to an initial value "Coding For All".
# Print the variable company using print().

company = "Coding For All"
print(company) 
print(len(company))


# Change all the characters to uppercase letters using upper() method.

x = "hello world! this is new mee"
print(x.upper())

# Change all the characters to lowercase letters using lower() method.

y = "hello world! this is new mee"
print(y.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.

s = "coding For All"
print(s.capitalize())

print(s.title())

print(s.swapcase())


# Cut(slice) out the first word of Coding For All string.

t = "Coding For All string"
print(t[0:3])
print(t[3:])
print(t[:-1])
print(t[-3:])


# Replace the word coding in the string 'Coding For All' to Python.

j = 'Coding For All'
print(j.replace('Coding','Python'))

# Change "Python for Everyone" to "Python for All" using the replace method or other methods.

v = 'Python for Everyone'
print(v.replace('Everyone','All'))


# Split the string 'Coding For All' using space as the separator (split()) .

w = 'Coding For All'
print(w.split())

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.

r = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(''.join(r))
print(r.split())

# What is the character at index 0 in the string Coding For All.

p = "Coding For All"
print(p[0])


# Use rfind to determine the position of the last occurrence of l in Coding For All People.

p = "Coding For All"
print(p.rfind('l'))

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'



