# list  odd element add 5 and for even element minus 5
# x= eval(input())
# for i in range(len(x)):
#  if x[i]%2==0:
#   x[i]-=5
#  else:
#   x[i]+=5
# print(x)

# print largest element from that list 

# lst = [3,5,7,18,20,11,26]
# l = 5
# sl = 3
# for i in range(2,len(lst)):
#     if lst[i]>l:
#         l=lst[i]
#     elif lst[i]>sl:
#         sl=lst[i]

# print(l)
# print(sl)






# addding element options  

# append function 
# append only add one element in lst

lst = [3,5,7,18,20,11,26]
# lst.append("hello")
# lst.append([3,4,5,6,7,8])
# print(lst[-1][3])
# print(lst)



# inserting 
# it gonna add on n+1 space ex (-3,34) so elem gonna inset in -4 index
lst.insert(3,35)
print(lst)
lst.insert(-3,78)
print(lst)



# extend
lst = [3,5,7,18,20,11,26]
# lst.extend({3,4,5,67,89})
lst+= {3,4,5,67,89} 
print(lst)




# delete 
lst = [3,5,7,18,20,11,26]
del lst[3]
print(lst)

#pop also print the value of deleted elem
x=lst.pop(4)
print(lst)
print(x)

# with remove operation value have to be present in lst

lst.remove(7)
print(lst)

# count use to count element how many time it is present in lst
lst.count(20)

# use reverse for reversing list 
lst.reverse()
print(lst)

# for sorting list 
lst.sort()
print(lst)

# inbuild sorted function 
sorted([3,78,90,56,76])
print(sorted([3,78,90,56,76]))