# This prototype code asks questions to player
# Player has to answer them correctly
# Question code
answer = input("Q1 Who directed Lord of the Rings? ")
score = 0
if answer == "Peter Jackson":
    score = score + 1
    print("You're correct!")
else: print("wrong")

# Question 2
answer = input("Q2 Where was Lord Of the Rings Directed? ")
if answer == "New Zealand" or "NZ":
    score = score + 1
    print("You're correct!")
else: print("wrong")

# Point system and rankings
print('You have scored', score, 'out of 10')
if score == 2:
    print("RANKING: You're smart!")
if score <= 1:
    print("RANKING: You're dumb!")