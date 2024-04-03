class Employee: 
    def __init__(self, name, employee_id, email):

        self.name = name
        self.employee_id = employee_id
        self.email = email
        self.current_hours = 0

    def update_hours(self, number_of_hours): 
            self.current_hours += number_of_hours


paul = Employee("Paul Gonzales", 142965, "gonzalespaulb@gmail.com")
paul.update_hours(5)
paul.update_hours(5)

class Score: 
     def __init__(self):
          self.score = 0
    
     def add_point(self): 
          self.score += 1
          print(f"{self.score}/{len(questions)}")

class Question: 
     def __init__(self, question, answer):
          self.question = question
          self.answer = answer
     
     def ask_question(self): 
          user_answer = input(f"{self.question} (True or False): ")
          if user_answer == self.answer: 
               print("Correct!")
               score.add_point()
          else: 
               print("Incorrect.")    
               print(f"{score.score}/{len(questions)}")

question_1 = Question("Filipinos are from the Philippines", "True")
question_2 = Question("Aspen Ajax is a snowboarder's mountain", "False")
question_3 = Question("Vail is owned by Aspen Ski Co", "False")

questions = [question_1, question_2, question_3]
score = Score()

for question in questions: 
     question.ask_question()

print(f"Finished the quiz! Your final score is {score.score}/{len(questions)}")