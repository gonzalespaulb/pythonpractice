# import random 

# user_wins = 0
# computer_wins = 0

# choices = ["rock", "paper", "scissors"]

# def show_picks_and_scores(user, computer, userWins, computerWins): 
#     print("User:", user , "Computer:", computer)
#     print("Running score is user:", userWins, "computer:", computerWins)

# while True: 
#      user_input = input("type rock, paper, scissors or q to quit:  ").lower()

#      if user_input == "q":
#         break

#      if(user_input not in choices):
#          continue
     
#      random_number = random.randint(0, 2)

#      computer_pick = choices[random_number]

#      if user_input == computer_pick:
#          print("Its a tie")
#          continue

#      if user_input == "rock" and computer_pick == "scissors":
#          user_wins += 1
#          show_picks_and_scores(user_input, computer_pick, user_wins, computer_wins)
#          continue
#      if user_input == "scissors" and computer_pick == "paper":
#          user_wins += 1
#          show_picks_and_scores(user_input, computer_pick, user_wins, computer_wins)
#          continue
#      if user_input == "paper" and computer_pick == "rock":
#          user_wins += 1
#          show_picks_and_scores(user_input, computer_pick, user_wins, computer_wins)
#          continue

#      else:
#          print("you lost computer wins")
#          computer_wins += 1
#          show_picks_and_scores(user_input, computer_pick, user_wins, computer_wins)


                      
# print("thanks for playing")    


# -------------------------------------------------------------- Lists 

# da_homies = []

# Edit
# da_homies[0] = "Lilly Gorl"

# Append
# da_homies.append("Varo")


# while True: 
#     new__homie = input("Please input da homie's name.\n")

#     da_homies.append(new__homie)

#     keep_adding = input("Keep adding? y or n\n").lower()

#     if keep_adding == "y": 
#         continue
#     else: 
#         break

# print(da_homies)

