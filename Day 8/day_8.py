from replit import clear


someone_left = "yes"
bids = {
}


while someone_left.lower() == "yes":
    name = input("What is your name?\n")
    bid = input("How much do you want to bid?\n")
    someone_left = input("Is there someone else who wants to bid?\n")
    bids[name] = bid
    clear()
highest_bid = 0
highest_bidder = ""
for key in bids:
    if int(bids[key]) > int(highest_bid):
        highest_bid = bids[key]
        highest_bidder = key

print(f"{highest_bidder} won as he bid {highest_bid}.")
