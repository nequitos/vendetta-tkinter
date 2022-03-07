from src.client.app_api.constants import *
from src.client.app_api.structures import get_response_structure

import asyncio
import logging

import socket
import pickle


class BasicDispatchClient(socket.socket):
    def __init__(self):
        super(BasicDispatchClient, self).__init__()
        self.host, self.port = 'localhost', 65044
        self.logger = logging.getLogger('connection')

        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)

    def set_up(self):
        self.logger.debug('Connect to server host {}, port {}'.format(self.host, self.port))
        self.connect(
            (self.host, self.port)
        )
        self.setblocking(True)

    def listen_server(self):
        self.logger.debug('Waiting for the data to be received from the server')
        data = self.recv(1024)
        if not data:
            self.logger.debug('Data on server has not information')
            return
        else:
            print(pickle.loads(data))
            self.logger.debug('Data received {}'.format(pickle.loads(data)))
            return pickle.loads(data)

    async def send_data(self, **kwargs):
        response_structure = get_response_structure(**kwargs)
        if len(response_structure) > 0:
            self.logger.debug('Sending data to server')
            await self.event_loop.sock_sendall(self, pickle.dumps(response_structure))
            self.logger.debug('Data sent successfully')


# For debugging
if __name__ == '__main__':
    try:
        with BasicDispatchClient() as connection:
            logger = connection.logger
            logger.setLevel(logging.DEBUG)
            logger.debug('Waiting for client to complete')
            loop = connection.event_loop
            connection.set_up()
            data = loop.create_task(connection.listen_server())
            send = loop.create_task(connection.send_data(
                type=MESSAGE_NEW, data='Start message', dialog_name='main')
            )

            loop.run_until_complete(asyncio.gather(data, send))

    finally:
        logger.debug('Closing event loop')
        loop.close()


