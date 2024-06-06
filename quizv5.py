# This prototype code asks questions to player
# Player has to answer them correctly
# Question code
print("Lord of the Rings Quiz")
answer = input("\nQ1 Who directed Lord of the Rings? ")
score = 0
if answer == "Peter Jackson":
    score = score + 1
    print("You're correct!")
else: print("Wrong! It's Peter Jackson")

# Question 2
answer = input("\nQ2 Where was Lord of the Rings Directed? ")
if answer == "New Zealand":
    score = score + 1
    print("You're correct!")
else: print("Wrong! It was directed in New Zealand")

# Question 3
print("\nMULTICHOICE!")
print("Q3 What is the name of the main character?")
print("A. Sam")
print("B. Frodo")
print("C. Fred")
print("D. Gandalf")
answer = input("Enter your answer: ")
if answer == "B" or answer == "Frodo":
    score = score + 1
    print("You're correct!")
else: print("Wrong! It's Frodo")

# Question 4
answer = input('\nQ4 What NZ city served as the primary filming location for the Shire? ')
if answer == "Matamata":
    score = score + 2
    print("You're correct!")
else: print("Wrong! The correct answer is Matamata")

# Question 5
print("\nMULTICHOICE!")
print("Q5 When was the first Lord of The Rings filmed? ")
print("A. 2003")
print("B. 2012")
print("C. 1999")
print("D. 1997")
answer = input("Enter your answer: ")
if answer == "C" or answer == "1999":
    score = score + 1
    print("You're correct!")
else: print("Wrong! It was 1999")

# Question 6
answer = input("\nQ6: What is the name of the New Zealand special effects and prop company "
       "that created many of the creatures and weapons for the film? ")
if answer == "Weta Workshop":
    score = score + 1
    print("You're correct!")
else: print("Wrong! It was Weta Workshop")

# Question 7
answer = input("\nQ7 Which New Zealand actor played the role of Éomer? ")
if answer == "Karl Urban":
    score = score + 1
    print("You're correct!")
else: print("Wrong! It's Karl Urban")

# Question 8
print("\nMULTICHOICE!")
print("Q8 The lush forest scenes for Lothlórien were filmed in which New Zealand park?")
print("A. Fiordland National Park")
print("B. Botanical Gardens")
print("C. Abel Tasman National Park")
answer = input("Enter your answer: ")
if answer == "A" or answer == "Fiordland National Park":
    score = score + 1
    print("You're correct!")
else: print("Wrong! It was Fiordland National Park")


# BONUS
print("\n--BONUS!--")
print("Who illustrated Lord of The Rings? ")
print("A. J. R. R. Tolkien")
print("B. Peter Jackson")
print("C. J. K. Rowling")
print("D. Stephen King")
answer = input("Enter your answer: ")
if answer == "A" or answer == "J. R. R. Tolkien":
    score = score + 2
    print("You're correct!")
else: print("Wrong! It was J. R. R. Tolkien")

# Point system and rankings
print('\nYou have scored', score, 'out of 10')
if score >= 10:
    print("RANKING: You're a genius!")
elif score >= 7:
    print("RANKING: High Knowledge")
elif score >= 5:
    print("RANKING: Intermediate Knowledge")
elif score <= 4:
    print("RANKING: Low Knowledge")