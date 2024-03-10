import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many symbols would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))


# Eazy level not randomizing the sequence of password
password = ""  # taking a variable password string that is empty, we will fill it gradually
for char in range(1, nr_letters + 1):
    random_char = random.choice(letters)  # selecting randomly in the string : letters
    password = password + random_char  # or password += random_char

for char in range(1, nr_numbers + 1):
    random_char = random.choice(numbers)
    password += random_char

for char in range(1, nr_symbols + 1):
    random_char = random.choice(symbols)
    password += random_char
    print(password)

# Hard level
password_list = []  # taking a variable password this time a list
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(symbols))


for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(numbers))
    print(password_list)
    random.shuffle(password_list)  # shuffle elements of a list
    print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is : {password}")