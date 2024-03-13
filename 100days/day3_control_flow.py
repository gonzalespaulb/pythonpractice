# Leap year checker 

def is_leap_year (year):
    year_to_check = int(year)

    if year_to_check % 4 == 0:
        if year_to_check % 100 > 0: 
            print("is leap")
        elif year_to_check % 400 == 0: 
            print("is leap")
        else: 
            print("is not leap")
    else: 
        print("is not leap")
        
# Work storyline
        
while True:

    wake_up = input(f"Today is Thursday, another work day for you. What should we do next? snooze or wake up").lower()

    if wake_up == "snooze": 
        print("You woke up late and got fired!")
        break

    elif wake_up == "wake up": 
        print("You're up on time! Good job!")
        travel = input("How do we get to work? RFTA or Drive?\n").lower()

        if travel == "rfta": 
            rfta = input("Youre on the Rfta and you think you can sleep a little bit more. sleep or stay up?\n").lower()
            if rfta =="sleep": 
                print("You ended up at Rubey Park and was late. You got fired!")
                break
            if rfta == "stay up": 
                print("You made it to work on time and got a promotion!")
                break
            else: 
                print("Bus crashed and you died.")        
                continue

        if travel == "drive": 
            print("You made it to work on time and got a promotion!")
            break
        
        else: 
            print("You decided to walk and ended up late. You got fired")
            break 

    else: 
        print("You never woke up and died.")
        continue