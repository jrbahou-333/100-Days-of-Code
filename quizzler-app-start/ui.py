from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.is_right = None

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(background=THEME_COLOR, pady=20, padx=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(background="white", height=250, width=300)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Press a Button",
                                                     width=280,
                                                     font=FONT,
                                                     fill="black")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.tick_img = PhotoImage(file="./images/true.gif")
        self.tick_button = Button(image=self.tick_img, command=self.check_answer_true)
        self.tick_button.grid(column=0, row=2)

        self.cross_img = PhotoImage(file="./images/false.gif")
        self.cross_button = Button(image=self.cross_img, command=self.check_answer_false)
        self.cross_button.grid(column=1, row=2)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, fill="black")

        else:
            self.canvas.config(bg="white")
            self.canvas.itemconfig(self.question_text, text=f"Quiz Complete\n\nFinal Score: {self.quiz.score}/10", fill="black")
            self.tick_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def check_answer_true(self):
        self.is_right = self.quiz.check_answer("True")
        self.give_feedback(self.is_right)


    def check_answer_false(self):
        self.is_right = self.quiz.check_answer("False")
        self.give_feedback(self.is_right)



    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")

        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")

        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_q)


