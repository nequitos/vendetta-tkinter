
import asyncio
import socket
import json
import sys
import os


class Socket(socket.AF_INET, socket.SOCK_STREAM):
    pass