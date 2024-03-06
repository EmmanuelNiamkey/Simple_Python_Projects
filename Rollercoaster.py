print("Welcome to  Edmonton Amusement park. The rollercoaster has a height limit")

# taking the height
height = float(input("What is your height in cm?"))
bill = 0

if height >= 120:
    # check the age
    print("You can ride the rollercoaster!")
    age = int(input("How old are you?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5")

    elif age <= 18:
        bill = 7
        print("youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    # check if they want a photo
    wants_photo = input("Do you want a photo taken? Y or N ")
    if wants_photo == "Y":
        bill += 3
        print(f"Your final bill is ${bill}")
else:
    print("You don't have the required height, try other attractions")
