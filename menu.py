
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import levenshtein_check as lc
import tkinter.messagebox

settings = {}

def run(root):
    global settings
    print("Opening menu...")
    menu_window = tk.Toplevel(root)
    menu_window.title("Trivia Game - settings")
    menu_window.geometry("566x339")
    menu_window.resizable(False, False)


        

    #! main title
    title = ttk.Label(
        menu_window, 
        text="Settings",
        font=("Helvetica", 30, 'bold'),
    )
    title.place(x=10, y=10)

    #! extra info
    instructions = ttk.Label(
        menu_window, 
        text="Select your settings",
        font=("Helvetica", 10, 'bold'),
    )
    instructions.place(x=10, y=50)

    #! set number of players
    number_of_players = ttk.Label(
        menu_window, 
        text="Number of players",
        font=("Helvetica", 10, "bold"),
    )
    number_of_players.place(x=10, y=100)
    number_of_players_input = ttk.Entry(
        menu_window, 
        width=23
    )
    number_of_players_input.place(x=250, y=100)

    #?Ensure number of players isnt more than 5
    def num_players_check(prev_fix=None):

        if (prev_fix != None):
            print('second loop')
            input_value = prev_fix
        else:
            input_value = number_of_players_input.get()
        initial_value = input_value
        try:
            if (input_value == ""):
                input_value = 1
                #input_value = num_players_check(input_value)[1]
                return (False, input_value, initial_value)
            input_value = int(input_value)
            if (input_value > 5):
                input_value = 5
                #input_value = num_players_check(input_value)[1]
                return (False, input_value, initial_value)
            elif (input_value < 1):
                input_value = 1
                #input_value = num_players_check(input_value)[1]
                return (False, input_value, initial_value)
            else:
                return(True, input_value, initial_value)
        except:
            input_value = ''.join(filter(str.isdigit, input_value))  # remove non-numeric characters from the input
            if(len(input_value) < 1): input_value = 1
            else: input_value = int(input_value)
            input_value = num_players_check(input_value)[1]
            print('continued with', input_value)
            return (False, input_value, initial_value)
    
    def dropdown_sanity_check(inputed_value, available_options):
        for option in available_options:
            if option == inputed_value:
                return True
            else:
              possible_value = lc.check_input(inputed_value, available_options)
              return possible_value  


            

    #! Set category
    category = ttk.Label(
        menu_window, 
        text="Category",
        font=("Helvetica", 10),
    )
    category.place(x=10, y=150)
    categories = [
        "Any Category",
        "General Knowledge",
        "Entertainment: books",
        "Entertainment: film",
        "Entertainment: music",
        "Entertainment: musicals & theaters",
        "Entertainment: television",
        "Entertainment: video games",
        "Entertainment: board games",
        "Science & nature",
        "Science: computers",
        "Science: mathematics",
        "Mythology",
        "Sports",
        "Geography",
        "History",
        "Politics",
        "Art",
        "Celebrities",
        "Animals"
    ]

    category_combo_box = ttk.Combobox(menu_window, values= categories)
    category_combo_box.current(0)
    category_combo_box.place(x=250, y=150)


    #! set Difficulty
    difficulty = ttk.Label(
        menu_window, 
        text="Difficulty",
        font=("Helvetica", 10),
    )
    difficulty.place(x=10, y=200)
    difficulty_levels = [
        'Easy 🤡',
        'Expert 🥸',
        'Awesome 😎'
    ]
    difficulty_combo_box = ttk.Combobox(menu_window, values= difficulty_levels)
    difficulty_combo_box.current(0)
    difficulty_combo_box.place(x=250, y=200)

    #! set type
    type = ttk.Label(
        menu_window, 
        text="Type",
        font=("Helvetica", 10),
    )
    type.place(x=10, y=250)
    type_levels = [
        'Any',
        'Multiple choice',
        'True or false'
    ]
    type_combo_box = ttk.Combobox(menu_window, values= type_levels)
    type_combo_box.current(0)
    type_combo_box.place(x=250, y=250)


    def report_input_err(err, initial_val, new_val, reason):
        err_string =  f"the value of {err} was changed to {new_val} from {initial_val} this could be because {reason}"
        messagebox.showerror("Adjustents to your settings", err_string)

    def apply_settings():
        global settings
        check_results = num_players_check(None)
        num_of_players = number_of_players_input.get()
        #?checking text input
        if (check_results[0] is not True):
            report_input_err('number of players', check_results[2], check_results[1], "\n 1. you entered a letter\n2. the value was too large \n3. the value was too small\n4. you left the field blank")
            num_of_players = check_results[1]
        #?checking combo boxes
        settings = {
            'players': num_of_players,
            'category': category_combo_box.get(),
            'difficulty': difficulty_combo_box.get(),
            'type': type_combo_box.get()
        }
        print(settings['category'])
        settings['category'] = dropdown_sanity_check(settings['category'], categories)
        settings['difficulty'] = dropdown_sanity_check(settings['difficulty'], difficulty_levels)
        settings['type'] = dropdown_sanity_check(settings['type'], type_levels)
        menu_window.destroy()


    #! complete settings
    ok_button = ttk.Button(
        menu_window,
        text= "Apply",
        command=apply_settings,
    )
    ok_button.place(x=200, y=300)

    menu_window.wait_window()
    # design menu page
    return settings
#run()