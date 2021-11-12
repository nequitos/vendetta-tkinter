
from tkinter.filedialog import askopenfilename
from ttkbootstrap import Style, Colors
from tkinter import ttk
import tkinter as tk


style = Style(theme='fiery-sunset', themes_file='data/themes/json/ttkbootstrap_themes.json')

master = style.master
master.geometry('600x500')

canvas = tk.Canvas()
canvas.pack(side='left', expand='true', fill='both', anchor='c')

scrollbar = ttk.Scrollbar(command=canvas.yview, orient='vertical')
canvas.configure(yscrollcammand=scrollbar.set)
scrollbar.pack(side='left', expand='true', fill='y', anchor='c')

master.mainloop()