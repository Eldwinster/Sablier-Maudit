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


def padding(frame):
    for child in frame.winfo_children():
        child.grid_configure(padx=10, pady=10)


class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

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

        # Settings
        hourVar = tk.IntVar()
        minVar = tk.IntVar()
        secVar = tk.IntVar()
        incrementVar = tk.IntVar()
        loopVar = tk.IntVar()

        # Entries
        hourEntry = ttk.Entry(self, textvariable=hourVar, width=3)
        minEntry = ttk.Entry(self, textvariable=minVar, width=3)
        secEntry = ttk.Entry(self, textvariable=secVar, width=3)
        incrementEntry = ttk.Entry(self, textvariable=incrementVar, width=3)
        loopEntry = ttk.Entry(self, textvariable=loopVar, width=3)

        # Label placement
        timeLabel.grid(row=0, column=1)
        incrementLabel.grid(row=1, column=1)
        loopLabel.grid(row=2, column=1)

        # Entries placement
        hourEntry.grid(row=0, column=2)
        minEntry.grid(row=0, column=3)
        secEntry.grid(row=0, column=4)
        incrementEntry.grid(row=1, column=2)
        loopEntry.grid(row=2, column=2)

        quit_button = ttk.Button(self, text="Quitter",
                                 command=lambda: self.quit())
        quit_button.grid(row=10, column=0)
        padding(self)


# third window frame page2
class CountdownPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2")
        label.grid(row = 0, column = 4)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(SettingsPage))

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(WelcomePage))

        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1)

        padding(self)

# Driver Code
app = tkinterApp()
app.mainloop()
