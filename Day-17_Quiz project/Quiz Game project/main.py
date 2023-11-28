# TODO 1: Import Zone
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# TODO 2: Creating Question Bank
Question_Bank = []  # Creating question bank list by Question class. so, that Question & answers can be called by attributes
for n in question_data:
    Question_Bank.append(Question(n["text"], n["answer"]))

# TODO 3: Implementing Quiz brain
Quiz = QuizBrain(Question_Bank)

Score = 0
Is_Loop = True
while Is_Loop:
    print(f"Your current score is {Score}")
    Answer = (Quiz.Ask_Question())
    print(Answer)
    if Answer:
        Score += 1
    elif Answer == False:
        print(f"Sorry, The Answer is Wrong, & Your final score is {Score}")
        Is_Loop = False
    if Score >= len(Question_Bank):
        Is_Loop = False
        print(f"Congrats, You answered all Questions. & Your score is {Score}")