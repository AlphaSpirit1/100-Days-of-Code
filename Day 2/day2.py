print("Welcome to tip calculator")
bill = int(input('What is the total bill'))
percent = int(input('How much percent do you want to tip'))
number = int(input('How many members are you'))
bill_with_tip = bill+bill*percent/100
print(f"Each persone should pay {bill_with_tip/number}")