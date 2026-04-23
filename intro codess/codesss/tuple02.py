# empty tuple 

# tpl = ()
# tpl1 = tuple()
# print(tpl,tpl1)

# intialization 

tple = (2,3,4,1)
print(type(tple))
print(tple)

tpl = (2,3,4,5,6,"hello")
del tpl
# print(tpl)

# some important
tpl1 = (2,3,4,5,6,"hello")
print(id(tple))
tpl1 += (3,4,5,6,7)
print(id(tpl1))


# changing values in tuple 

tpl = (2,3,4,5,6,7,"hello")
tpl =list(tpl)
tpl[3] = 90
tpl = tuple(tpl)
print(tpl)


tpl2 = (2,3,4,5,6,7,4,4,4,4,4,4,5,5,5,"hello")
k = tpl2.count(4)
print(k)

tpl = {1,5,6,4,5,7,8,9,2,3,3,4,5}
