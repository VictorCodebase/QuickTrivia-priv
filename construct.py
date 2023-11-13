from tkinter import *

# a method to create multiple Labels
def construct_lables(window, texts=[], x=0, y=0, width=20, height=10, font=['ariel', 10, 'normal'], bg='white', isBold = False, fg='black', highlightbg='blue', highlight_thickness=1, bwidth=1, anchor='w', x_increment=0, y_increment=0, stringVar=False, releif='flat'):
    # let font be a list of all font attributes
    if type(font) != list:
        font = ["Inter", 10, 'normal']

    for text in texts:
        Label(
            window,
            text=text,
            bg=bg,
            fg=fg,
            width=width,
            font=(font[0], font[1], font[2] if isBold else ''),
            anchor=anchor,
            borderwidth=bwidth,
            highlightthickness=highlight_thickness,
            highlightbackground=highlightbg, 
            relief=releif,
        ).place(x=x, y=y)
        y += y_increment
        x += x_increment


# a method to create multiple Radiobuttons
def construct_radio_buttons(window, texts=[], x=0, y=0, font=['ariel', 10, 'normal'], bg="white", fg="black", anchor="w", x_increment=0, y_increment=0):
    for text in texts:
        Radiobutton(
            window,
            text=text,
            bg=bg,
            fg=fg,
            font=font,
            anchor=anchor
        ).place(x=x, y=y)
        y += y_increment
        x += x_increment

        

def construct_buttons(window, texts=[], x=0, y=0, width=20, height=10, font=['ariel', 10, 'normal'], bg='white', fg='black', highlightbg='blue', highlight_thickness=1, bwidth=1, anchor='w', x_increment=0, y_increment=0, stringVar=False, releif='raised'):
    buttons = []
    if type(font) != list:
        font = [font, 10, 'normal']
    if stringVar:
        for text in texts:
            var = StringVar()
            var.set(text)
            button = Button(
                window,
                textvariable=var,
                bg=bg,
                width=width,
                height=height,
                fg=fg,
                font=(font[0], font[1], font[2]),
                borderwidth=bwidth,
                highlightthickness=highlight_thickness,
                highlightbackground=highlightbg, 
                relief=releif,
                anchor=anchor,
            )
            button.place(x=x, y=y)
            y += y_increment
            x += x_increment

            buttons += [button]
        return buttons
    for text in texts:
        label = Label(
            window,
            text=text,
            bg=bg,
            width=width,
            height=height,
            fg=fg,
            font=font,
            borderwidth=bwidth,
            highlightthickness=highlight_thickness,
            highlightbackground=highlightbg, 
            relief=releif,
            anchor=anchor,
        )
        label.place(x=x, y=y)
        y += y_increment
        x += x_increment

        buttons += [label]
    return buttons