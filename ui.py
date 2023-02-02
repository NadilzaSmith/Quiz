from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.screen = Tk()
        self.screen.title("Guess?")
        self.screen.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score = Label(text="Score: 0",fg="white",bg=THEME_COLOR)
        self.score.grid(row=0,column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.text = self.canvas.create_text(150,125,width=280,text="Some Question Text",fill=THEME_COLOR,font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.b_image = PhotoImage(file="images/true.png")
        self.botao1 = Button(image=self.b_image,highlightthickness=0,command=self.right_guess)
        self.botao1.grid(row=2, column=0)

        self.b_image2 = PhotoImage(file="images/false.png")
        self.botao2 = Button(image=self.b_image2,highlightthickness=0,command=self.wrong_guess)
        self.botao2.grid(row=2, column=1)

        self.next_guess()

        self.screen.mainloop()

    def next_guess(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            try_guess = self.quiz.next_question()
            self.canvas.itemconfig(self.text,text=try_guess)
        else:
            self.canvas.itemconfig(self.text, text="You finish the quiz")
            self.botao1.config(state="disabled")
            self.botao2.config(state="disabled")


    def right_guess(self):
        right_guess = self.quiz.check_answer("True")
        self.feedback(right_guess)

    def wrong_guess(self):
        right_guess = self.quiz.check_answer("False")
        self.feedback(right_guess)

    def feedback(self, right_guess):
        if right_guess:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.screen.after(1000,self.next_guess)







