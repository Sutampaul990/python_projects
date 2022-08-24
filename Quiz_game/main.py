
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
    
Quiz=QuizBrain(question_bank)  
while Quiz.still_has_questions():#if quiz still has question remaining---- 
    Quiz.next_question()
    
print("You have completed the Quiz.")
print(f"Your final score was : {Quiz.score}/{Quiz.question_number} .")