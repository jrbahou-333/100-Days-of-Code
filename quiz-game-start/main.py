from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    q_text = question["question"]
    q_answer = question["correct_answer"]
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Quiz complete")
print(f"You scored: {quiz.score}/{quiz.question_number} ")