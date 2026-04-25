
numbers = [10, 20, 30, 40, 50]

print(numbers[2])
print(len(numbers))
isempty =len(numbers)==0
print(f"is the list is empty ? {isempty}")


numbers[2] = 200
print(f"the updated version of list is : {numbers}")

numbers.append(600)
print(f" the new list : {numbers}")

numbers.insert(2,300)
print(f" after inserting the new list is : {numbers}")

numbers.remove(600)
print(f" after removing by element the new list is : {numbers}")

numbers.pop()
print(f" after removing by index, updated list is  : {numbers}")


sum = 0 
for i in numbers:
    sum+=i
    
print(f"total sum of list {sum}")    

print(f"the average of list :  {sum//len(numbers)}")


max = numbers[0]
for i in numbers:
    if max < i:
        max=i

print(f"maximum number of list {max}")  



min= numbers[0]
for i in numbers:
    if min > i:
        min=i

print(f"minimum number of list {min}")  



product = 1
for i in numbers:
    product*=i
    
print(f"total product of list {product}")  


even = 0
odd = 0
for i in numbers:
    if i % 2==0:
        even+=1
        

    else:
        odd+=1
         

print(f"total count of even numbers : {even}")
print(f"total count of odd numbers : {odd}")


numbers = [10, 20, 300, 200, 40]
print("Reversed list:", numbers[::-1])


numbers = [10, 20, 300, 200, 40]
numbers.reverse()
print("Reversed list:", numbers)


numbers.sort()
print("sorted list ",numbers)


lst = ["Apple", "Banana", "Cherry"]
lst2 = numbers.copy()
print(lst2)



listA = ["Physics", "Chemistry"]
listB = ["Maths", "Biology"]

combined = listA + listB

print(f"combined list : {combined}")


# exercise - 11
# list slicing extract middle elements

List = [10, 20, 30, 40, 50, 60, 70]
s = List[2:5]
print(f"middle three : {s}")



my_list = [10, 20, 30, 40, 50]

print("Full list:", my_list)


for item in my_list:
    print(item)

