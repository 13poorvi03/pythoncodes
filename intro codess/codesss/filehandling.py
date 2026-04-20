# files - an name with an extension is file 

# that extension can be py,.txt,.mp3 etc and when we want to handle these files we will use file handling 

# file handling means creating reading updating deleting crud operation that we can perform in files

# "r" - read(default) - file must exist 

# "w" - write - create file or overwrites

# "a" - append - adds to end of life 

# "x" - create - creates a new file, fails if it exists




# "r" - read(default) - file must exist 

p =open(r'C:\Users\LENOVO\Desktop\python project\intro codess\codesss\dictionary.py')
print(p.read())

# "w" - write - create file or overwrites

r = open("superman.txt",'w')
r.write(" hello this is poorvi and I am writing inside this file ")
r.close()

# "a" - append - adds to end of life 

r = open("superman.txt",'a')
r.write(" hello this is poorvi and I am appending some content inside this file ")
r.close()

# "x" - create - creates a new file, fails if it exists

c = open("doremon.txt",'x')
c.write("hello doremon give me some gadgets pls ")
c.close()
