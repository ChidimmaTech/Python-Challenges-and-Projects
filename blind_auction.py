from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids ={}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of £{highest_bid}\n")

while not bidding_finished:
  name = input('What is your name?\n')
  price = int(input('How much are you bidding? £\n'))
  bids[name] = price
  continue_bidding = input("Are there more bidders? Type 'yes' or 'no'\n")
  if continue_bidding == 'no':
    bidding_finished = True
    find_highest_bidder(bids)
  elif continue_bidding == 'yes':
    clear()


'''
This was done using replit so you may encounter some errors if used in another IDE. The error may occur becuase of the clear() fnction which was imported from replit. You may have to figure out how to use the clear() for your IDE
'''