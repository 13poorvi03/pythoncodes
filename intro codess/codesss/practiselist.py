# print even and odd elemets of an list 

lst = [23, 45, 67, 89, 34, 23, 57, 98]

even_count = 0
odd_count = 0

for i in lst:
    if i % 2 == 0:
        print(i, "is Even")
        even_count += 1
    else:
        print(i, "is Odd")
        odd_count += 1

print("\nTotal number of even elements:", even_count)
print("Total number of odd elements:", odd_count)



#  print even and odd elemets of an list 

lst = [23, -45, 67, -89, 34, -23, 57, -98]
print("positive elements are : ")
for i in lst:
    if i>=0:
        print(i)

print("negative elemnets are : ")
for i in lst:
    if i<0:
        print(i)


# mean of list elemnts 

lst = [23, 45, 67, 89, 34, 23, 57, 98]

total = 0
for i in lst :
    total+=i

print(total)    

x = total/len(lst)
print(x)


# print the largest and second largest elem in lst 


lst = [23, 45, 67, 89, 34, 23, 57, 98]

max_num = lst[0]
smax = lst[0]  # start with very small number

for i in lst:
    if i > max_num:
        smax = max_num   # update second largest
        max_num = i      # update largest
    elif i > smax and i != max_num:
        smax = i         # update second largest only

print("The largest number:", max_num)
print("The second largest number:", smax)
    

# check if the list is sorted or not 

lst = [23, 45, 67, 89, 34, 23, 57, 98]

lst.sort()
print(lst)




# mutable - mutablity refers to whether an object's value can be changed after creation and list sllows this 

# duplication - list allows same value many times 

# orderes - it maintain the sequence of elemas they were inserted tthis means u can access elements using their position(index)

# heterogenous - list have heterogenous nature that means we can have multiple data type inside the list  