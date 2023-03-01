# Split string method
import random as rd
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#who_pay = rd.choice(names)

random1 = names[rd.randint(0, len(names) - 1)]

print(f"{random1} is going to buy the meal today!")

