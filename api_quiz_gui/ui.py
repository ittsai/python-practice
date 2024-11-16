
from tkinter import *
import random
import html


THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, questions):
        self.question_data = questions
        self.data = {}
        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.label = Label(text="Score 0", fg="white", bg=THEME_COLOR)
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text= self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill="black",
            font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady= 50)
        true_img = PhotoImage(file="true.png")
        false_img = PhotoImage(file="false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.get_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.get_false)
        self.false_button.grid(row=2, column=1)
        self.get_question()
        self.window.mainloop()

    def get_question(self):
        self.canvas.config(bg=THEME_COLOR)
        if len(self.question_data) > 0:
            self.data = random.choice(self.question_data)
            self.question_data.remove(self.data)
            q_text = html.unescape(self.data["question"])
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")

        else:
            self.canvas.itemconfig(self.question_text, text="No more questions")

    def get_true(self):
        self.button_disabled()
        correct_answer = self.data["correct_answer"]
        if correct_answer == "True":
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)
        self.button_enabled()


    def get_false(self):
        self.button_disabled()
        correct_answer = self.data["correct_answer"]
        if correct_answer == "False":
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)
        self.button_enabled()

    def button_disabled(self):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

    def button_enabled(self):
        self.true_button.config(state="active")
        self.false_button.config(state="active")


