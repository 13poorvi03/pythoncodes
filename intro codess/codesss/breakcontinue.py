
# a break condition refers to using the break statement inside a loop to immediately exit the loop once a certain condition is met. This allows you to stop iterating before the loop naturally finishes, giving you more control over program flow

for i in range (1,21):
    if i ==15:
        break
    else:
        print(i)

#  continue is a loop control statement that tells the program to skip the rest of the code inside the current iteration and move directly to the next iteration of the loop.       

for i in range(1,34):
    if i ==15:
        continue 
    print(i)        