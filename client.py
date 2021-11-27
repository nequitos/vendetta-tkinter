
from socket import socket
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
        structure = {}
        return pickle.dumps(*args, **kwargs)

    def set_up(self):

        if os.path.exists('temp/'):
            os.mkdir('temp/')

        self.connect(
            ('localhost', 65044)
        )
        self.setblocking(False)

    def start_client(self):
        self.loop.run_until_complete(self.get_tasks())

    async def listen_server(self):
        while True:
            data = await self.loop.sock_recv(self, 1024)
            print(data.decode('utf-8'))

    async def send_data(self, message=None, chat_name=None):
        while True:

            async with aiofiles.open('temp/message_send_' + chat_name + '.txt', 'w', encoding='utf-8') as message_fl:
                await message_fl.write(message)

            async with aiofiles.open('temp/message_send_' + chat_name + '.txt', 'rb') as message_fl:
                while True:
                    data = await message_fl.read(1024)

                    if data == b'':
                        break

                    await self.loop.sock_sendall(self, self.get_structure(data))

                os.remove('temp/messages_send_' + chat_name + '.txt')

    async def get_tasks(self):
        listen_server_task = self.loop.create_task(self.listen_server())
        send_server_task = self.loop.create_task(self.send_data())

        await asyncio.gather(listen_server_task, send_server_task)


if __name__ == '__main__':
    client = BasicDispatchClient()