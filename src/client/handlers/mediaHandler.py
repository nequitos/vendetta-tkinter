from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from PIL import Image, ImageTk
from tkvideo import tkvideo
from playsound import playsound
import cv2 as cv

from itertools import count, cycle

from pathlib import Path
import os


class MediaHandler:
    def __init__(self, widget, file):
        self._temp_path = str(Path(__file__).parent.parent) + '/temp/img'
        self.widget = widget
        self.file = file

        self.file_extension = self._split_file(file)[1]
        self.image_extensions = ['.png', '.jpg', '.jpeg']
        self.video_extensions = ['.mp4', '.gif']
        self.handle()

    def handle(self):
        if self.file_extension in self.image_extensions:
            image = self.image_load(self.file)
            self._insert_image(image)
        if self.file_extension in self.video_extensions:
            if self.file_extension == '.gif':
                gif = self.gif_load(self.file)
                self._insert_gif(*gif)
            else:
                video = self.video_load(self.file, self.widget)
                self._insert_video(video)

    def _insert_video(self, video):
        video.play()

    def _insert_gif(self, frames, length, delay=None):
        if length == 1:
            frame = list(frames)[0]
            self.widget.image = frame
            self.widget.config(image=frame)
        else:
            self.widget.config(image=next(frames))
            self.widget.after(delay, lambda: self._insert_gif(frames, length-1, delay))

    def _insert_image(self, file):
        self.widget.image = file
        self.widget.config(image=file)

    def image_load(self, file):
        image = Image.open(file)
        size = self.get_size(file)

        resized_image = image.resize((size[0], size[1]), Image.ANTIALIAS)

        return ImageTk.PhotoImage(resized_image)

    def video_load(self, file, widget):
        video = tkvideo(file, widget, loop=1)
        # playsound(file)
        size = self.get_size(file)
        video.size = size

        return video

    def gif_load(self, file):
        gif = Image.open(file)
        size = self.get_size(file)
        print(size)

        frames = []
        try:
            for frame in count(1):
                new_frame = gif.copy()
                new_frame.thumbnail((size[0], size[1]), Image.ANTIALIAS)
                frames.append(ImageTk.PhotoImage(new_frame))
                gif.seek(frame)
        except EOFError as exc:
            pass

        try:
            delay = gif.info['duration']
        except Exception as exc:
            delay = 100

        return (i for i in frames), len(frames), delay

    @staticmethod
    def get_size(file):
        try:
            media_file = Image.open(file)
            width, height = media_file.size[0], media_file.size[1]
        except Exception as exc:
            video = cv.VideoCapture(file)
            height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
            width = video.get(cv.CAP_PROP_FRAME_WIDTH)

        if width <= 1920 and height <= 1080:
            return int(float(width / 100 * 50)), int(float(height / 100 * 50))

    @staticmethod
    def _get_file_name(file):
        return os.path.basename(file)

    @staticmethod
    def _split_file(file):
        file_path_name, file_extension = os.path.splitext(file)
        return file_path_name, file_extension
