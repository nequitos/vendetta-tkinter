import logging
import asyncio

import socket
import pickle

from data.config import db_config
import psycopg

from time import ctime

from db_handler import BaseDBHandler
from data.config import host, port

logging.basicConfig(
    level=logging.DEBUG,
    filename=None  # 'logs/' + ctime().replace(':', '.') + '.log'
)
logger = logging.getLogger('main')

asyncio.set_event_loop_policy(
    asyncio.WindowsSelectorEventLoopPolicy()
)