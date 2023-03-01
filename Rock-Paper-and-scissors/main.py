import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


options_list = [rock, paper, scissors]

choose = int(input("what do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choose >= 3  or choose < 0:
  print('You typed an invalid number, you lose!')
else:
  print(options_list[choose])
    
  computer_choice = random.randint(0, len(options_list) - 1)
  
  print('Computer chose: ')
  print(options_list[computer_choice])
  
  
  if choose == 0 and computer_choice == 1:
    print('You lose!')
  elif choose == 1 and computer_choice == 0:
    print('You win!')
  elif choose == 2 and computer_choice == 1:
    print('You win!')
  elif choose == 1 and computer_choice == 2:
    print('You lose!')
  elif choose == 0 and computer_choice == 2:
    print('You win!')
  elif choose == 2 and computer_choice == 0:
    print('You lose!')
  elif choose == 0 and computer_choice == 3:
    print('You win!')
  elif choose == 3 and computer_choice == 0:
    print('You lose!')
  elif choose == computer_choice:
    print("It's a draw")
  




