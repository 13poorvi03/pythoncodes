lst1=[]
print(lst1)

lst = [20,'poori',True,'23',"yess"]
print(len(lst))

print(lst[0])
print(lst[len(lst)-1])
print(lst[len(lst)//2])

lstt = ['Facebook',' Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(lstt)
print(len(lstt))
print(lstt[0])
print(lstt[len(lst)-1])
print(lstt[len(lst)//2])

lstt[0] ="bain"
print(lstt)

# adding zomato into lstt
lstt.append("zomato")
print(lstt)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle"]

# Change one company to uppercase (excluding IBM)
for i in range(len(it_companies)):
    if it_companies[i] != "IBM":
        it_companies[i] = it_companies[i].upper()
        break   # stop after changing one
print(it_companies)


x = ["i","j","k"]
y=["o","p","q","a","j"]
x.extend(y)
print(x)

does_exist= "p" in y
print(does_exist)

y.reverse()
print(y)

y.sort()
print(y)

print(y[0:2])

y.remove("p")
print(y)

del y[len(y)//2]
print(y)

y.pop()
print(y)

y.clear()
print(y)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(min(ages))
print(max(ages))