
# muttable - dictionarries are mutable meaning you can change add or remove key value pairs after creation 

# duplicates - keys must be unique but u can have duplicates in values 

# order - dictionary follows insertion order 

# heterogenous - a dictionary can store different types of keys and values like integer ,strings ,list or even another dictionary  
d = {}
print(type(d))

# {key:values}
# each key must be unique but values can have duplicates 
d = {1:"hello",2:56}
print(d)

student = {"name":"Poorvi","age":20,10:18}
# for accesing key's values u have to use key student("name")
print(student["name"])


student[10]=1000
print(student[10])

d = {10:100,20:200,3:300,4:400,5:500}
d.update({60:600})
print(d)

