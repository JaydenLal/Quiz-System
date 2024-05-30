# checks users enter yes (y) or no (n)
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks user response, question
        # repeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instruction():
    print('''

**** Instructions ****
For each round of the game, you win points by answering questions correctly.  
The winner of the round is the one who gets 10 points.

If you win the round, then your score will increase by the 
number of points that you earned. If you answer a hard question correctly
you will get double the points,

 If you lose the round, then you don't get any points.

 Your goal is to try to get to the target score.

 Good luck.   

    ''')


# Main routine
print()
print("Trivia Questions")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")