#Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


lowercase = name1.lower() + name2.lower()

t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")
########################
l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")

true = t + r + u + e
love = l + o + v + e

score = int(str(true)) + int(str(love))

if score < 10 or score > 90:
  print(f'Your score is {score}, you go together like coke and mentos.')
elif score >= 40 and score <= 50:
  print(f'Your score is {score}, you are alright together.')
else:
  print(f'Your score is {score}.')