# Linear Search Program in Python

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i   # return index if found
    return -1          # return -1 if not found

# Main program
print("Welcome to Linear Search Demo!")

# Taking input from user
n = int(input("Enter number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    num = int(input(f"Element {i+1}: "))
    arr.append(num)

key = int(input("Enter the element to search: "))

# Searching
result = linear_search(arr, key)

# Output
if result != -1:
    print(f"Element {key} found at index {result}")
else:
    print(f"Element {key} not found in the list")
