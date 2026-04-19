# mutable = u can change value in set 

# duplicates - cannot have any duplicate values in set that mens every element will be unique 

# unordered - sets are unordered and u cannot access them through index values 

# heterogenous - set is semi heterogenous it can store some data type like string numbers tuples but not everything 

# list and dictionaries are not allowed 

# set stores value in hashing form hashing is basically kind of addresss it storess in value in address form thats why it is unordered 

s = {12,23,45,67}
print(s)
print(type(s))

k = 12
b = hash(k)
print(b)

d = hash("hello")
print(d)

c = hash((1,2,3,4,5,6))
print(c)

# set traversing 
# set cannot be traversed  using  the index values cause it is unordered and has no index 

p = {1,2,67,3,"hello",4,5,6}


for i in p:
    print(i)



# set methods 

l = {12,23,34,45,67,75,64}

# adds an elements to the set 
l.add(4)
print(l)

# remove 23 
l.remove(23)
print(l)

# removes 34
l.discard(34)
print(l)

# removes a random element  , it removes mostly first elem of set 
popped_elem = l.pop()
print(l)

# removes all elements 
s.clear()


m ={1,2,3,4,5}
n ={4,5,6,7,8}

# it prints all the set elements in one set but without duplicates
union_set = m.union(n)
print(union_set)

# it prints only those numbers which are common in both set 
intersection_set = m.intersection(n)
print(intersection_set)

# it prints those number which is not belongs to set n means 1,2,3 is not presentt in set n 
difference_set = m.difference(n)
print(difference_set)

# it prints those number which is common in both set 
symmetric_diff = m.symmetric_difference(n)
print(symmetric_diff)