OneYear = 365
Weeks = 52
Months = 12
Age = int(input("Please enter your age:"))
Your_life_in_Weeks_in_Two_Years = Weeks * 2
Remainingyears = 90 - Age
Your_live_in_weeks = Remainingyears * 52
Your_live_in_days = Remainingyears * 365
Your_life_in_months = Remainingyears * 12
message = f"Here is your remaining life in Weeks, days and months:\n You have {Your_live_in_weeks} weeks, {Your_live_in_days} days, and {Your_life_in_months} months to live.\n Make the best of it!"
print(message)