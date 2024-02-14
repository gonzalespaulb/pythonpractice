print("Welcome to my first py program!")

participate = input("Do you want to participate? ")

if participate.lower() == "yes":
    print("Hell yeah!")
else: 
    print("Aww, why not?")

score = 0

q1 = input("Who is the best programmer ever? ")
if q1 == "Paul":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

q2 = input("What language is he practicing? ")
if q2 == "Python":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

q3 = input("What is his specialty? ")
if q3 == "CSS":
    print("Correct")
    score += 1
else:
    print("Incorrect!")

finalScore = "{}/3".format(score)

print(finalScore)