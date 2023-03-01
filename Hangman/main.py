import random

from replit import clear

from hangman_words import word_list

from hangman_art import logo
print(logo)

from hangman_art import stages

#######################

randomly_word = random.randint(0, len(word_list) - 1)
chosen_word = word_list[randomly_word]
lives = 6

#######################

#Create blanks
def many_underscore(word):
  display = []
  for i in range(len(word)):
    i = display.append("_")
  return display
  
######################
  
#my join.
def my_join(lista):
  str_convert = ""
  for to_str in range(len(lista)):
    str_convert += lista[to_str]
  return str_convert

########################

#my in.
def my_in(e, list):
  for i in list:
    if i == e:
      return True
    else:
      False
#########################  

replace = many_underscore(chosen_word)
while True:
  guess = input("Guess a letter: ").lower()

  clear()

  if my_in(guess, replace):
    print(f"You've already guessed: {guess}")
  
  for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
      replace[position] = letter
     
#########################

  #Check if user is wrong.
  if not my_in(guess, chosen_word):
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives -= 1
      if lives == 0:
          print("you lose")
          print(stages[lives]}\nlife remain: {lives}")
          break
   
  #Join all the elements in the list and turn it into a String.
  print(my_join(replace))
  
  #Check if user has got all letters.
  if not my_in("_", replace):
      print("you win")
      print(f"{stages[lives]}\nlife remain: {lives}")
      break
  else:
      pass
  print(f"{stages[lives]}\nlife remain: {lives}")
