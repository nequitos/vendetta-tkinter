
from tkinter.filedialog import askopenfilename
# from ttkbootstrap import Style, Colors
# from tkinter import ttk
# import tkinter as tk
#
#
# style = Style(theme='fiery-sunset', themes_file='data/themes/json/ttkbootstrap_themes.json')
#
# master = style.master
# master.geometry('600x500')
#
# canvas = tk.Canvas()
# canvas.pack(side='left', expand='true', fill='both', anchor='c')
#
# scrollbar = ttk.Scrollbar(command=canvas.yview, orient='vertical')
# canvas.configure(yscrollcammand=scrollbar.set)
# scrollbar.pack(side='left', expand='true', fill='y', anchor='c')
#
# master.mainloop()

# import tkinter as tk
# from PIL import Image, ImageTk
# from itertools import count
# import itertools
#
#
# class ImageLabel(tk.Label):
#     """a label that displays images, and plays them if they are gifs"""
#     def load(self, im):
#         if isinstance(im, str):
#             im = Image.open(im)
#         self.loc = 0
#         self.frames = []
#         self.check = 0
#
#         self.b = []
#
#         try:
#             for i in count(1):
#                 self.frames.append(ImageTk.PhotoImage(im.copy()))
#                 im.seek(i)
#         except EOFError:
#             pass
#
#         try:
#             self.delay = im.info['duration']
#         except:
#             self.delay = 100
#
#         if len(self.frames) == 1:
#             self.config(image=self.frames[0])
#         else:
#             self.next_frame()
#
#
#     def unload(self):
#         self.config(image="")
#         self.frames = None
#
#     def next_frame(self):
#         if self.frames:
#             self.loc += 1
#             self.loc %= len(self.frames)
#             print(self.loc)
#             self.config(image=self.frames[self.loc])
#             if self.loc < 26:
#                 self.after(self.delay, self.next_frame)
#                 self.check += 1
#             else:
#                 pass
#
#
#
# root = tk.Tk()
# root.config(bg='white')
# lbl = ImageLabel(root)
# lbl.pack()
# lbl.load('data/images/rast/64x32/block-mic.gif')
# root.mainloop()


from tkinter import *
from PIL import Image, ImageTk

check = 0


class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq = []
        try:
            while 1:
                seq.append(im.copy()) # заполнение списка кадрами
                im.seek(len(seq)) # skip to next frame
                print(seq)
        except EOFError:
            pass # we're done

        # try:
        #     self.delay = im.info['duration'] # возврат задержки
        # except KeyError:
        #     self.delay = 50

        self.delay = 30

        first = seq[0].convert('RGBA') # конвертирование в RGBA
        self.frames = [ImageTk.PhotoImage(first)]

        print(self.frames)

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]: # доконвертирование картинок
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0 # старт картинки

        #self.cancel = self.after(self.delay, self.play) # зацикливание проигрывания фремов из списка
        self.play()

    def play(self):
        global check
        self.config(image=self.frames[self.idx]) # проигрывание каждого фрейма
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0 # конец картинки
        print(len(self.frames), self.idx)
        if self.idx < (len(self.frames)-1):
            self.cancel = self.after(self.delay, self.play)


root = Tk()
anim = MyLabel(root, 'data/images/PNG/64x32/block-mic.gif')
anim.pack()

if check == 1:
    anim.after_cancel(anim.cancel)
def stop_it():
    anim.after_cancel(anim.cancel)

Button(root, text='stop', command=stop_it).pack()

root.mainloop()