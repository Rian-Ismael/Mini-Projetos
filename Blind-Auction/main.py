from replit import clear
from art import logo
print(logo)

bets = {

}

def add(dic): #parâmetro: um dic.
    highest_bid = 0
    winner = ""
    for key in dic:
        value = dic[key]
        if value > highest_bid:
            highest_bid = value
            winner = key           
    print(f"The winner is {winner} with a bid of ${highest_bid}")
        
while True:
    name = input("What is your name? ")
    value_bet = int(input("What is your bid? $"))
    bets[name] = value_bet #adiciona a key(name) e o valor da key (bets[name]) no dicionário BETS.
    proceed = input("Are there any other bidders? Type 'yes or 'no'. ")
    if proceed == "no":
        add(bets) #O que foi armazenado em bets é "jogado" na função, o qual irá selecionar a maior aposta e o vencedor.
        break
    elif proceed == "yes":
        clear()
        continue