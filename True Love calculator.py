print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")

combined_names = name1 + name2 # combine the names
lower_names = combined_names.lower() # lower all the carracters
# count how many times the letter appear
t = lower_names.count("t")
e = lower_names.count("e")
r = lower_names.count("r")
u = lower_names.count("u")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# creating the two digits number
score = int(str(first_digit) + str(second_digit))

# writing the description

if (score < 10) or (score > 90) :
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together")
else:
  print(f"Your score is {score}.")