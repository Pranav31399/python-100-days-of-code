print("Welcome to the tip calculator!!")
total_bill=float(input("What was the total bill? $"))
no_of_people=int(input("How may people to split the bill with "))
tip_in_percent=float(input("What percentage tip would you like to give? "))
result=round((total_bill*(1+tip_in_percent/100))/no_of_people,1)
print(f"Each person should pay : ${result}")
