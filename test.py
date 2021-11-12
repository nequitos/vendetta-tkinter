

# import tkinter as tk
#
#
# root = tk.Tk()
# root.geometry('300x300')
# test = tk.PhotoImage(file='data/images/fsociety.gif')
#
# canvas = tk.Canvas(bg='red', scrollregion=(0, 0, 0, 1000), width=300, height=300)
# canvas.pack(side='left', expand='true', fill='both', anchor='c')
#
# scroll = tk.Scrollbar(orient='vertical', command=canvas.yview)
# canvas.configure(yscrollcommand=scroll.set)
# scroll.pack(side='right', expand='false', fill='y', anchor='e')
#
# canvas.create_text(150, 150, text='Well')

# btn = tk.Button(canvas, image=test)
# btn.pack(side='top')

# def get_buttons(widget):
#     for i in range(30):
#         tk.Button(widget, text=str(i)).pack(side='top')
#
# get_buttons(canvas)


# root.mainloop()


import tkinter as tk
from tkinter import messagebox

# root = tk.Tk()
#
# def on_closing():
#     if messagebox.askokcancel("Quit", "Do you want to quit?"):
#         root.destroy()
#
# root.protocol("WM_DELETE_WINDOW", on_closing)
# root.mainloop()


root = tk.Tk()
root.geometry('600x500')


l1 = tk.Label(bg='red')
l1.pack(side='left', expand='true', fill='both', anchor='w')

l2 = tk.Label(bg='blue')
l2.pack(side='left', expand='true', fill='both', anchor='w')

l3 = tk.Label(bg='yellow')
l3.pack(side='left', expand='true', fill='both', anchor='w')
print(root.winfo_viewable())

root.mainloop()

