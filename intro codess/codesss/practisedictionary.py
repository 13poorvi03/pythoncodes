# wap a python script to merge two python dictionaries 

d1={10:1000,20:200,30:300}
d2={40:400,50:500,60:600}

for i in d2:
    # taking all the key and values from d2 and updating all the values in d1
    d1[i]=d2[i]

print(d1)


# wap python program to sum all the values in a dictinary 
d3={10:1000,20:200,30:300}
sum = 0
# it sum all the values of dictionary 
for i in d1:
    sum+=d1[i]

print(sum)


# count the frequency of each elements 

a =[1,1,1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,5,6,6,6,7,7,8,9]
d = {}
# {1:3,2:2,3:3,4:4,5:6}
for i in a:
    if i in d.keys():
        d[i] +=1
    else:
        d[i] = 1

print(d)        

#  write a python program to combine two dictionary by adding values two common keys 

d4={10:1000,20:200,30:300}
d5={40:400,50:500,60:600}

for i in d2:
    if i in d4.keys():
        d4[i] +=d5[i]
    else:
        d4[i] = d5[i]

print(d4)        