from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    q_obj = Question(q["text"], q["answer"])
    question_bank.append(q_obj)

q = QuizBrain(question_bank)

while q.still_has_question():
    q.next_question()


print(f"Your final score is {q.score}/{len(question_data)}")


