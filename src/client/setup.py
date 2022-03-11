from pathlib import Path
import sys
import os

sys.path.append(str(Path(__file__).parent.parent.parent.absolute()))

temp_path = str(Path(__file__).parent) + '/temp'

if not os.path.exists(temp_path):
    os.mkdir(temp_path)

if not os.path.exists(temp_path + '/img'):
    os.mkdir(temp_path + '/img')
