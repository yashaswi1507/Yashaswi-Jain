import random
import math
#code for input 
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter the Upper Bond: "))
#generating random number between upper and lower bond
x = random.randint(lower, upper)
print("\n\tYou've only ", round(math.log(upper-lower+1, 2)), "chance to guss the number!\n")
#initializing the number of guesses.
count=0
#for calculation of minimum number of gusses depends upon range
while count< math.log(upper-lower+1, 2):
    count+=1
    #take gussing number as input
    guess=int(input("Guess a number: "))
    #condition test
    if x==guess:
        print("congratulation you did it in ", count, "try")
        break
    elif x>guess:
        print("you guessed small number!")
    elif x<guess:
        print("you guessed large number!")
        
if count>=math.log(upper-lower+1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next Time!")
        