# TODO: 1. asking the questions
# TODO: 2. checking if the answer was correct
# TODO: 3. checking if we're the end of the quiz
# from question_model import Question
# from data import question_data


class QuizBrain:
    def __init__(self, questions_bank):
        """initialise a quiz brain"""
        # list of question objects
        self.question_number = 0
        self.questions_list = questions_bank
        self.score = 0

    def still_has_questions(self):
        """
        checks if there are any questions left not answered yet
        :return: True if there are any questions left, otherwise - False
        """
        return self.question_number < len(self.questions_list)

    def next_question(self):
        """
        retrieve current question, gets answer, and check if it's correct
        :return:
        """
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
        checks if user answer correctly on a question
        :param correct_answer: correct answer (expected one)
        :param user_answer: given answer from user input
        :return:
        """
        is_correct = user_answer.lower() == correct_answer.lower()
        if is_correct:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")


'''
    def __init__(self):
        """initialise a quiz brain"""
        # list of question objects
        self.question_number = 0
        self.question_bank = []
        self.initialize_q_bank()
        self.correct_answers = 0

    def next_question(self):

    def initialize_q_bank(self):
        """iterates question_data (list) and initialises a question bank"""
        for question in question_data:
            # the question (str)
            question_text = question["text"]
            # the answer (str) - "True" or "False"
            question_answer = question["answer"]
            # Creates new instance of Question
            q_obj = Question(q_text=question_text, q_answer=question_answer)
            # adds question to the question bank
            self.question_bank.append(q_obj)

    def ask_questions(self):
        """
        questions to ask from question_bank
        :return:
        """
        print("Welcome to Quiz Brain. Please answer some questions..")
        c = 0
        for q_obj in self.question_bank:
            if isinstance(q_obj, Question):
                c += 1
                print(f"Question {c}:")
                # prompt the user to answer a question
                user_answer = input(f"{q_obj.text} True/False? ")
                if is_correct_ans(expected_answer=q_obj.answer, answer=user_answer):
                    self.correct_answers += 1

    def show_score(self):
        """display num of correct answers, and final score of the quiz"""
        final_score = int(self.correct_answers * 100 / len(self.question_bank))
        print(f"You have answered {self.correct_answers} out of {len(self.question_bank)} correctly")
        print(f"your score for Quiz Brain is: {str(final_score)}")


def is_correct_ans(expected_answer, answer):
    """
    checks if user answer correctly on a question
    :param expected_answer: real answer (expected one)
    :param answer: given answer from user input
    :return: True for correct answer, otherwise False
    """
    if answer == expected_answer:
        return True
    return False

'''
