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

    player_cards = [player_card_1, player_card_2]
    dealer_cards = [dealer_card_1, dealer_card_2]

    play = input("Would you like to play blackjack? y or n\n").lower()

    if play == "y": 
        set_bet = int(input("How much would you like to bet?\n"))
        bet = set_bet
        starting_chips -= set_bet
        print(f"Player: [{player_card_1},{player_card_2}] Dealer: [{dealer_card_1}, *] ---- You currently have {player_card_1 + player_card_2}")

        while True: 

            hit_or_stay = input("Hit or stay?\n").lower()

            # What happens if dealer has 21
            if sum(deal_cards) == 21: 
                print("Dealer has blackjack! You lost.")
                break

            # What happens on hit
            if hit_or_stay == "hit": 
                player_cards += deal_cards()
                continue

            if hit_or_stay == "stay": 
                if sum(dealer_cards) < 16: 
                    dealer_cards += deal_cards()
                    continue
                else: 
                    if sum(dealer_cards) > sum(player_cards): 
                        print(f"Dealer has {sum(deal_cards)} and you have {sum(player_cards)}. Dealer won!")
                        break
                    else: 
                        starting_chips += bet * 2
                        print(f"Dealer has {sum(deal_cards)} and you have {sum(player_cards)}. You won ${starting_chips}!")
                        
            # What happens on stay
                # If dealer is less than 15 hit
                # Else stay and compare with dealer cards

    else: 
        print(f"Thank you for playing! Your total winnings are ${starting_chips}")