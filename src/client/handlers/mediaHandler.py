from ttkbootstrap.constants import *
import ttkbootstrap as ttk

from PIL import Image, ImageTk
from itertools import count

from pathlib import Path
import os

from src.client.handlers.animatedLabelHandler import AnimatedLabelHandler


class MediaHandler(ttk.Label):
    def __init__(self, parent, widget, file):
        super(MediaHandler, self).__init__(parent)
        self._temp_path = str(Path(__file__).parent.parent) + '/temp/img'
        print(self._temp_path)
        self.parent = parent
        self.widget = widget
        self.file = file

        self.image_extensions = ['.png', '.jpg', '.jpeg', '.gif']
        self.handle()

    def handle(self):
        file_extension = self._split_file(self.file)[1]
        if file_extension in self.image_extensions:
            image_file = Image.open(self.file)

            # Image settings
            print(image_file.size[:])
            resized_image = self.image_resize(image_file, file_extension)
            print(resized_image.size[:])

            if file_extension == '.gif':
                AnimatedLabelHandler(self.parent, self.widget, image_file)
            else:
                resized_image = ImageTk.PhotoImage(resized_image)
                self.widget.image = resized_image
                self.widget.config(image=resized_image)

    @staticmethod
    def image_resize(image_file, extension):
        image_width = image_file.size[0]
        image_height = image_file.size[1]
        resized_image = image_file

        # if image_width <= 8000 and image_height <= 8000:
        #     image_file.resize((int(float(image_width / 100 * 50)), int(float(image_height / 100 * 50))))
        # if image_width <= 4000 and image_height <= 4000:
        #     image_file.resize((int(float(image_width / 100 * 30)), int(float(image_height / 100 * 30))))
        # if image_width <= 2000 and image_height <= 2000:
        #     image_file.resize((int(float(image_width / 100 * 20)), int(float(image_height / 100 * 20))))

        if image_width <= 1920 and image_height <= 1080:
            if extension == '.gif':
                pass
            else:
                resized_image = image_file.resize(
                    (int(float(image_width / 100 * 50)), int(float(image_height / 100 * 50))), Image.ANTIALIAS
                )

        return resized_image

    @staticmethod
    def _get_file_name(file):
        return os.path.basename(file)

    @staticmethod
    def _split_file(file):
        file_path_name, file_extension = os.path.splitext(file)
        return file_path_name, file_extension
