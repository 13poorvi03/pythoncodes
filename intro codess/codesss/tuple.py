# immutable - tuples are not mutable you cannot change the values of tuple 

# duplicates - you can have duplicate values i  tuple there are no restriction

# ordered - set are ordered an you can access them through index values 

# heterogenous - set also have hetrogeneous nature and can have different types of data structure in tuple 

a=(1,2,3,4,5,5.5,print())

# printing elements of a tuple 

for i in a:
    print(i)

# printing index value of a tuple

for i in range(len(a)):
    print(i)

    print(a[i])
print(type(a))


# methods 

t = (5,2,9,3,5,6)

# finds the index of first occurrence of 3
index = t.index(3)
print(index)
# counts occurrence of 5 
count_five =  t.count(5)
print(count_five)


# unpacking the valuee of tuples

f,b,c,d = (1,2,3,4)
print(f)
print(c)

s=(1)
print(type(s))

s=(1,)
print(type(s))
