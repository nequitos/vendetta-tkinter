from tkinter.filedialog import askopenfilename
from ttkbootstrap import Style, Colors
from tkinter import ttk
import tkinter as tk

from api import *

import client

tabs_frame_settings = []
tabs_frame_slaves = []


class ChoseFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(ChoseFrame, self).__init__(root, **kwargs)

        # Main Frame settings ------------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta Alpha')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

        # Styles settings ----------------------------------------------------------------------------------------------
        style.configure('custom.Outline.TButton', padding=0, borderwidth=0, anchor='c')

        # Tabs Frame settings ------------------------------------------------------------------------------------------
        self.tabs_frame = ttk.Frame(width=64, height=550)
        self.tabs_frame.pack(side='left', expand='false', fill='both', anchor='c')

        # Profile Button settings --------------------------------------------------------------------------------------
        self.btn_news = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_news_img,
                                   state='disabled')
        self.btn_news.pack(side='top', expand='false', fill='both', anchor='c')

        # Main Button settings -----------------------------------------------------------------------------------------
        self.btn_main = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_main_frame_img,
                                   command=self.main)
        self.btn_main.pack(side='top', expand='false', fill='both', anchor='c', pady=5)

        # Music Button settings ----------------------------------------------------------------------------------------
        self.btn_music = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_music_img,
                                    state='disabled')
        self.btn_music.pack(side='top', expand='false', fill='both', anchor='c')

        # Settings Button settings -------------------------------------------------------------------------------------
        self.btn_settings = ttk.Button(self.tabs_frame, style='custom.Outline.TButton', image=btn_settings_img,
                                       state='disabled')
        self.btn_settings.pack(side='bottom', expand='false', fill='both', anchor='c')

        if len(tabs_frame_settings) <= 0:
            [tabs_frame_settings.append(i) for i in self.root.grid_slaves()]

        if len(tabs_frame_slaves) <= 0:
            [tabs_frame_slaves.append(i) for i in self.tabs_frame.pack_slaves()]

        self.main()

    def news(self):
        [i.configure(state='normal') for i in self.tabs_frame.pack_slaves() if str(i['state']) == 'disabled']
        [i.destroy() for i in self.root.pack_slaves() if str(i) != '.!frame']

        ReturnButtonAnimation(self.tabs_frame, self.btn_news, 'data/images/GIF/news.gif').play()
        self.btn_news.configure(state='disabled')
        NewsFrame(self.root)

    def main(self):
        # [i.configure(state='normal') for i in self.tabs_frame.pack_slaves() if str(i['state']) == 'disabled']
        [i.destroy() for i in self.root.pack_slaves() if str(i) != '.!frame']

        ReturnButtonAnimation(self.tabs_frame, self.btn_main, 'data/images/GIF/main.gif').play()
        self.btn_main.configure(state='disabled')
        MainFrame(self.root)

    def music(self):
        [i.configure(state='normal') for i in self.tabs_frame.pack_slaves() if str(i['state']) == 'disabled']
        [i.destroy() for i in self.root.pack_slaves() if str(i) != '.!frame']

        ReturnButtonAnimation(self.tabs_frame, self.btn_music, 'data/images/GIF/music.gif').play()
        self.btn_music.configure(state='disabled')
        MusicFrame(self.root)

    def settings(self):
        [i.configure(state='normal') for i in self.tabs_frame.pack_slaves() if str(i['state']) == 'disabled']
        [i.destroy() for i in self.root.pack_slaves() if str(i) != '.!frame']

        ReturnButtonAnimation(self.tabs_frame, self.btn_settings, 'data/images/GIF/settings.gif').play()
        self.btn_settings.configure(state='disabled')
        SettingsFrame(self.root)

    def toggle_full_screen(self, event):
        self.full_screen_state = not self.full_screen_state
        self.root.attributes("-fullscreen", self.full_screen_state)

    def end_full_screen(self, event):
        self.full_screen_state = False
        self.root.attributes("-fullscreen", self.full_screen_state)


class NewsFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(NewsFrame, self).__init__(root, **kwargs)

        # Profile Frame settings --------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta News')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
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


class MainFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(MainFrame, self).__init__(root, **kwargs)

        # Main Frame settings ------------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta Alpha')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

        # Styles settings ----------------------------------------------------------------------------------------------
        style.configure('custom.Outline.TButton', padding=0, borderwidth=0, anchor='c')
        style.configure('custom_notebook.TButton', borderwidth=0, anchor='c')
        style.configure('custom.Vertical.TScrollbar')

        # Chats Frame settings -----------------------------------------------------------------------------------------
        self.chats_frame = ttk.Frame(width=128, height=550)
        self.chats_frame.pack(side='left', expand='false', fill='both', anchor='c', padx=5)

        # Dialogue Frame settings --------------------------------------------------------------------------------------
        self.dialogue_frame = ttk.Frame(width=554, height=550)
        self.dialogue_frame.pack(side='left', expand='true', fill='both', anchor='c')

        # Notebook Dialogue Frame settings -----------------------------------------------------------------------------
        self.notebook_dialogue_frame = ttk.Frame(self.dialogue_frame)
        self.notebook_dialogue_frame.pack(side='top', expand='false', fill='both', anchor='c')

        # Canvas Dialogue Frame settings -------------------------------------------------------------------------------
        self.canvas_dialogue_frame = ttk.Frame(self.dialogue_frame)
        self.canvas_dialogue_frame.pack(side='top', expand='true', fill='both', anchor='c')

        # Text Dialogue Frame settings ---------------------------------------------------------------------------------
        self.text_dialogue_frame = ttk.Frame(self.dialogue_frame)
        self.text_dialogue_frame.pack(side='top', expand='false', fill='both', anchor='c')

        # Create Button settings ---------------------------------------------------------------------------------------
        self.btn_create = ttk.Button(self.chats_frame, style='custom.Outline.TButton', image=btn_create_img,
                                     command=self.chat_create, state='disabled')
        self.btn_create.pack(side='top', expand='false', fill='both', anchor='c')

        # Main chat Button settings ------------------------------------------------------------------------------------
        self.btn_main_chat = ttk.Button(self.chats_frame, style='custom.Outline.TButton', image=btn_main_chat_img,
                                        command=self.main_chat, state='disabled')
        self.btn_main_chat.pack(side='top', expand='false', fill='both', anchor='c', pady=5)

        # Dialogue Notebook settings -----------------------------------------------------------------------------------
        self.dialogue_notebook = ttk.Notebook(self.notebook_dialogue_frame, height=31)
        self.info_frame_notebook = ttk.Button(self.dialogue_notebook,
                                              style='custom_notebook.TButton',
                                              text='Посмотреть закрепленное сообщение.',
                                              command=self.info, state='disabled')

        self.voice_button_notebook = ttk.Button(self.dialogue_notebook,
                                                style='custom_notebook.TButton',
                                                text='Записать голосовое сообщение.',
                                                command=self.recording_voice_message, state='disabled')
        self.media_button_notebook = ttk.Button(self.dialogue_notebook,
                                                style='custom_notebook.TButton',
                                                text='Выбрать медиафайл.',
                                                command=self.open_media_file, state='disabled')

        self.dialogue_notebook.add(self.info_frame_notebook, image=btn_info_img)
        self.dialogue_notebook.add(self.voice_button_notebook, image=btn_voice_img)
        self.dialogue_notebook.add(self.media_button_notebook, image=btn_media_img)

        self.dialogue_notebook.pack(side='top', expand='false', fill='both', anchor='c')

        # Dialogue Canvas settings -------------------------------------------------------------------------------------
        self.dialogue_canvas = tk.Canvas(self.canvas_dialogue_frame)
        self.dialogue_canvas.pack(side='left', expand='true', fill='both', anchor='c')

        # Dialogue Text settings ---------------------------------------------------------------------------------------
        self.dialogue_text = tk.Text(self.text_dialogue_frame, height=3, bg='#5C5C5C', fg='white',
                                     insertbackground='white')
        self.dialogue_text.pack(side='top', expand='false', fill='both', anchor='c')

        # Dialogue Canvas Scrollbar settings ---------------------------------------------------------------------------
        self.scrollbar_dialogue_canvas = ttk.Scrollbar(self.canvas_dialogue_frame, style='custom.Vertical.TScrollbar',
                                                       orient='vertical',
                                                       command=self.dialogue_canvas.yview)
        self.dialogue_canvas.configure(yscrollcommand=self.scrollbar_dialogue_canvas.set)
        self.scrollbar_dialogue_canvas.pack(side='right', expand='false', fill='y', anchor='c')

    def chat_create(self):
        # Button create Frame settings ---------------------------------------------------------------------------------
        ReturnButtonAnimation(self.chats_frame, self.btn_create, 'data/images/GIF/create.gif').play()

        def close_chat_create_frame():
            self.btn_create.configure(state='active')
            btn_create_frame.destroy()

        self.btn_create.configure(state='disabled')
        btn_create_frame = tk.Toplevel()
        btn_create_frame.title('Create new chat')
        btn_create_frame.geometry('400x200')
        btn_create_frame.resizable(False, False)

        btn_create_frame.protocol("WM_DELETE_WINDOW", close_chat_create_frame)

    def main_chat(self):
        ReturnButtonAnimation(self.chats_frame, self.btn_main_chat, 'data/images/GIF/main_chat.gif').play()

    def info(self):
        pass

    def recording_voice_message(self):
        # Voice Frame settings -----------------------------------------------------------------------------------------
        def close_voice_frame():
            self.voice_button_notebook.configure(state='active')
            voice_frame.destroy()

        def play_half(master, button):
            ReturnButtonAnimation(master, button, 'data/images/GIF/play.gif').play_half()
            button.configure(command=lambda: play_continue(master, button))

        def play_continue(master, button):
            ReturnButtonAnimation(master, button, 'data/images/GIF/play.gif').play_continue()
            button.configure(command=lambda: play_half(master, button))

        def replay(master, button):
            ReturnButtonAnimation(master, button, 'data/images/GIF/replay.gif').play()

        self.voice_button_notebook.configure(state='disabled')
        voice_frame = tk.Toplevel()
        voice_frame.title('Voice message')
        voice_frame.geometry('560x68')
        voice_frame.resizable(False, False)

        btn_play_voice = ttk.Button(voice_frame, style='custom.secondary.Outline.TButton', image=btn_play_img,
                                    command=lambda: play_half(voice_frame, btn_play_voice))
        btn_play_voice.grid(row=0, column=0, padx=5, pady=5)

        btn_replay_voice = ttk.Button(voice_frame, style='custom.secondary.Outline.TButton', image=btn_replay_img,
                                      command=lambda: replay(voice_frame, btn_replay_voice))
        btn_replay_voice.grid(row=0, column=1, padx=5, pady=5)

        scale_voice = ttk.Scale(voice_frame, length=350, from_=0, to=100, value=0, orient='horizontal')
        scale_voice.grid(row=0, column=2, columnspan=3, padx=10, pady=5)

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


class MusicFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(MusicFrame, self).__init__(root, **kwargs)

        # Music Frame settings -----------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta Music')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
        self.root.bind("<F11>", self.toggle_full_screen)
        self.root.bind("<Escape>", self.end_full_screen)

        # Style settings -----------------------------------------------------------------------------------------------
        style.configure('custom.TFrame', background='black')

        # Notebook Frame settings --------------------------------------------------------------------------------------
        self.music_notebook_frame = ttk.Frame(style='custom.TFrame')
        self.music_notebook_frame.pack(side='left', expand='true', fill='both', anchor='c')

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


class SettingsFrame(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(SettingsFrame, self).__init__(root, **kwargs)

        # Settings Frame settings --------------------------------------------------------------------------------------
        self.root = root
        self.root.title('Vendetta Settings')
        self.root.minsize(width=697, height=450)
        self.full_screen_state = False
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


if __name__ == '__main__':
    style = Style(theme='fiery-sunset', themes_file='data/themes/json/ttkbootstrap_themes.json')
    # print([(i, style.colors.get(i)) for i in style.colors])

    master = style.master
    master.geometry('750x550')

    master.configure(bg='#5C5C5C')
    master.iconphoto(False, tk.PhotoImage(file='data/images/fsociety.gif'))

    btn_news_img = tk.PhotoImage(file='data/images/GIF/news.gif')
    btn_main_frame_img = tk.PhotoImage(file='data/images/GIF/main.gif')
    btn_music_img = tk.PhotoImage(file='data/images/GIF/music.gif')
    btn_settings_img = tk.PhotoImage(file='data/images/GIF/settings.gif')

    btn_create_img = tk.PhotoImage(file='data/images/GIF/create.gif')
    btn_main_chat_img = tk.PhotoImage(file='data/images/GIF/main_chat.gif')

    btn_info_img = tk.PhotoImage(file='data/images/PNG/32x16/info.png')

    btn_voice_img = tk.PhotoImage(file='data/images/PNG/32x16/voice.png')
    btn_play_img = tk.PhotoImage(file='data/images/GIF/play.gif')
    btn_replay_img = tk.PhotoImage(file='data/images/GIF/replay.gif')

    btn_media_img = tk.PhotoImage(file='data/images/PNG/32x16/media.png')

    ChoseFrame(master)

    master.mainloop()
