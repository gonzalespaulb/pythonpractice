import random

starting_chips = 5000
bet = 0

def deal_cards(): 
    return random.randint(1, 11)



while True: 

    print(f"You currently have ${starting_chips}")

    player_card_1 = deal_cards()
    player_card_2 = deal_cards()
    dealer_card_1 = deal_cards()
    dealer_card_2 = deal_cards()

    play = input("Would you like to play blackjack? y or n\n").lower()

    if play == "y": 
        set_bet = int(input("How much would you like to bet?\n"))
        bet = set_bet
        
    else: 
        print(f"Thank you for playing! Your total winnings are ${starting_chips}")