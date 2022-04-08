import random 

def gamewin(comp,you):
    # If two values are equal, declare a tie
    if comp ==you:
        return None
    #Check for all possibilities when computer chose s
    elif comp == 's':
        if you =='sc':
            return False
        elif you=='p':
            return True
    #Check for all possibilities when computer chose sc
    elif comp == 'sc':
        if you =='p':
            return False
        elif you=='s':
            return True
    #Check for all possibilities when computer chose p
    elif comp == 'p':
        if you =='s':
            return False
        elif you=='sc':
            return True

print("Comp Turn: Stone(s) Paper(p) Scissors(sc)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp ='s'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp ='sc'
you = input("Yours Turn: Stone(s) Paper(p) Scissors(sc)?")

a =gamewin(comp , you)

print(f"Computer chose {comp}  ")
print(f"you chose {you}  ")
if a == None:
    print("The game is a tie!")
elif a:
    print("you win!")
else:
    print("You lose!")