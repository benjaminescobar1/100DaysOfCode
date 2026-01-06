# Greets User and prompts questions
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? \n$"))
tip = int(input("What percentage tip would you like to give? 10 12 15 \n"))
people = int(input("How many people to split the bill? \n"))


# Calculate the tip amount
bill_with_tip = tip/100 * bill

# Add the tip to the original bill to get the total bill
total_bill = bill + bill_with_tip

# Divide the total bill by the number of people to find each person's share
bill_per_person = total_bill / people

# Round the final amount to 2 decimal places for currency format
final_amount = round(bill_per_person, 2)


# Print how much each person should pay
print(f"Each person should pay: ${final_amount}")

