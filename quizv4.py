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
if answer == "New Zealand":
    score = score + 1
    print("You're correct!")
else: print("wrong")

# Question 3
print("MULTICHOICE!")
print("Q3 What is the name of the main character?")
print("A. Sam")
print("B. Frodo")
print("C. Fred")
print("D. Gandalf")
answer = input("Enter your answer: ")
if answer == "B" or answer == "Frodo":
    score = score + 1
    print("You're correct!")
else: print("wrong")

# Question 4
answer = input('Q4 What NZ city served as the primary filming location for the "Shire"? ')
if answer == "Matamata":
    score = score + 1
    print("You're correct!")
else: print("wrong")

# Question 5
print("MULTICHOICE!")
print("Q5 When was the first Lord of The Rings filmed? ")
print("A. 2003")
print("B. 2012")
print("C. 1999")
print("D. 1997")
answer = input("Enter your answer: ")
if answer == "C" or answer == "1999":
    score = score + 1
    print("You're correct!")
else: print("wrong")

# Question 6
answer = input("Q6: What is the name of the New Zealand special effects and prop company "
       "that created many of the creatures and weapons for the film? ")
if answer == "J. R. R. Tolkien":
    score = score + 1
    print("You're correct!")
else: print("wrong")

# Question 7
answer = input("Q7 Which New Zealand actor played the role of Éomer? ")
if answer == "Karl Urban":
    score = score + 1
    print("You're correct!")
else: print("wrong")

# Question 8
print("MULTICHOICE!")
print("Q8 The lush forest scenes for Lothlórien were filmed in which New Zealand park?")
print("A. Fiordland National Park")
print("B. 2012")
print("C. 1999")
print("D. 1997")
answer = input("Enter your answer: ")
if answer == "A" or answer == "Fiordland National Park":
    score = score + 1
    print("You're correct!")
else: print("wrong")


# BONUS
print("--BONUS!--")
print("Who illustrated Lord of The Rings? ")
print("A. J. R. R. Tolkien")
print("B. Peter Jackson")
print("C. J. K. Rowling")
print("D. Stephen King")
answer = input("Enter your answer: ")
if answer == "A" or answer == "J. R. R. Tolkien":
    score = score + 2
    print("You're correct!")
else: print("wrong")

# Point system and rankings
print('You have scored', score, 'out of 10')
if score >= 10:
    print("RANKING: You're a genius!")
elif score >= 7:
    print("RANKING: High Knowledge")
elif score >= 5:
    print("RANKING: Intermediate Knowledge")
elif score <= 4:
    print("RANKING: Low Knowledge")