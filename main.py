#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import time
import datetime

HOUR = 3600
MINUTE = 60
DECREMENT = 1

loop = 9
hours = 0
minutes = 0
seconds = 10

NUM_FONT = ("Latin Modern Math", 250, "bold")
TXT_FONT = ("FiraCode Nerd Font", 150, "")
PADDING = '0 0 0 0'
BACKGROUND = 'black'
FOREGROUND = 'white'

def countdown():
    global loop
    turnFrame = ttk.Frame(root, padding=PADDING)
    turnFrame.grid(row=0, column=0)
    turnFrame.columnconfigure(0, weight=1)
    turnFrame.rowconfigure(0, weight=1)

    turnLabel1 = ttk.Label(
        turnFrame,
        text='Tour: ',
        font=TXT_FONT,
        background=BACKGROUND,
        foreground=FOREGROUND
    )

    turnLabel2 = ttk.Label(
        turnFrame,
        textvariable=turnVar,
        font=TXT_FONT,
        background=BACKGROUND,
        foreground=FOREGROUND
    )

    turnLabel3 = ttk.Label(
        turnFrame,
        text='/9',
        font=TXT_FONT,
        background=BACKGROUND,
        foreground=FOREGROUND
    )

    turnLabel1.grid(row=0, column=0)
    turnLabel2.grid(row=0, column=1)
    turnLabel3.grid(row=0, column=2)

    countdownFrame = ttk.Frame(root, padding=PADDING)
    countdownFrame.grid(row=1, column=0)
    countdownFrame.columnconfigure(0, weight=1)
    countdownFrame.rowconfigure(0, weight=1)


    hourLabel = ttk.Label(
        countdownFrame,
        textvariable=hourVar,
        font=NUM_FONT,
        background=BACKGROUND,
        foreground=FOREGROUND
    )
    sep1Label = ttk.Label(
        countdownFrame,
        text=":",
        font=NUM_FONT,
        background=BACKGROUND,
        foreground=FOREGROUND
    )
    minLabel = ttk.Label(
        countdownFrame,
        textvariable=minVar,
        font=NUM_FONT,
        background=BACKGROUND,
        foreground=FOREGROUND
    )
    sep2Label = ttk.Label(
        countdownFrame,
        text=":",
        font=NUM_FONT,
        background=BACKGROUND,
        foreground=FOREGROUND
    )
    secLabel = ttk.Label(
        countdownFrame,
        textvariable=secVar,
        font=NUM_FONT,
        background=BACKGROUND,
        foreground=FOREGROUND
    )

    hourLabel.grid(row=1, column=0)
    sep1Label.grid(row=1, column=1)
    minLabel.grid(row=1, column=2)
    sep2Label.grid(row=1, column=3)
    secLabel.grid(row=1, column=4)


    try:
        tmp = int(hourVar.get()) * HOUR + int(minVar.get()) * MINUTE + int(secVar.get())
        initial_timer = tmp
        tempsVariable = int(hourVar.get()) * HOUR + int(minVar.get()) * MINUTE + int(secVar.get())

        timeMem = tempsVariable

        timeToDecrement = tempsVariable

    except:
        print("Please input the right value")

    while loop >= 0:
        mins, secs = divmod(tempsVariable, MINUTE)
        hours = 0

        if loop == 1:
            turnLabel1.destroy()
            turnLabel2.destroy()
            turnLabel3.destroy()

            lastTurnLabel = ttk.Label(
                turnFrame,
                text='Dernier Tour !',
                font=NUM_FONT,
                background=BACKGROUND,
                foreground='red'
            )
            lastTurnLabel.grid(row=0, column=0)

        if mins > MINUTE:
            hours, mins = divmod(mins, MINUTE)

        hourVar.set("{0:2d}".format(hours))
        minVar.set("{0:2d}".format(mins))
        secVar.set("{0:2d}".format(secs))
        turnVar.set("{0:2d}".format(loop))

        # tentative de formatage des variables en text sans succes
        # time_string = f'{hourVar:2d}:{minVar:2d}:{hourVar:2d}'
        # label.config(text=time_string)

        root.update()
        time.sleep(1)

        if (tempsVariable == 10):
            hourLabel.config(foreground="red")
            sep1Label.config(foreground="red")
            minLabel.config(foreground="red")
            sep2Label.config(foreground="red")
            secLabel.config(foreground="red")

        if (tempsVariable == 0):
            timeToDecrement -= DECREMENT
            # impossible de à mettre freeze le timer
            loop -= 1
            tempsVariable = timeToDecrement
        if (tempsVariable < 0):
            tempsVariable = timeMem

        tempsVariable -= 1

        if (loop == 0):
            tk.messagebox.showinfo("Timer: ", "Time's up")

    # while tmp_time > 0:
    #     timer = datetime.timedelta(seconds=tmp_time)


# main window
root = tk.Tk()
root.title('Sablier Maudit')
root.geometry("800x600")
root.attributes("-fullscreen", True)
root.resizable(True, True)
root.configure(background=BACKGROUND)

root.after(100, countdown)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

hourVar = tk.StringVar()
minVar = tk.StringVar()
secVar = tk.StringVar()
turnVar = tk.StringVar()

hourVar.set(hours)
minVar.set(minutes)
secVar.set(seconds)
turnVar.set(loop)

# tentative de conversion en string pour le label
# t = "%2d:%2d:2%d"(hourVar,minVar,secVar)

root.mainloop()
