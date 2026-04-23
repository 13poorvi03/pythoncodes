# find the length of your list 

# lst = [12,3,45,34,67,544,21,34,78]

# print(len(lst))




# get the first item the middle item and the lat item of the list 

# lst1 = [12,3,45,34,67,544,21,34,78]
# print(lst[0])
# print(lst[-1])
# print(len(lst)//2)



# Sort the list and find the min and max age

# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# max = ages[0]
# min = ages[0]
# for i in ages:
#     if max<ages:
#         max=ages[i]
        

# print(max)
    



# # wap to compute the ddifference between two list 

# color = ["red","orange","green","blue","white "]
# color2 = ["black", "yellow","green","blue"]

# lst = []   # elements in color but not in color2
# lst2 = []  # elements in color2 but not in color

# for i in color:
#     if i not in color2:
#         lst.append(i)

# for i in color2:
#     if i not in color:
#         lst2.append(i)

# print("Difference from color:", lst)
# print("Difference from color2:", lst2)


# # wap to pack consecutive duplicates of a given liistt pf elemnets into sublist 



# lst = [0,0,1,1,2,3,4,4,4,5,5,6,6,7,7,8]

# result = []
# sublist = [lst[0]]   

# for i in range(1, len(lst)):
#     if lst[i] == lst[i-1]:
#         sublist.append(lst[i])    
#     else:
#         result.append(sublist)   
#         sublist = [lst[i]]       

# result.append(sublist)  
# print(result)





# wap to remove consecutive duplicates elements free a given 


lst = [0,0,1,1,2,3,4,4,4,5,5,6,6,7,7,8,4,4]

result = [lst[0]]   

for i in range(1, len(lst)):
    if lst[i] != lst[i-1]:   
        result.append(lst[i])

print(result)
