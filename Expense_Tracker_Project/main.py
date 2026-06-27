#expense tracker project 

expensesList = []   #list of expenses in form of dictionary 
print("Welcome to expense tracker : spend less bbygurl")

while True:
    print("====MENU====")
    print("1. Add Expenses")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("please enter your choice : "))

# ADD Expense
    if(choice==1):
        date = input("enter the date dd-mm-yy")
        category=input("enter the type..(food,travel,makeup,books)")
        description =input("write a detailed description of ur spendings")
        amount = float(input("enter the amount: "))

        expense={
            "date": date,
            "category": category,
            "description":description,
            "amount": amount
        }

        expensesList.append(expense)
        print("\n Done bro! expenses is added succesfully")


# view all expenses
    
    elif(choice==2):
        if(len(expensesList)==0):
            print("No Expenses Added.\n bro spend some moneyy")
        else:
            print("===== this is your all expenses=====")
            count =1
            for eachspending in expensesList:
                print(f"first spending{count} -> {eachspending["date"]} , {eachspending["category"]} ,{eachspending["description"]} ,{eachspending["amount"]}")
                count=count+1



# View Total Spending
    elif(choice ==3):
        total = 0
        for eachspending in expensesList:
            total = total + eachspending["amount"]

            print("\n Total expenses = ", total)


# exist
    
    elif(choice==4):
        print("Thank you for trusting us take care meet agian asap")
        break

    else:
        print("Invalid choice")







        
