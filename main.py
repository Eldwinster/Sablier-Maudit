#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

WELCOME_TEXT = """
Bienvenue au jeu du Sablier Maudit.
"""

RULES_TEXT = """
Voici en quoi ce jeu consiste:

On commence par choisir un temps total pour effectuer un premier tour.
Chaque participant doit finir son tour avant que le sablier ne soit écouler.

À la fin du temps impartie, le sablier est retourné ce qui signifie le début du tour suivant.

Le sablier étant maudit, à chaque tour, perd un peu de son sable.

Plus le sablier se retourne moins vous avez de temps.

Réussirez-vous à battre le sablier ou allez vous succombez sous le poids de sa malédiction ?
"""

hourVar = ""
minVar = ""
secVar = ""
incrementVar = ""
loopVar = ""


def padding(frame):
    for child in frame.winfo_children():
        child.grid_configure(padx=10, pady=10)


def countdown():
    try:
        # get the initial time and convert it in seconds
        tmp_time = hourVar.get() * 3600 + minVar.get() * 60 + secVar.get()
    except:
        print("error")



class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(anchor=tk.CENTER, side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (WelcomePage, SettingsPage, CountdownPage):

            frame = F(container, self)

            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


# first window frame startpage
class WelcomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels
        welcomeLabel = ttk.Label(self, text=WELCOME_TEXT)
        rulesLabel = ttk.Label(self, text=RULES_TEXT)

        welcomeLabel.grid(row=0, column=4)
        rulesLabel.grid(row=1, column=4)

        next_button = ttk.Button(self, text="Suivant",
                                 command=lambda: controller.show_frame(SettingsPage))

        next_button.grid(row=10, column=5)

        quit_button = ttk.Button(self, text="Quitter",
                                 command=lambda: self.quit())

        quit_button.grid(row=10, column=3)

        padding(self)


class SettingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels
        timeLabel = ttk.Label(self, text="Temps initial : ")
        incrementLabel = ttk.Label(self, text="Incrément/Décrément : ")
        loopLabel = ttk.Label(self, text="Nombre de tours : ")

        hourLabel = ttk.Label(self, text="h")
        minLabel = ttk.Label(self, text="m")
        secLabel = ttk.Label(self, text="s")

        # Settings
        global hourVar, minVar, secVar, incrementVar, loopVar
        hourVar = tk.StringVar()
        minVar = tk.StringVar()
        secVar = tk.StringVar()
        incrementVar = tk.StringVar()
        loopVar = tk.StringVar()
        inc = tk.StringVar()
        dec = tk.StringVar()

        # Entries
        hourEntry = ttk.Entry(self, textvariable=hourVar, width=2)
        minEntry = ttk.Entry(self, textvariable=minVar, width=2)
        secEntry = ttk.Entry(self, textvariable=secVar, width=2)
        incrementEntry = ttk.Entry(self, textvariable=incrementVar, width=3)
        loopEntry = ttk.Entry(self, textvariable=loopVar, width=3)

        # Checkbox
        incrementCheckbox = ttk.Checkbutton(self, text="Incrément", variable=inc)
        decrementCheckbox = ttk.Checkbutton(self, text="Décrément", variable=dec)

        # button
        quit_button = ttk.Button(self, text="Quitter",
                                 command=lambda: self.quit())
        apply_button = ttk.Button(self, text="Lancer",
                                  command=lambda: controller.show_frame(CountdownPage))

        # Label placement
        timeLabel.grid(row=0, column=1)
        incrementLabel.grid(row=1, column=1)
        loopLabel.grid(row=2, column=1)

        hourLabel.grid(row=0, column=11)
        minLabel.grid(row=0, column=21)
        secLabel.grid(row=0, column=31)

        # Entries placement
        hourEntry.grid(row=0, column=10)
        minEntry.grid(row=0, column=20)
        secEntry.grid(row=0, column=30)
        incrementEntry.grid(row=1, column=10)
        loopEntry.grid(row=2, column=10)

        # Checkbox placement
        incrementCheckbox.grid(row=1, column=20)
        decrementCheckbox.grid(row=1, column=30)

        # Button placement
        quit_button.grid(row=10, column=0)
        apply_button.grid(row=10, column=40)

        padding(self)


# third window frame page2
class CountdownPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        hourLabel = ttk.Label(
            self,
            textvariable=hourVar,
            width=2,
            font=("Roboto", 100, "")
        )

        minLabel = ttk.Label(
            self,
            textvariable=minVar,
            width=2,
            font=("Roboto", 100, "")
        )

        secLabel = ttk.Label(
            self,
            textvariable=secVar,
            width=2,
            font=("Roboto", 100, "")
        )

        hourLabel.grid(row=2, column=10)
        minLabel.grid(row=2, column=20)
        secLabel.grid(row=2, column=30)

        # button to show frame 2 with text
        # layout2
        quit_button = ttk.Button(self, text="Quitter",
                                 command=lambda: self.quit())

        quit_button.grid(row=10, column=0)

        prev_button = ttk.Button(self, text ="Précédent",
                                 command=lambda: controller.show_frame(SettingsPage))

        # putting the button in its place by
        # using grid
        prev_button.grid(row = 10, column = 100)

        padding(self)

# Driver Code
app = tkinterApp()
app.mainloop()
