print('Welcome To Your Love Calculator:\n')
Name1 = input("Enter Your Full Name:\n")
Name2 = input("Enter Your Partner's Full Name:\n")
Names = (Name1 + Name2).lower()

true_score = 0
love_score = 0

for letter in set('true'):
  true_score += Names.count(letter)
for letter in set('love'):
  love_score += Names.count(letter)

total_score = int(str(true_score) + str(love_score))

if total_score < 10 or total_score > 90:
  message=(f'You are {total_score}% compatible, you go together like coke and mentos.')
  print(message)

elif total_score >= 40 and total_score <= 50:
  message = (f'You are {total_score}% compatible, you are alright together.')
  print(message)

else:
  message = (f'You are {total_score}% compatible.')
  print(message)
  