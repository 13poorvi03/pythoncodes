

# Program to divide the list into two equal halves and print the sum of each half

lst = [2, 4.6, 3, 3.5, 8.3]


mid = len(lst) // 2


firsthalf = lst[:mid]
secondhalf = lst[mid:]


sumfirst = sum(firsthalf)
sumsecond = sum(secondhalf)

print("First half:", firsthalf, "Sum =", sumfirst)
print("Second half:", secondhalf, "Sum =", sumsecond)

print(sum(lst[:len(lst)//2]),sum(lst[len(lst)//2:]))


# wap to print the list first and last elements of each list list2 = [23,45,76] [45,3,12] [3,5,20]


list2 = [[23, 45, 76], [45, 3, 12], [3, 5, 20]]

for i in list2:
    print("First element:", i[0], "Last element:", i[-1])

list2 = [[23, 45, 76], [45, 3, 12], [3, 5, 20]]

lst = []
for i in list2:
    lst.append(i[0])   
    lst.append(i[-1])  

print(lst)


# wap to craete new list from the given list the new list have all the ven nnum from previous given list 


list1 = [23, 45, 76, 45, 3, 12, 3, 5, 20]


evenlst = []

for num in list1:
    if num % 2 == 0:  
        evenlst.append(num)
print(evenlst)

# wap which will create which will having all the odd numbers between 2 to 20  

oddlist = []

for num in range(2, 21):   
    if num % 2 != 0:   
        oddlist.append(num)

print(oddlist)

# first list having all odd number square and second list having all even number square 

oddlist = []
evenlist = []

for num in range(2, 21):   
    if num % 2 != 0:   
        oddlist.append(num**2)   
    else:
        evenlist.append(num**2)  

print("Odd squares:", oddlist)
print("Even squares:", evenlist)



# create a new list which have the 























# wap program 


