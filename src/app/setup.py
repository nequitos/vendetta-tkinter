from utils import *

import logging
import asyncio

from client import *
from src.app.data.config import theme

from time import ctime
from os.path import exists
from os import mkdir

if not exists('client/logs'):
    mkdir('client/logs')

logging.basicConfig(
    level=logging.DEBUG,
    filename='client/logs/' + ctime().replace(':', '.') + '.log')
logger = logging.getLogger('application')

connection = BasicDispatchClient()
event_loop = connection.event_loop
asyncio.set_event_loop(event_loop)
