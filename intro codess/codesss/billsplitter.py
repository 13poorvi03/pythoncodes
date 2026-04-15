print("Bill Split Calculator")
bill_amount = float(input())
tip_percentage = float(input())
num_people = int(input()
)
tip_amount =(tip_percentage/100)*bill_amount
total_amount = bill_amount+tip_amount
amount_per_person = total_amount/num_people
print(total_amount)
print(amount_per_person)