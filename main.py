import tkinter as tk
from tkinter import messagebox, ttk
from ttkbootstrap import Style
from quiz_data import quiz_data

def show_question():
    question = quiz_data[current_question]
    qs_label.config(text=question["question"])

    choices = question["choices"]
    for i in range(4):
        choice_btns[i].config(text=choices[i], state="normal")

    feedback_label.config(text="")
    next_btn.config(state="disabled")

def check_answer(choice):
    question = quiz_data[current_question]
    selected_choice = choice_btns[choice].cget("text")

    if selected_choice == question["answer"]:
        global score
        score += 1
        score_label.config(text="Score: {}/{}".format(score, len(quiz_data)))
        feedback_label.config(text="Correct!", foreground="green")
    else:
        feedback_label.config(text="Incorrect!", foreground="red")
    
    for button in choice_btns:
        button.config(state="disabled")
    next_btn.config(state="normal")

def next_question():
    global current_question
    current_question += 1

    if current_question < len(quiz_data):
        show_question()
    else:
        messagebox.showinfo("Quiz Completed",
                            "Quiz Completed! Final score: {}/{}".format(score, len(quiz_data)))
        root.destroy()

root = tk.Tk()
root.title("Quiz App")
root.geometry("600x600")
style = Style(theme="flatly")

root.configure(bg=style.colors.primary)

title_label = ttk.Label(
    root,
    text="Welcome to the Quiz App",
    font=("Helvetica", 24, "bold"),
    foreground=style.colors.light,
    background=style.colors.primary,
    padding=20
)
title_label.pack()

separator = ttk.Separator(root, orient='horizontal')
separator.pack(fill='x', padx=20, pady=5)

qs_label = ttk.Label(
    root,
    anchor="center",
    wraplength=500,
    padding=20,
    font=("Helvetica", 20),
    foreground=style.colors.light,
    background=style.colors.primary
)
qs_label.pack(pady=10)

choice_btns = []
for i in range(4):
    button = ttk.Button(
        root,
        command=lambda i=i: check_answer(i),
        style="Custom.TButton"
    )
    button.pack(pady=10)
    choice_btns.append(button)

feedback_label = ttk.Label(
    root,
    anchor="center",
    padding=10,
    font=("Helvetica", 16),
    background=style.colors.primary
)
feedback_label.pack()

score = 0

score_label = ttk.Label(
    root,
    text="Score: 0/{}".format(len(quiz_data)),
    anchor="center",
    padding=10,
    font=("Helvetica", 16),
    foreground=style.colors.light,
    background=style.colors.primary
)
score_label.pack()

next_btn = ttk.Button(
    root,
    text="Next",
    command=next_question,
    state="disabled",
    style="Custom.TButton"
)
next_btn.pack(pady=20)

current_question = 0

show_question()

style.configure("Custom.TButton", font=("Helvetica", 14), foreground=style.colors.light, background=style.colors.secondary)

root.mainloop()
