from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
#HINT: You can call clear() to clear the output in the console.
print(logo)
bids={}
go_ahead=True

def find_highest_bider(bidding_record):
  highest=0
  winner=""
  for bidder in bidding_record:
    bid=int(bidding_record[bidder])
    if(bid>highest):
      highest=bid
      winner=bidder
  print(f"Thw winner is {winner} with a bid of ${highest}.")

  
while(go_ahead):
  name=input("Please enter your name : ")
  price=input("Please enter your bid price : $")
  bids[name]=price
  ask=input("Any other User want to bid. If agree then write 'yes' otherwise write 'no'? ")
  if(ask=="no"):
    go_ahead=False
    find_highest_bider(bids)
  else:
    clear()