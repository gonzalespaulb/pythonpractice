import random
import os
import time

chips = 5000
bet = 0

# Function to clear the terminal screen
def clear_screen():
    # Clear screen command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear screen command for Unix/Linux/MacOS
    else:
        os.system('clear')

def delay_timer(seconds): 
    print("Game resetting in 5s.")
    time.sleep(5)
    clear_screen()

def deal_cards(): 
    return random.randint(1, 11)

def is21(card_1, card_2): 
    if card_1 + card_2 == 21: 
        return True
    else: 
        return False
    
def is_greater_than_17(cards): 
    if sum(cards) >= 17: 
        return True
    
    else: 
        return False

while True: 

    if chips < 1:
        reup = input("Looks like you're out of chips! Re up? y or n\n").lower()

        if reup == "y": 
            chips += 5000
            print("Heres another $5000. On the house ;)\n")
        
        else: 
            break

    play_question = input("Would you like to play a hand? y or n\n").lower()

    if play_question == "y": 
        while True: 
            
            bet = int(input(f"How much would you like to bet? You currently have ${chips}\n"))

            if bet > chips: 
                print(f"You only have ${chips}. Please try again.\n")
                continue
                
            else:
                player_card_1 = deal_cards()
                player_card_2 = deal_cards()
                dealer_card_1 = deal_cards()
                dealer_card_2 = deal_cards()

                player_cards = [player_card_1, player_card_2]
                dealer_cards = [dealer_card_1, dealer_card_2]

                print("Dealer is checking for 21.\n")

                if is21(player_card_1, player_card_2): 
                    chips += bet
                    print(f"You have blackjack!! (+${bet})")
                    print("Game resetting in 5s.")
                    time.sleep(5)
                    clear_screen()
                    break

                elif is21(dealer_card_1, dealer_card_2): 
                    chips -= bet
                    print(f"Dealer has blackjack!! (-${bet})")
                    print("Game resetting in 5s.")
                    time.sleep(5)
                    clear_screen()
                    break
                
                else: 
                    initial_cards = f"Player-[{player_card_1}, {player_card_2}]: {player_card_1 + player_card_2} || Dealer-[{dealer_card_1}, *]\n"
                    print(initial_cards)

                    while True: 
                        hit_or_stay = input(f"You currently have {sum(player_cards)}. Hit or stay? h or s?\n").lower()

                        if hit_or_stay == "h": 
                            player_cards.append(deal_cards())

                            if sum(player_cards) > 21: 
                                print(f"{sum(player_cards)}. You bust! (-${bet})")
                                chips -= bet
                                print("Game resetting in 5s.")
                                time.sleep(5)
                                clear_screen()
                                break

                            else: 
                                continue

                        elif hit_or_stay == "s":

                            while True: 

                                print(f"Dealer currently has {sum(dealer_cards)}.")

                                if sum(dealer_cards) >= 17 and sum(dealer_cards) <= 21:
                                    if sum(dealer_cards) > sum(player_cards): 
                                        print(f"You lost! (-${bet})")
                                        chips -= bet
                                        print("Game resetting in 5s.")
                                        time.sleep(5)
                                        clear_screen()
                                        break

                                    elif sum(dealer_cards) == sum(player_cards): 
                                        print("Its a push!")
                                        print("Game resetting in 5s.")
                                        time.sleep(5)
                                        clear_screen()
                                        break

                                    else:
                                        print(f"You win! (+${bet})")
                                        chips += bet
                                        print("Game resetting in 5s.")
                                        time.sleep(5)
                                        clear_screen()
                                        break
                                
                                elif sum(dealer_cards) < 17: 
                                    dealer_cards.append(deal_cards())
                                    continue

                                elif sum(dealer_cards) > 21: 
                                    print(f"Dealer bust! You win! (+${bet})")
                                    chips += bet
                                    print("Game resetting in 5s.")
                                    time.sleep(5)
                                    clear_screen()
                                    break
                            break

                        else: 
                            print("Not a valid move.\n")
                            continue
            break                    
    else: 
        break