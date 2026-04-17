# fruits = ["bannna","mango","apple","orange"]
# first_item, second_item, third_item, *rest =fruits

# print("fruits : ", fruits)
# print("numbers: ",len(fruits))

# # accesing list positive index 
# first_fruits = fruits[0]
# print(first_fruits)

# last_fruits = fruits[-1]
# print(last_fruits)
# print(rest)

# # slicing item from a list 

# all_fruits = fruits[0:4]
# print(all_fruits)

# first_and_second = fruits[1:3]
# print(first_and_second)
# mango_index = fruits[1:]
# print(mango_index)

# orange_index = fruits[::2]
# print(orange_index)


# # negative indexing 










# methodsss 

lst = [2,4,6,7,8,9,5,4,8,8,8]
 
# adds 10 to the end 
lst.append(10) 
print(lst)

# insert 15 at index 2
lst.insert(2,15)
print(lst)

# adds multiple elements at the end 
lst.extend([20,34,56,78])
print(lst)

# remove the first occurrence of 4
lst.remove(4)
print(lst)

# remove and stores the elements at index 3 
popped_item = lst.pop(7)
print(lst)

# finds the index of 5
index = lst.index(5)
print(lst)

# count occurrence of 5 
count_5 = lst.count(8)
print(lst)

# sorts the list in ascending order 
lst.sort()
print(lst)

# reverse the list order 
lst.reverse()
print(lst)

# create a copy of the list 
new_lst=lst.copy()
print(lst)

# remove all elemets from list 
lst.clear()
print(lst)