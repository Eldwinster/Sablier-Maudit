#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk

# main window
root = tk.Tk()
root.title('Sablier Maudit')

# firstWindow = tk.Toplevel(root)

# Create a frame and configure its grid
paramFrame = ttk.Frame(root, padding='3 3 12 12')
paramFrame.grid(row=0, column=0)
# root.rowconfigure(3, weight=1)
# root.columnconfigure(4, weight=1)

# Layout of the root window
timelbl = ttk.Label(paramFrame, text='Temps de départ : ')
timelbl.grid(row=10, column=1)

hourVar = tk.StringVar()
hourEntry = ttk.Entry(paramFrame, textvariable=hourVar, width=3)
hourEntry.grid(row=10, column=10)

hourlbl = ttk.Label(paramFrame, text="h")
hourlbl.grid(row=10, column=11)

minVar = tk.StringVar()
minEntry = ttk.Entry(paramFrame, textvariable=minVar, width=3)
minEntry.grid(row=10, column=12)

minlbl = ttk.Label(paramFrame, text='min')
minlbl.grid(row=10, column=13)

secVar = tk.StringVar()
secEntry = ttk.Entry(paramFrame, textvariable=secVar, width=3)
secEntry.grid(row=10, column=14)

seclbl = ttk.Label(paramFrame, text='sec')
seclbl.grid(row=10, column=15)

incrementlbl = ttk.Label(paramFrame, text='Incrément/Décrément : ')
incrementlbl.grid(row=20, column=1)

incrementVar = tk.StringVar()
incrementEntry = ttk.Entry(paramFrame, textvariable=incrementVar, width=20)
incrementEntry.grid(row=20, column=10, columnspan=20)

incExampleLabel = ttk.Label(paramFrame, text="-1s, -1m, +1h, etc")
incExampleLabel.grid(row=20, column=32)

looplbl = ttk.Label(paramFrame, text='Nombre de tours : ')
looplbl.grid(row=30, column=1)

loopVar = tk.StringVar()
loopEntry = ttk.Entry(paramFrame, textvariable=loopVar, width=20)
loopEntry.grid(row=30, column=10, columnspan=20)

# button
closeButton = ttk.Button(paramFrame, text="Close", command=lambda: root.quit())
closeButton.grid(row=40, column=1)

applyButton = ttk.Button(paramFrame, text="Apply")
applyButton.grid(row=40, column=100)

root.mainloop()
