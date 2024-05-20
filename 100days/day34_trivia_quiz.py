import requests
import random
import string


api = "https://opentdb.com/api.php?amount=10&category=20&difficulty=medium&type=multiple"

data = requests.get(api).json()

results = data["results"]

# Present question 

# Present choices

# Ask for input on which answer user would like

# Check if input matches with correct answer

# Add to score if correct
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
        question_and_answers = f"{all_letters[i]}: {all_answers[i]}"
        print(question_and_answers)
        
    user_answer = input("Your answer here: ").upper()
    

        # print(all_answers[i])
    # for answer in all_answers: 
    #     print(f"a.{answer}")
    # user_answer = input("--Your answer--")
    

    
    

    

    