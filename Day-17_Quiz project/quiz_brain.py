# TODO 1: Import Zone
from data import question_data
from question_model import Question


# TODO 2: Import Zone
class QuizBrain:

    def __init__(self, Question_List):
        self.Question_Number = 0  # It is a parameter that gives index of list to fetch data
        self.Question_List = Question_List  # List with data of Questions

    def Ask_Question(self):
        User_Answer = input(f"Q.{self.Question_Number + 1} {self.Question_List[self.Question_Number].question} (True/False) ? : ").capitalize() # Asks Question
        if User_Answer == self.Question_List[self.Question_Number].answer: # Returns True or False
            self.Question_Number += 1
            return True
        else:
            self.Question_Number += 1
            return False
