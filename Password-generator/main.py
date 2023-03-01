#Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

total = []

many_letters = 0
for letter in letters: 
  if many_letters < nr_letters:
    many_randomised_letters = letters[random.randint(0, int(len(letters)) - 1)]
    total += many_randomised_letters
    many_letters += 1
    
# print(many_letters)    
# print(total_letters)    

many_symbols = 0
for symbol in symbols:
  if many_symbols < nr_symbols:
    many_randomised_symbols = symbols[random.randint(0, len(symbols) - 1)]
    total += many_randomised_symbols
    many_symbols += 1
    
# print(many_symbols)   
# print(total_symbols)

many_numbers = 0
for number in numbers:
  if many_numbers < nr_numbers:
    many_randomised_numbers = numbers[random.randint(0, len(numbers) - 1)]
    total += many_randomised_numbers
    many_numbers += 1

# print(many_numbers)  
# print(total_numbers)
# print(total)
random.shuffle(total)

password = ""
many_total = 0
for combination in total:
  password += combination
  many_total += 1
  
# print(total)
print(f"Your password is: {password}")