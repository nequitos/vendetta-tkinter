from PIL import Image, ImageTk
import cv2 as cv
import imageio

import pydub
# import pyaudio

from itertools import count, cycle, repeat
import os.path

from threading import Thread

__all__ = [
    'TkMediaHandler'
]


class TkMediaHandler:
    def __init__(self, media_file, widget, toggle_button, size=None):
        self.media_file = media_file
        self.widget = widget
        self.toggle_button = toggle_button
        self.size = size

        self.playback_flag = True

        self.media_file_extension = self.split_file(media_file)[1].lower()
        self.image_extensions = ['.png', '.jpg', '.jpeg']
        self.video_extensions = ['.mp4', '.gif']

    def handle(self):
        if self.media_file_extension in self.image_extensions:
            self._load_image()
        if self.media_file_extension in self.video_extensions:
            if self.media_file_extension == '.gif':
                self._load_gif()
            else:
                self._load_video()

    def stop(self, event=None):
        self.widget.bind('<Button-1>', self.proceed)
        self.toggle_button.config(command=self.proceed)
        self.playback_flag = False

    def proceed(self, event=None):
        self.widget.bind('<Button-1>', self.stop)
        self.toggle_button.config(command=self.stop)
        self.playback_flag = True
        Thread(target=self._insert_media).start()

    def play(self, event=None):
        self.widget.bind('<Button-1>', self.stop)
        self.toggle_button.config(command=self.stop)
        Thread(target=self._insert_media).start()

    def _insert_media(self):
        if self.playback_flag:
            try:
                frame = next(self.loaded_media['frames'])

                if self.loaded_media['type'] == 'video':
                    image = ImageTk.PhotoImage(
                        Image.fromarray(frame).resize((self.size[0], self.size[1]), Image.ANTIALIAS))
                else:
                    image = frame

                self.widget.config(image=image)
                self.widget.image = image
                self.widget.after(self.loaded_media['delay'], self._insert_media)

            except StopIteration:
                self.widget.bind('<Button-1>', self.play)
                self.handle()

    def insert_start_frame(self):
        media_file = imageio.get_reader(self.media_file)
        frame = media_file.iter_data()

        start_frame = ImageTk.PhotoImage(
            Image.fromarray(next(frame)).resize((self.size[0], self.size[1]), Image.ANTIALIAS)
        )

        self.widget.config(image=start_frame)
        self.widget.image = start_frame

    def _load_gif(self):
        frames = []
        with Image.open(self.media_file) as gif:

            try:
                for frame in count(1):
                    new_frame = gif.copy()
                    new_frame.thumbnail((self.size[0], self.size[1]), Image.ANTIALIAS)
                    frames.append(ImageTk.PhotoImage(new_frame))
                    gif.seek(frame)
            except EOFError as exc:
                pass

            try:
                delay = gif.info['duration']
            except Exception as exc:
                delay = 100

        self.insert_start_frame()
        self.widget.bind('<Button-1>', self.play)
        self.toggle_button.config(command=self.play)
        self.loaded_media = {'type': 'gif', 'frames': cycle(frames), 'delay': delay}

    def _load_video(self):
        video = imageio.get_reader(self.media_file)
        frames = video.iter_data()
        delay = 20

        self.insert_start_frame()
        self.widget.bind('<Button-1>', self.play)
        self.toggle_button.config(command=self.play)
        self.loaded_media = {'type': 'video', 'frames': frames, 'delay': delay}

    def _load_image(self):
        with Image.open(self.media_file) as image:
            resized_image = image.resize((self.size[0], self.size[1]), Image.ANTIALIAS)

            self.insert_start_frame()
            self.loaded_media = {'type': 'image', 'image': resized_image}

    def _load_music(self):
        pass

    @staticmethod
    def get_size(file):
        try:
            media_file = Image.open(file)
            width, height = media_file.size[0], media_file.size[1]
        except Exception as exc:
            video = cv.VideoCapture(file)
            height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
            width = video.get(cv.CAP_PROP_FRAME_WIDTH)

        return width, height

    @staticmethod
    def get_file_name(file):
        return os.path.basename(file)

    @staticmethod
    def split_file(file):
        file_path_name, file_extension = os.path.splitext(file)
        return file_path_name, file_extension
