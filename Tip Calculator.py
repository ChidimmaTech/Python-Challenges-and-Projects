

print("Welcome To Your Tip Calculator...Calculate Away :)")
bill = int(input("What is your total bill?\n"))
percentage = int(input("What percentage tip would you like to give?\n"))
no_of_people = int(input("How many people will be splitting the bill?\n"))
tip = percentage/100 * bill
total_bill_with_tip = tip + bill
bill_per_person = total_bill_with_tip/no_of_people
final_amount = round(bill_per_person, 1)
message = f"Each person should pay £{bill_per_person}"
print(message)