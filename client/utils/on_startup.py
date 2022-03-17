from pathlib import Path
import os

temp_path = str(Path(__file__).parent) + '/temp'

if not os.path.exists(temp_path):
    os.mkdir(temp_path)

if not os.path.exists(temp_path + '/img'):
    os.mkdir(temp_path + '/img')
