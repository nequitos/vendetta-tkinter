
from socket import socket
import threading
import aiofiles
import asyncio

import pickle
import json
import os


class BasicDispatchClient(socket):
    def __init__(self):
        super(BasicDispatchClient, self).__init__()
        self.loop = asyncio.get_event_loop()
        self.set_up()

    @staticmethod
    def get_structure(*args, **kwargs):
        structure = {
            'message': [],
            'file': []
        }
        return pickle.dumps(*args, **kwargs)

    def set_up(self):

        if os.path.exists('temp/'):
            os.mkdir('temp/')

        self.connect(
            ('localhost', 65045)
        )
        self.setblocking(False)

    def start_client(self):
        threading.Thread(self.loop.run_until_complete(self.get_tasks())).start()

    async def listen_server(self):
        while True:
            data = await self.loop.sock_recv(self, 1024)
            print(data.decode('utf-8'))

    async def send_data(self, message=None, chat_name=None):
        while True:
            await self.loop.sock_sendall(self, message.encode('utf-8'))

    async def get_tasks(self):
        listen_server_task = self.loop.create_task(self.listen_server())
        send_server_task = self.loop.create_task(self.send_data())

        await asyncio.gather(listen_server_task, send_server_task)