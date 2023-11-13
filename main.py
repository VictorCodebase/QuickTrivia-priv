
# ttkthemes
import tkinter as tk
import menu as menu
import construct as construct
from tkinter import messagebox
import conn as conn
import sys
import os

window = tk.Tk()
window.title("Quick Trivia game")
window.geometry("566x339")
window.resizable(False, False)
conn.init()
trivia = 'Open settings to set up a new level'
settings_is_open = False
settings = {}
default_value = 1
players = 1
category = 0
difficulty = ''
type = ''


#print("menu:", menu.run(window))

def main():
    global settings, players, category, difficulty, type, trivia, settings_is_open
    print("main")
    trivia_question = tk.StringVar()
    trivia_question.set(trivia)

    def get_settings():
        global settings_is_open
        if (settings_is_open is True):
            messagebox.showerror('Menu instance running', 'An instance of the menu is running in the background. Close it or apply settings to open')
            return
        else:
            settings_is_open = True
        settings = menu.run(window)
        print(settings)
        settings_is_open = False
        players = settings['players']
        category = settings['category']
        difficulty = settings['difficulty']
        type = settings['type']



    settings_button = tk.Button(
        window, 
        text="Create new level", 
        width=20,
        command=get_settings,
    )
    settings_button.place(x=400, y=300)

    title = tk.Label(
        window, 
        text="Quick Trivia Game",
        font=("Helvetica", 30, 'bold'),
    )
    title.place(x=10, y=10)

    trivia_question_label = tk.Label(
        window, 
        textvariable=trivia_question,
        font=("Helvetica", 10, 'bold'),
        wraplength=600,  
        #highlightbackground="orange",
        #highlightthickness=2,
    )
    trivia_question_label.place(x=10, y=100)


    construct.construct_lables(
        window,
        texts=['player - 1'], # texts
        x=420, # starting x
        y=80, # starting y
        font=["Helvetica", 10, 'normal'], # font details
        bg="white", # bg
        fg="black", # fg
        highlightbg='orange',
        highlight_thickness=2,
        width=10,
        bwidth=2,
        anchor="w", # anchor 
        isBold=False, # isBold
        x_increment=0, # x_increment
        y_increment=50, # y_increment
    )

    construct.construct_buttons(
        window,
        texts=["A", "B", "C", "D"], 
        x=10, 
        y=200, 
        width=10, 
        height=2, 
        font="Helvetica",
        bg="white",
        fg="black",
        highlightbg="grey", 
        highlight_thickness=2, 
        bwidth=2, 
        anchor="w", 
        x_increment=100,
        y_increment=0,
        stringVar=True,
        releif='groove'
    )
    def fetch_questions():
        global players, category, difficulty, type
        print("fetching questions")
        if (players == 0): players = default_value
        if (category == 0): category = default_value
        if (difficulty == ''): difficulty = 'easy'
        if (type == ''): type = 'multiple'
        
        conn.fetchQuestions(
            quantity=players * 5, 
            category=category, 
            difficulty=difficulty, 
            type=type
        )
    #fetch_questions()


    window.mainloop()

if __name__ == "__main__":
    main()

