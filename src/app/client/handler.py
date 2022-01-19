import asyncio
import logging

import socket
import pickle


class BasicDispatchClient(socket.socket):
    def __init__(self):
        super(BasicDispatchClient, self).__init__(
            socket.AF_INET, socket.SOCK_STREAM
        )
        self.host, self.port = 'localhost', 65044
        self.logger = logging.getLogger('connection')

        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)

    def set_up(self):
        self.logger.debug('Connect to server host {}, port {}'.format(self.host, self.port))
        self.connect(
            (self.host, self.port)
        )

    async def listen_server(self):
        while True:
            self.logger.debug('Waiting for the data to be received from the server')
            data = await self.event_loop.sock_recv(self, 1024)
            if not data:
                pass
            else:
                self.logger.debug('Data received {}'.format(pickle.loads(data)))
                return data

    async def send_data(self, **kwargs):
        structure = {'type': kwargs['type'], 'data': kwargs['data']}

        if len(structure) > 0:
            self.logger.debug('Sending data to server')
            await self.event_loop.sock_sendall(self, pickle.dumps(structure))
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
            loop.run_until_complete(connection.send_data(type='message', data='My message'))
    finally:
        logger.debug('Closing event loop')
        loop.close()


