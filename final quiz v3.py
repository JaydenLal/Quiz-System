# Start quiz
def yes_no(question):
    while True:
        response = input(question).lower().strip()

        if response in ("yes", "y"):
            return "yes"
        elif response in ("no", "n"):
            return "no"
        else:
            print("Please enter yes / no")

# Instruction code
def instruction():
    print('''
**** Instructions ****
For each round of the game, you win points by answering questions correctly.  
You must use a, b, c, d to answer.
If you are correct, then your score will increase by the 
number of points that you earned. If you answer a hard question correctly you will get
double the points,

If you lose the round, then you don't get any points.

This quiz grades you based on points at the end.

Good luck.   
    ''')

# Main routine
print()
print("Trivia Questions")
print()

want_instructions = yes_no("Do you want to read the instructions? ")

if want_instructions == "yes":
    instruction()

# Score initialize
score = 0

# Question code
questions = [
    {
        "question": "Q1 Who directed Lord of the Rings?",
        "options": ["A. J. R. R Tolkien", "B. Peter Jackson", "C. Dr Seuss", "D. Steven Spielberg"],
        "answer": "b",
        "correct_message": "Peter Jackson",
        "points": 1
    },
    {
        "question": "Q2 Where was Lord of the Rings Directed?",
        "options": ["A. NL", "B. AU", "C. NZ"],
        "answer": "c",
        "correct_message": "NZ",
        "points": 1
    },
    {
        "question": "Q3 What is the name of the main character?",
        "options": ["A. Sam", "B. Frodo", "C. Fred", "D. Gandalf"],
        "answer": "b",
        "correct_message": "Frodo",
        "points": 1
    },
    {
        "question": "Q4 What NZ city served as the primary filming location for the Shire?",
        "options": ["A. Christchurch", "B. Auckland", "C. Matamata", "D. Wellington"],
        "answer": "c",
        "correct_message": "Matamata",
        "points": 2
    },
    {
        "question": "Q5 When was the first Lord of The Rings filmed?",
        "options": ["A. 2003", "B. 2012", "C. 1999", "D. 1997"],
        "answer": "c",
        "correct_message": "1999",
        "points": 1
    },
    {
        "question": "Q6 What is the name of the special effects and prop company in the movie?",
        "options": ["A. Clockwork Films", "B. NZ Films", "C. FilmFX", "D. Weta Workshop"],
        "answer": "d",
        "correct_message": "Weta Workshop",
        "points": 1
    },
    {
        "question": "Q7 Which New Zealand actor played the role of Éomer?",
        "options": ["A. Karl Urban", "B. Botanical Gardens", "C. Abel Tasman National Park", "D. Wellington"],
        "answer": "a",
        "correct_message": "Karl Urban",
        "points": 1
    },
    {
        "question": "Q8 The lush forest scenes for Lothlórien were filmed in which New Zealand park?",
        "options": ["A. Fiordland National Park", "B. Botanical Gardens", "C. Abel Tasman National Park"],
        "answer": "a",
        "correct_message": "Fiordland National Park",
        "points": 1
    },
    {
        "question": "BONUS! Who illustrated Lord of The Rings?",
        "options": ["A. Peter Jackson", "B. J. R. R. Tolkien", "C. J. K. Rowling", "D. Stephen King"],
        "answer": "b",
        "correct_message": "J. R. R. Tolkien",
        "points": 2
    }
]

# Loop through questions
for q in questions:
    print(f"\n{q['question']}")
    for option in q["options"]:
        print(option)
    answer = input("Enter your answer: ").lower().strip()
    if answer == q["answer"] or answer == q["correct_message"].lower().strip():
        score += q["points"]
        print("You're correct!")
    else:
        print(f"Wrong! It's {q['correct_message']}")

# Final scoring
print('\nYou have scored', score, 'out of 10')
if score == 11:
    print("RANKING: You're a genius!")
elif score >= 7:
    print("RANKING: High Knowledge")
elif score >= 5:
    print("RANKING: Intermediate Knowledge")
else:
    print("RANKING: Low Knowledge")
