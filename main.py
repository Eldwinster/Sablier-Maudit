#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import time
import datetime

HOUR = 3600
MINUTE = 60
DECREMENT = 10

FONT = ("Arial", 200)

def countdown():
    paramFrame = ttk.Frame(root, padding='3 3 12 12')
    paramFrame.grid(row=0, column=0)
    paramFrame.columnconfigure(0, weight=1)
    paramFrame.rowconfigure(0, weight=1)

    hourLabel = ttk.Label(paramFrame, textvariable=hourVar, font=FONT)
    minLabel = ttk.Label(paramFrame, textvariable=minVar, font=FONT)
    secLabel = ttk.Label(paramFrame, textvariable=secVar, font=FONT)
    sep1Label = ttk.Label(paramFrame, text=":", font=FONT)
    sep2Label = ttk.Label(paramFrame, text=":", font=FONT)

    hourLabel.grid(row=0, column=0)
    sep1Label.grid(row=0, column=1)
    minLabel.grid(row=0, column=2)
    sep2Label.grid(row=0, column=3)
    secLabel.grid(row=0, column=4)


    try:
        tmp = int(hourVar.get()) * HOUR + int(minVar.get()) * MINUTE + int(secVar.get())
        initial_timer = tmp
    except:
        print("Please input the right value")

    while initial_timer > 0:
        mins, secs = divmod(tmp, MINUTE)
        hours = 00

        if mins > MINUTE:
            hours, mins = divmod(mins, MINUTE)

        hourVar.set("{0:2d}".format(hours))
        minVar.set("{0:2d}".format(mins))
        secVar.set("{0:2d}".format(secs))

        # tentative de formatage des variables en text sans succes
        # time_string = f'{hourVar:2d}:{minVar:2d}:{hourVar:2d}'
        # label.config(text=time_string)
        #
        root.update()
        time.sleep(1)

        if (tmp == 0):
            initial_timer -= DECREMENT
            tmp = initial_timer
        tmp -= 1

        if (initial_timer == 0):
            tk.messagebox.showinfo("Timer: ", "Time's up")

    # while tmp_time > 0:
    #     timer = datetime.timedelta(seconds=tmp_time)


# main window
root = tk.Tk()
root.title('Sablier Maudit')
root.geometry("800x600")
root.after(100, countdown)
root.resizable(True, True)
root.attributes("-fullscreen", True)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

hourVar = tk.StringVar()
minVar = tk.StringVar()
secVar = tk.StringVar()

hourVar.set('00')
minVar.set('00')
secVar.set('20')

# tentative de conversion en string pour le label
# t = "%2d:%2d:2%d"(hourVar,minVar,secVar)

root.mainloop()
