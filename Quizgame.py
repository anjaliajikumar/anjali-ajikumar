print("----------WELCOME TO QUIZ GAME----------")
playing=input("Do You Want To Play The Game?(yes/no)  ")
if playing.lower()!="yes":
    quit()
print("Okey Lets Play!!!!!")
SCORE=0
answer=input("What does CPU Stands for?  ")
if answer.lower()==("central processing unit"):
    print("correct!")
    SCORE+=1
else:
    print("Sorry wrong answer :(")

answer=input("easiest programming language currently?  ")
if answer.lower()==("python"):
    print("correct!")
    SCORE+=1
else:
    print("Sorry wrong answer :(")

answer=input("unit of resistance?  ")
if answer.lower()==("ohm"):
    print("correct!")
    SCORE+=1
else:
    print("Sorry wrong answer :(")

answer=input("wjat does GPU stand for?  ")
if answer.lower()==("graphics processing unit"):
    print("correct!")
    SCORE+=1
else:
    print("Sorry wrong answer :(")

answer=input("full form of RISC?  ")
if answer.lower()==("reduced instruction set computer"):
    print("correct!")
    SCORE+=1
else:
    print("Sorry wrong answer :(")

answer=input("resulting operation of an AND and OR gate is?  ")
if answer.upper()==("AND"):
    print("correct!")
    SCORE+=1
else:
    print("Sorry wrong answer :(")
print("YOU GOT "+ str(SCORE)+" QUESTIONS CORRECT:)")
print("FINAL SCORE=",SCORE)
print("YOU GOT "+ str((SCORE/6)*100)+"%.")
print("----------THANK YOU FOR ATTENDING THE QUIZ----------")
