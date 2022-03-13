from PIL import Image, ImageTk
import cv2 as cv
import imageio

from itertools import count

from threading import Thread
from pathlib import Path
import os


class MediaHandler:
    def __init__(self, widget, file):
        self.widget = widget
        self.file = file

        self.cancel = None
        self.ready_to_play = None
        self.stop_thread_flag = False

        self.file_extension = self._split_file(file)[1]
        self.image_extensions = ['.png', '.jpg', '.jpeg']
        self.video_extensions = ['.mp4', '.mkv', '.gif']

        self.handle()

    def handle(self):
        if self.file_extension in self.image_extensions:
            self._insert_image()
        if self.file_extension in self.video_extensions:
            if self.file_extension == '.gif':
                self.ready_to_play = self._insert_gif
            else:
                self.ready_to_play = self._insert_video

    def play(self):
        thread = Thread(target=self.ready_to_play)
        thread.start()

    def toggle(self, event):
        self.stop_thread_flag = not self.stop_thread_flag
        print(self.stop_thread_flag)

    def stop(self):
        self.stop_thread_flag = True

    def proceed(self):
        self.stop_thread_flag = False

    def _insert_video(self):
        video = imageio.get_reader(self.file)
        size = self.get_size(self.file)
        frames = video.iter_data()

        while True:
            if not self.stop_thread_flag:
                frame = next(frames)
                image = ImageTk.PhotoImage(Image.fromarray(frame).resize((size[0], size[1])))
                self.widget.config(image=image)
                self.widget.image = image

    def _insert_gif(self):
        gif = Image.open(self.file)
        size = self.get_size(self.file)

        try:
            for frames in count(1):
                new_frame = gif.copy()
                new_frame.thumbnail((size[0], size[1]), Image.ANTIALIAS)
                frame = ImageTk.PhotoImage(new_frame)
                self.widget.config(image=frame)
                self.widget.image = frame
                gif.seek(frames)
        except EOFError as exc:
            pass

    def _insert_image(self):
        image = Image.open(self.file)
        size = self.get_size(self.file)

        resized_image = image.resize((size[0], size[1]), Image.ANTIALIAS)
        self.widget.image = resized_image
        self.widget.config(image=image)

    @staticmethod
    def get_size(file):
        try:
            media_file = Image.open(file)
            width, height = media_file.size[0], media_file.size[1]
        except Exception as exc:
            video = cv.VideoCapture(file)
            height = video.get(cv.CAP_PROP_FRAME_HEIGHT)
            width = video.get(cv.CAP_PROP_FRAME_WIDTH)

        if width <= 7680 and height <= 4320:
            return int(float(width / 100 * 20)), int(float(height / 100 * 20))
        if width <= 3840 and height <= 2160:
            return int(float(width / 100 * 30)), int(float(height / 100 * 30))
        if width <= 2048 and height <= 1080:
            return int(float(width / 100 * 40)), int(float(height / 100 * 40))
        if width <= 1920 and height <= 1080:
            return int(float(width / 100 * 50)), int(float(height / 100 * 50))
        if width <= 1280 and height <= 720:
            return int(float(width / 100 * 60)), int(float(height / 100 * 60))
        else:
            return int(float(width / 100 * 50)), int(float(height / 100 * 50))

    @staticmethod
    def _get_file_name(file):
        return os.path.basename(file)

    @staticmethod
    def _split_file(file):
        file_path_name, file_extension = os.path.splitext(file)
        return file_path_name, file_extension
