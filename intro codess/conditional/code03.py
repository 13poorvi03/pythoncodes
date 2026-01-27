#if cp and sp of an item is input through the keyboard write a program to detemine whether the seller has made profit or increased write a program to determine whether the seller has made profit or incurred loss or no profit no loss also determine how much profit he made or loss he incurred

sp = int(input("enter the selling price : "))
cp = int(input("enter the cost price "))

if sp>cp:
    print("this is profitable deal")

elif sp==cp:
      print("this is neither loss nor profit deal ")

else:
     print("this is a loss deal")
