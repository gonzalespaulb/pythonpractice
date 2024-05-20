import requests
import random
import string
import time
import os


api = "https://opentdb.com/api.php?amount=10&category=20&difficulty=medium&type=multiple"

data = requests.get(api).json()

def clear_screen():
    # Clear screen command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear screen command for Unix/Linux/MacOS
    else:
        os.system('clear')

results = data["results"]

score = 0
all_letters = list(string.ascii_uppercase)

for result in results: 
    question = result["question"]
    correct_answer = result["correct_answer"]
    all_answers = result["incorrect_answers"]

    all_answers.append(correct_answer)
    random.shuffle(all_answers)

    print(question)

    for i in range(len(all_answers)): 
        letter_and_answers = f"{all_letters[i]}:{all_answers[i]}"
        all_answers[i] = letter_and_answers
        print(letter_and_answers)
        
    print(correct_answer)
    
    user_answer = input("A , B , C , D\n").upper()
        
    if user_answer.isalpha(): 

        for answer in all_answers: 
            if answer[0] == user_answer: 
                    check_answer = answer.split(":")
                    if check_answer[1] == correct_answer: 
                         score += 1
                         print(f"{score}/10")
                         print("...")
                         time.sleep(0.4)
                         print("...")
                         time.sleep(0.4)
                         print("...")
                         time.sleep(0.4)
                         print("...")
                         time.sleep(0.4)
                         print("...")
                         time.sleep(0.4)
                         clear_screen() 
                    else: 
                        print("Incorrect")
                        print(f"{score}/10")    
                        print("...")
                        time.sleep(0.4)
                        print("...")
                        time.sleep(0.4)
                        print("...")
                        time.sleep(0.4)
                        print("...")
                        time.sleep(0.4)
                        print("...")
                        time.sleep(0.4)
                        clear_screen()                                             

        
print(f"Your final score is {score}/10")

    

    