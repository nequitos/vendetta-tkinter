from src.client.app_api.constants import *
from src.client.app_api.structures import get_response_structure

import logging
import asyncio

import socket
import pickle

from threading import Thread
from src.client.data.config import host, port


class BasicDispatchClient(socket.socket):
    def __init__(self):
        super(BasicDispatchClient, self).__init__(
            socket.AF_INET, socket.SOCK_STREAM
        )
        self.host, self.port = host, port
        self.logger = logging.getLogger('connection')

    def set_up(self):
        self.logger.debug('Connect to server host {}, port {}'.format(self.host, self.port))
        self.connect(
            (self.host, self.port)
        )

    def listen_server(self):
        while True:
            self.logger.debug('Waiting for the data to be received from the server')
            data = self.recv(1024)
            if not data:
                self.logger.debug('Data on server has not information')
                continue
            else:
                self.logger.debug('Data received {}'.format(pickle.loads(data)))
                return pickle.loads(data)

    def send_data(self, **kwargs):
        response_structure = get_response_structure(**kwargs)
        if len(response_structure) > 0:
            if kwargs['type'] == MEDIA_FILE:
                self.sendfile(kwargs['file'])
                self.send(kwargs['file_name'])

            else:
                self.logger.debug('Sending data to server')
                self.sendall(pickle.dumps(response_structure))
                self.logger.debug('Data sent successfully')


# For debugging
if __name__ == '__main__':
    with BasicDispatchClient() as connection:
        connection.set_up()