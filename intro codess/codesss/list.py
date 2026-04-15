fruits = ["bannna","mango","apple","orange"]
first_item, second_item, third_item, *rest =fruits

print("fruits : ", fruits)
print("numbers: ",len(fruits))

# accesing list positive index 
first_fruits = fruits[0]
print(first_fruits)

last_fruits = fruits[-1]
print(last_fruits)
print(rest)

# slicing item from a list 

all_fruits = fruits[0:4]
print(all_fruits)

first_and_second = fruits[1:3]
print(first_and_second)
mango_index = fruits[1:]
print(mango_index)

orange_index = fruits[::2]
print(orange_index)


# negative indexing 

