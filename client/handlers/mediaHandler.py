from PIL import Image, ImageTk
import cv2 as cv
import imageio

import pydub
# import pyaudio

from itertools import count

from pathlib import Path
import os.path
import pickle


class MediaHandler:
    def __init__(self, media_file, size, save_path):

        if save_path:
            self.save_path = save_path
        else:
            _temp_file = str(Path(__file__).parent.parent.absolute()) + '/temp/media/'
            self.save_path = _temp_file + self.split_file(media_file)[0]

            if not os.path.exists(_temp_file):
                os.mkdir(_temp_file)

        self.media_file = media_file
        self.size = size

    def load_gif(self):
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

            if not os.path.exists(self.save_path):
                with open(self.save_path + '.pkl', 'w') as media_fl:
                    pickle.dump({'frames': frames, 'delay': delay}, media_fl)

    def load_video(self):
        video = imageio.get_reader(self.media_file)
        index = 0
        frames = {}

        try:
            for frame in video.iter_data():
                image = ImageTk.PhotoImage(Image.fromarray(frame).resize((self.size[0], self.size[1]), Image.ANTIALIAS))
                frames[index] = image
                index += 1
        except EOFError:
            pass

        delay = 40

        if not os.path.exists(self.save_path):
            with open(self.save_path + '.pkl', 'w') as media_fl:
                pickle.dump({'frames': frames, 'delay': delay}, media_fl)

    def load_image(self):
        with Image.open(self.media_file) as image:
            resized_image = image.resize((self.size[0], self.size[1]), Image.ANTIALIAS)

            return resized_image

    def load_music(self):
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
