from question_model import Question
from data import question_data, open_tdb_questions
from quiz_brain import QuizBrain

"""
# new_q = Question("2+3=5", "True")
# print(new_q.text)
# print(new_q.answer)

question_bank = [
    Question("2+3=5", "True"),
    Question("30 < 28", "False"),
    Question("Does Elon Musk Owns Tesla?", "True"),
]

for i in range(0, len(question_bank)):
    print(f"question {str(i+1)}: {question_bank[i].text}")
    print(f"answer {str(i+1)}: {question_bank[i].answer} \n")
# ------
question_bank = []
for q in question_data:
    q_obj = Question(q_text=q["text"], q_answer=q["answer"])
    question_bank.append(q_obj)
    print(q_obj.text, " --> ", q_obj.answer)

print(question_bank)
print(question_bank[0].text)
"""
if __name__ == '__main__':
    # creates a QuizBrain obj
    # my_quiz = QuizBrain()
    # my_quiz.ask_questions()
    # my_quiz.show_score()
    question_bank = []
    for q in question_data:
        q_obj = Question(q_text=q["text"], q_answer=q["answer"])
        question_bank.append(q_obj)

    my_quiz = QuizBrain(questions_bank=question_bank)
    while my_quiz.still_has_questions():  # while there are any questions left
        my_quiz.next_question()
    print("You've completed the quiz.")
    print(f"Your final score was: {my_quiz.score}/{my_quiz.question_number}")
    # current_question = my_quiz.next_question()
    # user_answer = input(f"Q.{my_quiz.question_number+1}: {current_question.text} (True/False)?: ")

    # some trivia questions from The Open Trivia Database (category - Science: Computers)
    open_tdb_bank = []
    for q in open_tdb_questions["results"]:
        q_obj = Question(q_text=q["question"], q_answer=q["correct_answer"])
        open_tdb_bank.append(q_obj)

    open_tdb_quiz = QuizBrain(questions_bank=open_tdb_bank)
    print("\n\nOpen Trivia Database Quiz")
    while open_tdb_quiz.still_has_questions():  # while there are any questions left
        open_tdb_quiz.next_question()
    print("You've completed the Open Trivia quiz.")
    print(f"Your final score was: {open_tdb_quiz.score}/{open_tdb_quiz.question_number}")
