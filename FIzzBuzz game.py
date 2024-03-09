# Write your code here 👇
for number in range(1, 100 + 1):

    # Multiple of 3
    if number % 3 == 0 and number % 5 == 0:
        print("fizzBuzz")

    elif number % 3 == 0:
        print("fizz")


    # Multiple of 5
    elif number % 5 == 0:
        print("Buzz")

    else:
        print(number)
