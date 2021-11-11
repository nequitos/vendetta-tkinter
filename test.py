

import tkinter as tk


root = tk.Tk()
root.geometry('300x300')
test = tk.PhotoImage(file='data/images/fsociety.gif')

canvas = tk.Canvas(bg='red', scrollregion=(0, 0, 0, 1000), width=300, height=300)
canvas.pack(side='left', expand='true', fill='both', anchor='c')

scroll = tk.Scrollbar(orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=scroll.set)
scroll.pack(side='right', expand='false', fill='y', anchor='e')

canvas.create_text(150, 150, text='Well')

# btn = tk.Button(canvas, image=test)
# btn.pack(side='top')

# def get_buttons(widget):
#     for i in range(30):
#         tk.Button(widget, text=str(i)).pack(side='top')
#
# get_buttons(canvas)


root.mainloop()