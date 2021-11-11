
from tkinter.filedialog import askopenfilename
from ttkbootstrap import Style, Colors
from tkinter import ttk
import tkinter as tk


class MainFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(MainFrame, self).__init__(root, **kwargs)

        # Main Canvas settings ------------
        self.root = root
        self.root.geometry('750x550')
        self.root.title('Vendetta Alpha')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
        self.root.bind('<Configure>', lambda _: self.layout_resize())
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

        # Styles settings ----------------
        style.configure('custom.Outline.TButton', padding=0, borderwidth=1, anchor='c')
        style.configure('custom.Vertical.TScrollbar')

        # Tabs Frame settings ------------
        self.tabs_frame = ttk.Frame(width=66, height=550)
        self.tabs_frame.grid(row=0, column=0)

        # Chats Frame settings -----------
        self.chats_frame = ttk.Frame(width=130, height=550)
        self.chats_frame.grid(row=0, column=1, columnspan=2, padx=5)

        # Dialogue Frame settings --------
        self.dialogue_frame = ttk.Frame(width=554, height=550)
        self.dialogue_frame.grid(row=0, column=3, columnspan=5)

        # Notebook Dialogue Frame settings
        self.notebook_dialogue_frame = ttk.Frame(self.dialogue_frame)
        self.notebook_dialogue_frame.pack(side='top', expand='false', fill='both', anchor='c')

        # Canvas Dialogue Frame settings
        self.canvas_dialogue_frame = ttk.Frame(self.dialogue_frame)
        self.canvas_dialogue_frame.pack(side='top', expand='false', fill='both', anchor='c')

        # Text Dialogue Frame settings ---
        self.text_dialogue_frame = ttk.Frame(self.dialogue_frame)
        self.text_dialogue_frame.pack(side='top', expand='false', fill='both', anchor='c')

        # Profile Button settings ---------
        self.btn_profile = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_profile_img)
        self.btn_profile.pack(side='top', expand='false', fill='both', anchor='c')

        # Settings Button settings --------
        self.btn_settings = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_settings_img)
        self.btn_settings.pack(side='bottom', expand='false', fill='both', anchor='c')

        # Music Button settings -----------
        self.btn_music = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_music_img)
        self.btn_music.pack(side='bottom', expand='false', fill='both', anchor='c', pady=5)

        # Main Button settings ------------
        self.btn_main = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_main_frame_img)
        self.btn_main.pack(side='bottom', expand='false', fill='both', anchor='c')

        # News Button settings ------------
        self.btn_news = ttk.Button(self.chats_frame, style='custom.Outline.TButton', image=btn_news_img)
        self.btn_news.pack(side='top', expand='false', fill='both', anchor='c')

        # Create Button settings ----------
        self.btn_create_state = True
        self.btn_create = ttk.Button(self.chats_frame, style='custom.Outline.TButton', image=btn_create_img,
                                     command=self.chat_create)
        self.btn_create.pack(side='top', expand='false', fill='both', anchor='c', pady=5)

        # Main chat Button settings -------
        self.btn_main_chat = ttk.Button(self.chats_frame, style='custom.Outline.TButton', image=btn_main_chat_img)
        self.btn_main_chat.pack(side='top', expand='false', fill='both', anchor='c')

        # Dialogue Notebook settings ------
        self.dialogue_notebook = ttk.Notebook(self.notebook_dialogue_frame)
        info_frame_notebook = ttk.Frame(self.dialogue_notebook)

        self.voice_button_notebook_state = True
        voice_button_notebook = ttk.Button(self.dialogue_notebook, text='Записать голосовое сообщение.',
                                           command=self.recording_voice_message)
        media_button_notebook = ttk.Button(self.dialogue_notebook, text='Выбрать медиафайл.',
                                           command=self.open_media_file)

        self.dialogue_notebook.add(info_frame_notebook, image=btn_info_img)
        self.dialogue_notebook.add(voice_button_notebook, image=btn_voice_img)
        self.dialogue_notebook.add(media_button_notebook, image=btn_media_img)

        self.dialogue_notebook.pack(side='top', expand='false', fill='both', anchor='c')

        # Dialogue Canvas settings --------
        self.dialogue_canvas = tk.Canvas(self.canvas_dialogue_frame)
        self.dialogue_canvas.pack(side='left', expand='false', fill='both', anchor='c')

        # Dialogue Text settings ----------
        self.dialogue_text = tk.Text(self.text_dialogue_frame, height=5)
        self.dialogue_text.pack(side='left', expand='false', fill='both', anchor='c')

        # Dialogue Canvas Scrollbar settings
        self.scrollbar_dialogue_canvas = ttk.Scrollbar(self.canvas_dialogue_frame, style='custom.Vertical.TScrollbar',
                                                       orient='vertical',
                                                       command=self.dialogue_canvas.yview)
        self.dialogue_canvas.configure(yscrollcommand=self.scrollbar_dialogue_canvas.set)
        self.scrollbar_dialogue_canvas.pack(side='right', expand='true', fill='y', anchor='c')

    def chat_create(self):
        # Button create Frame settings
        def close_chat_create_frame():
            self.btn_create_state = not self.btn_create_state
            btn_create_frame.destroy()

        if self.btn_create_state:
            self.btn_create_state = not self.btn_create_state
            btn_create_frame = tk.Toplevel()
            btn_create_frame.title('Create new chat')
            btn_create_frame.geometry('400x200')
            btn_create_frame.resizable(False, False)

            btn_create_frame.protocol("WM_DELETE_WINDOW", close_chat_create_frame)

    def recording_voice_message(self):
        # Voice Frame settings
        def close_voice_frame():
            self.voice_button_notebook_state = not self.voice_button_notebook_state
            voice_frame.destroy()

        def btn_play_state():
            pass

        if self.voice_button_notebook_state:
            self.voice_button_notebook_state = not self.voice_button_notebook_state
            voice_frame = tk.Toplevel()
            voice_frame.title('Voice message')
            voice_frame.geometry('500x60')
            voice_frame.resizable(False, False)

            btn_play_voice = ttk.Button(voice_frame, image=btn_play_img)
            btn_play_voice.grid(row=0, column=0, padx=5, pady=10)

            btn_replay_voice = ttk.Button(voice_frame, image=btn_replay_img)
            btn_replay_voice.grid(row=0, column=1, padx=5, pady=10)

            scale_voice = ttk.Scale(voice_frame, length=350, from_=0, to=100, value=0, orient='horizontal')
            scale_voice.grid(row=0, column=2, columnspan=3, padx=5, pady=10)

            voice_frame.protocol("WM_DELETE_WINDOW", close_voice_frame)

    def open_media_file(self):
        file = askopenfilename()
        print(file)

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.root.attributes("-fullscreen", self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.root.attributes("-fullscreen", self.full_screen_state)

    def layout_resize(self):
        main_frame_height = self.root.winfo_height()
        dialogue_frame_width = (self.root.winfo_width() - self.tabs_frame.winfo_width() -
                                self.chats_frame.winfo_width())

        self.tabs_frame.configure(height=main_frame_height)
        self.chats_frame.configure(height=main_frame_height)
        self.dialogue_frame.configure(width=dialogue_frame_width, height=main_frame_height)

        try:
            self.dialogue_canvas.configure(width=(dialogue_frame_width - 35),
                                           height=(main_frame_height - 43 - self.dialogue_notebook.winfo_height()))
        except Exception as ex:
            print("Виджет 'tkinter Canvas' несовеместим для использования с ttk.\n" + str(ex))

        try:
            self.dialogue_text.configure(width=dialogue_frame_width)
        except Exception as ex:
            print("Виджет 'tkinter Text' несовеместим для использования с ttk.\n" + str(ex))

        self.dialogue_notebook.configure(width=dialogue_frame_width)


class MusicFrame(ttk.Frame):
    pass


if __name__ == '__main__':
    style = Style(theme='superhero')

    master = style.master
    master.iconphoto(False, tk.PhotoImage(file='data/images/fsociety.gif'))

    btn_profile_img = tk.PhotoImage(file='data/images/rast/PNG Files/64x32/11.png')
    btn_main_frame_img = tk.PhotoImage(file='data/images/rast/PNG Files/64x32/7.png')
    btn_music_img = tk.PhotoImage(file='data/images/rast/PNG Files/64x32/104.png')
    btn_settings_img = tk.PhotoImage(file='data/images/rast/PNG Files/64x32/45.png')

    btn_news_img = tk.PhotoImage(file='data/images/rast/PNG Files/64x32/36.png')
    btn_create_img = tk.PhotoImage(file='data/images/rast/PNG Files/64x32/20.png')
    btn_main_chat_img = tk.PhotoImage(file='data/images/rast/PNG Files/64x32/9.png')

    btn_info_img = tk.PhotoImage(file='data/images/rast/PNG Files/32x16/22.png')

    btn_voice_img = tk.PhotoImage(file='data/images/rast/PNG Files/32x16/105.png')
    btn_play_img = tk.PhotoImage(file='data/images/rast/PNG Files/32x16/109.png')
    btn_replay_img = tk.PhotoImage(file='data/images/rast/PNG Files/32x16/21.png')

    btn_media_img = tk.PhotoImage(file='data/images/rast/PNG Files/32x16/29.png')

    MainFrame(master)

    master.mainloop()