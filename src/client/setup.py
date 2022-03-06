from app_api import *

import logging
import asyncio

from handlers import *
from data.config import theme

from time import ctime
from os.path import exists
from os import mkdir
import pickle

from multiprocessing import Process
from threading import Thread

if not exists('client/logs'):
    mkdir('client/logs')

logging.basicConfig(
    level=logging.DEBUG,
    filename=None #'client/logs/' + ctime().replace(':', '.') + '.log'
)
logger = logging.getLogger('application')

connection = BasicDispatchClient()
event_loop = connection.event_loop
asyncio.set_event_loop(event_loop)