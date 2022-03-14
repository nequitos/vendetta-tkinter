from PIL import Image, ImageTk
import cv2 as cv
import imageio

from itertools import count, cycle

from threading import Thread
import os


class MediaHandler:
    def __init__(self, widget, file):
        self.widget = widget
        self.file = file

        self.cancel = None
        self.ready_to_play = None
        self.frames, self.delay = 10, None

        self.file_extension = self._split_file(file)[1].lower()
        self.image_extensions = ['.png', '.jpg', '.jpeg']
        self.video_extensions = ['.mp4', '.mov', '.mkv', '.gif']

        self.handle()

    def handle(self):
        if self.file_extension in self.image_extensions:
            self._insert_image()
        if self.file_extension in self.video_extensions:
            if self.file_extension == '.gif':
                self.frames, self.delay = self._load_gif()
                self.ready_to_play = self._insert_gif
                self.cancel = self.widget.after(self.delay, self.ready_to_play)
            else:
                self.frames, self.delay = self._load_video()
                self.ready_to_play = self._insert_video
                self.cancel = self.widget.after(self.delay, self.ready_to_play)

    def play(self):
        thread = Thread(target=self.ready_to_play, args=(self.frames, self.delay))
        thread.daemon = 1
        thread.start()

    def toggle(self, event):
        self.widget.after_cancel(self.cancel)

    def stop(self):
        self.stop_thread_flag = True

    def proceed(self):
        self.stop_thread_flag = False

    def _insert_video(self, frames, delay, index=0):
        length = len(frames)
        frame = frames[index]

        if length == index:
            frame = frames[0]
            self.widget.config(image=frame)
            self.widget.image = frame
        else:
            self.widget.config(image=frame)
            self.widget.image = frame
            self.widget.after(40, lambda: self._insert_video(frames, delay, index+1))

    def _insert_gif(self, frames, delay, index=0):
        length = len(frames)
        frame = frames[index]

        if length == index:
            frame = frames[0]
            self.widget.config(image=frame)
            self.widget.image = frame
        else:
            self.widget.config(image=frame)
            self.widget.after(delay, lambda: self._insert_gif(frames, delay, index+1))

    def _load_video(self):
        video = imageio.get_reader(self.file)
        size = self.get_size(self.file)
        index = 0
        frames = {}

        try:
            for frame in video.iter_data():
                image = ImageTk.PhotoImage(Image.fromarray(frame).resize((size[0], size[1]), Image.ANTIALIAS))
                frames[index] = image
                index += 1
                print(frame)
        except EOFError:
            pass

        return frames, 40

    def _load_gif(self):
        gif = Image.open(self.file)
        size = self.get_size(self.file)
        frames = []

        try:
            for frames in count(1):
                new_frame = gif.copy()
                new_frame.thumbnail((size[0], size[1]), Image.ANTIALIAS)
                frames.append(ImageTk.PhotoImage(new_frame))
                gif.seek(frames)
        except EOFError as exc:
            pass

        try:
            delay = gif.info['duration']
        except Exception as exc:
            delay = 100

        return frames, delay

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
