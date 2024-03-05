print("Welcome to the tip calculator")

# Taking the inputs
total_bill = input("What is the total amount of the bill?")
tip = input("what percentage tip will you give? 10, 12, 15?")
people = input("How many people to split the bill?")

# Converting all the inputs in floats
tip_float = float(tip)
total_bill_float = float(total_bill)
people_float = float(people)

# Calculating tip in decimal
total_tip_decimal = (tip_float * total_bill_float) / 100
print(f"The total tip is ${total_tip_decimal}")

# Computing everything and round it
each_bill = (total_bill_float + total_tip_decimal) / people_float
each_bill_rounded = round(each_bill, 2)
final_amount = "{:.2f}".format(each_bill)

print(f"Each person should pay ${final_amount}")