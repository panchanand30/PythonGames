class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_questions_left(self):
        if self.question_number < len(self.question_list):
            return True
        elif self.question_number == len(self.question_list):
            print(f"You have completed the quiz.\nYour final score was: {self.score}/{self.question_number}")
            self.question_number += 1
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print(f"You got it right. \nThe correct answer was {correct_answer}")
            self.score += 1
            print(f"Your current score is: {self.score}\n")
            return self.still_questions_left()
        else:
            print(f"That's wrong. The correct answer was: {correct_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}\n")
