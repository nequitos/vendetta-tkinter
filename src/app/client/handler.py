import asyncio
import logging

import socket
import pickle
import time


host, port = 'localhost', 65044


class BasicDispatchClient(socket.socket):
    def __init__(self):
        super(BasicDispatchClient, self).__init__()
        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)
        self.set_up()

    def set_up(self):
        self.connect(
            (host, port)
        )

    def start_client(self):
        self.event_loop.run_until_complete(self.get_tasks())

    async def listen_server(self):
        data = await self.event_loop.sock_recv(self, 1024)
        print(data)

    async def send_data(self, data: str):
        await self.event_loop.sock_sendall(self, data.encode('utf-8'))

    async def get_tasks(self):
        listen_server_task = self.event_loop.create_task(self.listen_server())
        send_data_task = self.event_loop.create_task(self.send_data(''))

        await asyncio.gather(listen_server_task, send_data_task)


# For debugging
if __name__ == '__main__':
    now_time = time.ctime()

    logging.basicConfig(
        level=logging.DEBUG,
        filename=None # 'logs/' + now_time.replace(':', '.') + '.log'
    )
    logger = logging.getLogger('main')

    logger.debug('Waiting for client to complete')
    try:
        with BasicDispatchClient() as connection:
            loop = connection.event_loop
            loop.run_until_complete(connection.send_data(data='My message'))
    finally:
        logger.debug('Closing event loop')
        loop.close()
