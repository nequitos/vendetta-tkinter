
from PIL import ImageTk, Image
from tkinter import ttk
import tkinter as tk

half_frame = []

# def gen_init(gen):
#     def initial(*args, **kwargs):
#         g = gen(*args, **kwargs)
#         next(g)
#         return g
#     return initial


class ReturnButtonAnimation(ttk.Button):
    def __init__(self, master, widget, filename):
        super(ReturnButtonAnimation, self).__init__(master)
        self.widget = widget
        self.filename = filename
        image = Image.open(self.filename)
        cadres = []

        try:
            while True:
                cadres.append(image.copy())  # заполнение списка кадрами
                image.seek(len(cadres))  # skip to next frame
        except EOFError as ex:
            # print(ex)
            pass  # we're done

        # try:
        #     self.delay = image.info['duration']  # возврат задержки
        # except KeyError:
        #     self.delay = 100

        self.delay = 15

        first = cadres[0].convert('RGBA')  # конвертирование в RGBA
        self.frames = [ImageTk.PhotoImage(first)]

        self.widget.configure(image=self.frames[0])

        temp = cadres[0]
        for image in cadres[1:]:  # доконвертирование картинок
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.index = 0
        self.cancel = None

    def play(self):
        self.widget.config(image=self.frames[self.index])  # проигрывание каждого фрейма
        if self.index != len(self.frames):
            self.index += 1

        self.cancel = self.widget.after(self.delay, self.play)

        if self.index == len(self.frames):
            self.widget.after_cancel(self.cancel)
            self.widget.config(image=self.frames[0])

    def play_half(self):
        self.widget.config(image=self.frames[self.index])
        if self.index != (len(self.frames) // 2):
            self.index += 1

        self.cancel = self.widget.after(self.delay, self.play_half)

        if self.index == (len(self.frames) // 2):
            self.widget.after_cancel(self.cancel)
            half_frame.append(self.index)

    def play_continue(self):
        self.widget.config(image=self.frames[half_frame[0]])
        if half_frame[0] != len(self.frames):
            half_frame[0] += 1

        self.cancel = self.widget.after(self.delay, self.play_continue)

        if half_frame[0] == len(self.frames):
            self.widget.after_cancel(self.cancel)
            self.widget.config(image=self.frames[0])
            half_frame.pop()


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('600x500')
    btn_img = tk.PhotoImage(file='data/images/GIF/play.gif')

    def play_btn(master):
        ReturnButtonAnimation(master=master, widget=btn, filename='data/images/GIF/play.gif').play()

    btn = ttk.Button(image=btn_img, command=lambda: play_btn(master=root))
    btn.pack(side='top')

    root.mainloop()
