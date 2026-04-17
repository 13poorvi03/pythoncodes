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




# mean of list elemnts 

