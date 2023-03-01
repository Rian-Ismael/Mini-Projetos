import random
from art import logo
from replit import clear

def my_in(e, sequence):
    for carac in sequence:
        if carac == e:
            return True
    return False

def my_remove(e, lista):
    for i in range(len(lista)-1, -1, -1):
        if e == lista[i]: lista.pop(i)
    return lista
        
def my_sum(lista):
    sum = 0
    for n in lista: 
        n = int(n)
        sum += n
    return sum

def deal_card_one():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    rand_card = random.choice(cards)
    return rand_card

def calculate_score(cards):
    if my_sum(cards) == 21 and len(cards) == 2:
        return 0
    if my_in(11, cards) and my_sum(cards) > 21:
        my_remove(11, cards)
        cards.append(1)
        
    return my_sum(cards)

def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(0, 2): 
        user_cards.append(deal_card_one())
        computer_cards.append(deal_card_one())
    
    while not is_game_over: 
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" Your cards: {user_cards}, Currente score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("You want another card? type 'y' or 'n' ")
            if another_card == 'y':
                user_cards.append(deal_card_one())
            else:
                is_game_over = True
    
    
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card_one())
        computer_score = calculate_score(computer_cards)
    
    def compare(user_score, computer_score):
    
        if user_score == 0 and computer_score == 0:
            return "You lose"
            
        elif user_score == computer_score:
            return"It's a draw"
            
        elif computer_score == 0:
            return "You lose"
            
        elif computer_score > 21:
            return "You win"
            
        elif user_score > 21:
            return "You lose"
            
        elif user_score > computer_score:
            return "You win"
            
        else:
            return "You lose"  
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == 'y':
    clear()
    blackjack()