import random
top_range=input("Enter a number: ")
if top_range.isdigit():
    top_range=int(top_range)
    if int(top_range)<=0:
        print("Please enter a number greater than Zero next time.")
        quit()
else:
    print("Please enter a number next time")
    quit()

random_number=random.randint(0,top_range)
count=0
while True:
    count+=1
    user_quess=input("Make a quess: ")
    if user_quess.isdigit():
        user_quess=int(user_quess)
    else:
        print("Please enter a number next time")
        continue
    if user_quess==random_number:
        print("YOU GOT RIGHT!!")
        break
    
    elif user_quess>random_number:
        print("You got it wrong BUT Your quess was above the correct answer !!!")
    else:
        print("You got it wrong BUT Your quess was below the correct answer !!!")
print("You got it in", count, "quesses.")
