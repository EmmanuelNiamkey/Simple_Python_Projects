# Which year do you want to check?
print("Welcome to the Leap year calculator")
year = input("Type a Year\n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0 :
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year")
    else:
      print("Not leap year")
  else:
      print("Leap year")
else:
  print("Not a leap year")