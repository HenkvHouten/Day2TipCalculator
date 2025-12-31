print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
group = int(input("How many people to split the bill? "))

calculated_tip = bill * (tip / 100)
total_bill = bill + calculated_tip
bill_per_person = round(total_bill / group, 2)

print(f"Each person should pay: EUR {bill_per_person}")