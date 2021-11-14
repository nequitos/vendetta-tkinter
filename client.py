
from tkinter.filedialog import askopenfilename
from ttkbootstrap import Style, Colors
from tkinter import ttk
import tkinter as tk

from PIL import ImageTk, Image


tabs_frame_settings = []
tabs_frame_slaves = []


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
        self.cancel = self.widget.after(self.delay, self.play)

    def play(self):
        self.widget.config(image=self.frames[self.index])  # проигрывание каждого фрейма
        if self.index != len(self.frames):
            self.index += 1

        self.cancel = self.widget.after(self.delay, self.play)

        if self.index == len(self.frames):
            self.widget.after_cancel(self.cancel)
            self.widget.config(image=self.frames[0])


class ChoseFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(ChoseFrame, self).__init__(root, **kwargs)

        # Main Frame settings ------------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta Alpha')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
        self.root.bind('<Configure>', lambda _: self.layout_resize())
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

        # Styles settings ----------------------------------------------------------------------------------------------
        style.configure('custom.Outline.TButton', padding=0, borderwidth=0, anchor='c')

        # Tabs Frame settings ------------------------------------------------------------------------------------------
        self.tabs_frame = ttk.Frame(width=66, height=550)
        self.tabs_frame.grid(row=0, column=0)

        # Profile Button settings --------------------------------------------------------------------------------------
        self.btn_news = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_news_img,
                                      command=self.news)
        self.btn_news.pack(side='top', expand='false', fill='both', anchor='c')

        # Main Button settings -----------------------------------------------------------------------------------------
        self.btn_main = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_main_frame_img,
                                   command=self.main)
        self.btn_main.pack(side='top', expand='false', fill='both', anchor='c', pady=5)

        # Music Button settings ----------------------------------------------------------------------------------------
        self.btn_music = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_music_img,
                                    command=self.music)
        self.btn_music.pack(side='top', expand='false', fill='both', anchor='c')

        # Settings Button settings -------------------------------------------------------------------------------------
        self.btn_settings = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_settings_img,
                                       command=self.settings)
        self.btn_settings.pack(side='bottom', expand='false', fill='both', anchor='c')

        if len(tabs_frame_settings) <= 0:
            [tabs_frame_settings.append(i) for i in self.root.grid_slaves()]

        if len(tabs_frame_slaves) <= 0:
            [tabs_frame_slaves.append(i) for i in self.tabs_frame.pack_slaves()]

        self.main()

    def news(self):
        [i.configure(state='normal') for i in self.tabs_frame.pack_slaves() if str(i['state']) == 'disabled']
        [i.destroy() for i in self.root.grid_slaves() if str(i) != '.!frame']

        ReturnButtonAnimation(self.tabs_frame, self.btn_news, 'data/images/GIF/news.gif')
        self.btn_news.configure(state='disabled')
        NewsFrame(self.root)

    def main(self):
        [i.configure(state='normal') for i in self.tabs_frame.pack_slaves() if str(i['state']) == 'disabled']
        [i.destroy() for i in self.root.grid_slaves() if str(i) != '.!frame']

        ReturnButtonAnimation(self.tabs_frame, self.btn_main, 'data/images/GIF/main.gif')
        self.btn_main.configure(state='disabled')
        MainFrame(self.root)

    def music(self):
        [i.configure(state='normal') for i in self.tabs_frame.pack_slaves() if str(i['state']) == 'disabled']
        [i.destroy() for i in self.root.grid_slaves() if str(i) != '.!frame']

        ReturnButtonAnimation(self.tabs_frame, self.btn_music, 'data/images/GIF/music.gif')
        self.btn_music.configure(state='disabled')
        MusicFrame(self.root)

    def settings(self):
        [i.configure(state='normal') for i in self.tabs_frame.pack_slaves() if str(i['state']) == 'disabled']
        [i.destroy() for i in self.root.grid_slaves() if str(i) != '.!frame']

        ReturnButtonAnimation(self.tabs_frame, self.btn_settings, 'data/images/GIF/settings.gif')
        self.btn_settings.configure(state='disabled')
        SettingsFrame(self.root)

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.root.attributes("-fullscreen", self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.root.attributes("-fullscreen", self.full_screen_state)

    def layout_resize(self):
        main_frame_height = self.root.winfo_height()

        self.tabs_frame.configure(height=main_frame_height)


class NewsFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(NewsFrame, self).__init__(root, **kwargs)

        # Profile Frame settings --------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta News')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
        self.root.bind('<Configure>', lambda _: self.layout_resize())
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

        # Style settings -----------------------------------------------------------------------------------------------
        style.configure('custom.TFrame', background='black')

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.root.attributes("-fullscreen", self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.root.attributes("-fullscreen", self.full_screen_state)

    def layout_resize(self):
        main_frame_height = self.root.winfo_height()

        tabs_frame_settings[0].configure(height=main_frame_height)


class MainFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(MainFrame, self).__init__(root, **kwargs)

        # Main Frame settings ------------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta Alpha')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
        self.root.bind('<Configure>', lambda _: self.layout_resize())
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

        # Styles settings ----------------------------------------------------------------------------------------------
        style.configure('custom.Outline.TButton', padding=0, borderwidth=0, anchor='c')
        style.configure('custom_notebook.TButton', borderwidth=0, anchor='c')
        style.configure('custom.Vertical.TScrollbar')

        # Chats Frame settings -----------------------------------------------------------------------------------------
        self.chats_frame = ttk.Frame(width=130, height=550)
        self.chats_frame.grid(row=0, column=1, columnspan=2, padx=5)

        # Dialogue Frame settings --------------------------------------------------------------------------------------
        self.dialogue_frame = ttk.Frame(width=554, height=550)
        self.dialogue_frame.grid(row=0, column=3, columnspan=5)

        # Notebook Dialogue Frame settings -----------------------------------------------------------------------------
        self.notebook_dialogue_frame = ttk.Frame(self.dialogue_frame)
        self.notebook_dialogue_frame.pack(side='top', expand='false', fill='both', anchor='c')

        # Canvas Dialogue Frame settings -------------------------------------------------------------------------------
        self.canvas_dialogue_frame = ttk.Frame(self.dialogue_frame)
        self.canvas_dialogue_frame.pack(side='top', expand='false', fill='both', anchor='c')

        # Text Dialogue Frame settings ---------------------------------------------------------------------------------
        self.text_dialogue_frame = ttk.Frame(self.dialogue_frame)
        self.text_dialogue_frame.pack(side='top', expand='false', fill='both', anchor='c')

        # Create Button settings ---------------------------------------------------------------------------------------
        self.btn_create = ttk.Button(self.chats_frame, style='custom.Outline.TButton', image=btn_create_img,
                                     command=self.chat_create)
        self.btn_create.pack(side='top', expand='false', fill='both', anchor='c')

        # Main chat Button settings ------------------------------------------------------------------------------------
        self.btn_main_chat = ttk.Button(self.chats_frame, style='custom.Outline.TButton',
                                        image=btn_main_chat_img)
        self.btn_main_chat.pack(side='top', expand='false', fill='both', anchor='c', pady=5)

        # Dialogue Notebook settings -----------------------------------------------------------------------------------
        self.dialogue_notebook = ttk.Notebook(self.notebook_dialogue_frame)
        info_frame_notebook = ttk.Frame(self.dialogue_notebook)

        self.voice_button_notebook = ttk.Button(self.dialogue_notebook,
                                                style='custom_notebook.TButton',
                                                text='Записать голосовое сообщение.',
                                                command=self.recording_voice_message)
        self.media_button_notebook = ttk.Button(self.dialogue_notebook,
                                                style='custom_notebook.TButton',
                                                text='Выбрать медиафайл.',
                                                command=self.open_media_file)

        self.dialogue_notebook.add(info_frame_notebook, image=btn_info_img)
        self.dialogue_notebook.add(self.voice_button_notebook, image=btn_voice_img)
        self.dialogue_notebook.add(self.media_button_notebook, image=btn_media_img)

        self.dialogue_notebook.pack(side='top', expand='false', fill='both', anchor='c')

        # Dialogue Canvas settings -------------------------------------------------------------------------------------
        self.dialogue_canvas = tk.Canvas(self.canvas_dialogue_frame)
        self.dialogue_canvas.pack(side='left', expand='false', fill='both', anchor='c')

        # Dialogue Text settings ---------------------------------------------------------------------------------------
        self.dialogue_text = tk.Text(self.text_dialogue_frame, bg='#5C5C5C', fg='white', insertbackground='white',
                                     height=5)
        self.dialogue_text.pack(side='left', expand='false', fill='both', anchor='c')

        # Dialogue Canvas Scrollbar settings ---------------------------------------------------------------------------
        self.scrollbar_dialogue_canvas = ttk.Scrollbar(self.canvas_dialogue_frame, style='custom.Vertical.TScrollbar',
                                                       orient='vertical',
                                                       command=self.dialogue_canvas.yview)
        self.dialogue_canvas.configure(yscrollcommand=self.scrollbar_dialogue_canvas.set)
        self.scrollbar_dialogue_canvas.pack(side='right', expand='true', fill='y', anchor='c')

    def chat_create(self):
        # Button create Frame settings ---------------------------------------------------------------------------------
        def close_chat_create_frame():
            self.btn_create.configure(state='active')
            btn_create_frame.destroy()

        self.btn_create.configure(state='disabled')
        btn_create_frame = tk.Toplevel()
        btn_create_frame.title('Create new chat')
        btn_create_frame.geometry('400x200')
        btn_create_frame.resizable(False, False)

        btn_create_frame.protocol("WM_DELETE_WINDOW", close_chat_create_frame)

    def recording_voice_message(self):
        # Voice Frame settings -----------------------------------------------------------------------------------------
        def close_voice_frame():
            self.voice_button_notebook.configure(state='active')
            voice_frame.destroy()

        self.voice_button_notebook.configure(state='disabled')
        voice_frame = tk.Toplevel()
        voice_frame.title('Voice message')
        voice_frame.geometry('500x60')
        voice_frame.resizable(False, False)

        btn_play_voice = ttk.Button(voice_frame, style='custom.secondary.Outline.TButton', image=btn_play_img)
        btn_play_voice.grid(row=0, column=0, padx=5, pady=15)

        btn_replay_voice = ttk.Button(voice_frame, style='custom.secondary.Outline.TButton', image=btn_replay_img)
        btn_replay_voice.grid(row=0, column=1, padx=5, pady=15)

        scale_voice = ttk.Scale(voice_frame, length=350, from_=0, to=100, value=0, orient='horizontal')
        scale_voice.grid(row=0, column=2, columnspan=3, padx=10, pady=10)

        voice_frame.protocol("WM_DELETE_WINDOW", close_voice_frame)

    def open_media_file(self):
        file = askopenfilename()
        print(file)

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.root.attributes("-fullscreen", self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.root.attributes("-fullscreen", self.full_screen_state)

    def layout_resize(self):
        main_frame_height = self.root.winfo_height()
        dialogue_frame_width = (self.root.winfo_width() - tabs_frame_settings[0].winfo_width() -
                                self.chats_frame.winfo_width())

        tabs_frame_settings[0].configure(height=main_frame_height)
        self.chats_frame.configure(height=main_frame_height)
        self.dialogue_frame.configure(width=dialogue_frame_width, height=main_frame_height)

        try:
            self.dialogue_canvas.configure(width=(dialogue_frame_width - 35),
                                           height=(main_frame_height - 43 - self.dialogue_notebook.winfo_height()))
        except Exception as ex:
            #print("Виджет 'tkinter Canvas' несовеместим для использования с ttk.\n" + str(ex))
            pass

        try:
            self.dialogue_text.configure(width=dialogue_frame_width)
        except Exception as ex:
            #print("Виджет 'tkinter Text' несовеместим для использования с ttk.\n" + str(ex))
            pass

        self.dialogue_notebook.configure(width=dialogue_frame_width)


class MusicFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(MusicFrame, self).__init__(root, **kwargs)

        # Music Frame settings -----------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta Music')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
        self.root.bind('<Configure>', lambda _: self.layout_resize())
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

        # Style settings -----------------------------------------------------------------------------------------------
        style.configure('custom.TFrame', background='black')

        # Notebook Frame settings --------------------------------------------------------------------------------------
        self.music_notebook_frame = ttk.Frame(style='custom.TFrame')
        self.music_notebook_frame.grid(row=0, column=1, columnspan=2, padx=5)

        # Music Notebook settings --------------------------------------------------------------------------------------
        self.music_notebook = ttk.Notebook(self.music_notebook_frame)

        self.search_frame_notebook = ttk.Frame(self.music_notebook)
        self.saves_frame_notebook = ttk.Frame(self.music_notebook)
        self.playlists_notebook = ttk.Frame(self.music_notebook)

        self.music_notebook.add(self.search_frame_notebook, text='Поиск')
        self.music_notebook.add(self.saves_frame_notebook, text='Сохранненые')
        self.music_notebook.add(self.playlists_notebook, text='Плейлисты')

        self.music_notebook.pack(side='top', expand='false', fill='both', anchor='c')

        # Search Entry settings ----------------------------------------------------------------------------------------
        self.search_entry_search = ttk.Entry(self.search_frame_notebook)
        self.search_entry_search.pack(side='top', expand='false', fill='both', anchor='c', pady=5)

        # Saves Entry settings -----------------------------------------------------------------------------------------
        self.search_entry_saves = ttk.Entry(self.saves_frame_notebook)
        self.search_entry_saves.pack(side='top', expand='false', fill='both', anchor='c', pady=5)

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.root.attributes("-fullscreen", self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.root.attributes("-fullscreen", self.full_screen_state)

    def layout_resize(self):
        main_frame_width = self.root.winfo_width()
        main_frame_height = self.root.winfo_height()
        tabs_frame_width = tabs_frame_settings[0].winfo_width()

        tabs_frame_settings[0].configure(height=main_frame_height)
        self.music_notebook.configure(width=(main_frame_width - tabs_frame_width), height=(main_frame_height - 31))


class SettingsFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(SettingsFrame, self).__init__(root, **kwargs)

        # Settings Frame settings --------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta Settings')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
        self.root.bind('<Configure>', lambda _: self.layout_resize())
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

        # Style settings -----------------------------------------------------------------------------------------------
        style.configure('custom.TFrame', background='black')

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.root.attributes("-fullscreen", self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.root.attributes("-fullscreen", self.full_screen_state)

    def layout_resize(self):
        main_frame_height = self.root.winfo_height()

        tabs_frame_settings[0].configure(height=main_frame_height)


if __name__ == '__main__':
    theme = 'fiery-sunset'
    style = Style(theme='fiery-sunset', themes_file='data/themes/json/ttkbootstrap_themes.json')

    master = style.master
    master.geometry('750x550')

    master.configure(bg='#B66254')
    master.iconphoto(False, tk.PhotoImage(file='data/images/fsociety.gif'))

    btn_news_img = tk.PhotoImage(file='data/images/GIF/news.gif')
    btn_main_frame_img = tk.PhotoImage(file='data/images/GIF/main.gif')
    btn_music_img = tk.PhotoImage(file='data/images/GIF/music.gif')
    btn_settings_img = tk.PhotoImage(file='data/images/GIF/settings.gif')

    btn_create_img = tk.PhotoImage(file='data/images/PNG Files/64x32/' + theme + '/20.png')
    btn_main_chat_img = tk.PhotoImage(file='data/images/PNG Files/64x32/' + theme + '/9.png')

    btn_info_img = tk.PhotoImage(file='data/images/PNG Files/32x16/' + theme + '/22.png')

    btn_voice_img = tk.PhotoImage(file='data/images/PNG Files/32x16/' + theme + '/105.png')
    btn_play_img = tk.PhotoImage(file='data/images/PNG Files/32x16/' + theme + '/109.png')
    btn_replay_img = tk.PhotoImage(file='data/images/PNG Files/32x16/' + theme + '/21.png')

    btn_media_img = tk.PhotoImage(file='data/images/PNG Files/32x16/' + theme + '/29.png')

    ChoseFrame(master)

    master.mainloop()