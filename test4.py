
from ttkbootstrap import Style, Colors
from tkinter import ttk
import tkinter as tk

from tkinter import *
from PIL import Image, ImageTk


# Tkinter image animation
# class ButtonImageAnimation(ttk.Button):
#     def __init__(self, widget, filename=None, **kw):
#         super().__init__(widget, **kw)
#         self.widget = widget
#         image = Image.open(filename)
#         cadres = []
#         try:
#             while True:
#                 cadres.append(image.copy())  # заполнение списка кадрами
#                 image.seek(len(cadres))  # skip to next frame
#         except EOFError as ex:
#             # print(ex)
#             pass  # we're done
#
#         try:
#             self.delay = image.info['duration']  # возврат задержки
#         except KeyError:
#             self.delay = 100
#
#         first = cadres[0].convert('RGBA')  # конвертирование в RGBA
#         self.frames = [ImageTk.PhotoImage(first)]
#
#         self.widget.config(image=self.frames[0])
#
#         temp = cadres[0]
#         for image in cadres[1:]: # доконвертирование картинок
#             temp.paste(image)
#             frame = temp.convert('RGBA')
#             self.frames.append(ImageTk.PhotoImage(frame))
#
#         self.index = 0
#         self.play()
#
#     def play(self):
#         self.widget.config(image=self.frames[self.index])  # проигрывание каждого фрейма
#         self.index += 1
#         if self.index == len(self.frames):
#             self.index = 0  # конец картинки
#         print(len(self.frames), self.index)
#         if self.index < (len(self.frames) - 1):
#             self.after(self.delay, self.play)


class ReturnAnimationWidget:
    def __init__(self, widget, filename):
        self.widget = widget
        image = Image.open(filename)
        cadres = []

        try:
            while True:
                cadres.append(image.copy())  # заполнение списка кадрами
                image.seek(len(cadres))  # skip to next frame
        except EOFError as ex:
            # print(ex)
            pass  # we're done

        try:
            self.delay = image.info['duration']  # возврат задержки
        except KeyError:
            self.delay = 100

        first = cadres[0].convert('RGBA')  # конвертирование в RGBA
        self.frames = [ImageTk.PhotoImage(first)]

        self.widget.configure(image=self.frames[0])

        temp = cadres[0]
        for image in cadres[1:]:  # доконвертирование картинок
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.index = 0
        self.play()

    def play(self):
        self.widget.config(image=self.frames[self.index])  # проигрывание каждого фрейма
        self.index += 1
        if self.index == len(self.frames):
            self.index = 0  # конец картинки
        print(len(self.frames), self.index)
        if self.index < (len(self.frames) - 1):
            self.widget.after(self.delay, self.play)

style = Style(theme='cosmo')
master = style.master
master.geometry('600x500')

style.configure('custom.TButton', background='red')

btn = ttk.Button()
btn.pack()
anim = ReturnAnimationWidget(btn, 'data/images/PNG/64x32/block-mic.gif')


master.mainloop()
