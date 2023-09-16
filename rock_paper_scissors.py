import random
user_wins=0
comp_wins=0
options=["rock","paper","scissors"]

while True:
    user_input=input("type rock/paper/scissors or Q to quit: ").lower()
    if user_input=="q":
        break
    if user_input not in options:
        continue
    random_number=random.randint(0,2)
    #rock is 0 paper is 1 scissors is 2
    comp_quess=options[random_number]
    print("computer picked", comp_quess+".")
    if user_input=="rock" and comp_quess=="scissors":
        print("you won!")
        user_wins+=1
       

    elif user_input=="paper" and comp_quess=="rock":
        print("you won!")
        user_wins+=1
     

    elif user_input=="scissors" and comp_quess=="paper":
        print("you won!")
        user_wins+=1
       
    else:
        print("You Lost:(")
        comp_wins+=1



print("You won ",user_wins, "times.")
print("The computer won", comp_wins," times")
print("Bye See you Next Time!!!")
