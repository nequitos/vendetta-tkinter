import asyncio
import logging

import socket
import pickle


class Events:
    MESSAGE_NEW = 'message_new'
    START_MESSAGE = 'start_message'
    LOGIN_CODE = 'login_code'
    REGISTRATION_CODE = 'registration_code'
    RECOVERY_CODE = 'recovery_code'

    RECEIVE_LOGIN_CODE = 'receive_login_code'
    RECEIVE_REGISTRATION_CODE = 'registration_code'
    RECEIVE_RECOVERY_CODE = 'receive_recovery_code'


class BasicDispatchClient(socket.socket):
    def __init__(self):
        super(BasicDispatchClient, self).__init__()
        self.host, self.port = 'localhost', 65044
        self.logger = logging.getLogger('connection')

        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)

        try:
            self.set_up()
        except Exception as exc:
            logger.error('{}'.format(exc))

    def set_up(self):
        self.logger.debug('Connect to server host {}, port {}'.format(self.host, self.port))
        self.connect(
            (self.host, self.port)
        )

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
        structure = self.get_structure(**kwargs)
        if len(kwargs) > 0:
            self.logger.debug('Sending data to server')
            await self.event_loop.sock_sendall(self, pickle.dumps(kwargs))
            self.logger.debug('Data sent successfully')

    @staticmethod
    def get_structure(**kwargs):
        structure = {}
        if kwargs['type'] == Events.MESSAGE_NEW:
            structure['type'] = Events.MESSAGE_NEW
            structure['data'] = kwargs['data']
            structure['dialog_name'] = kwargs['dialog_name']

        if kwargs['type'] == Events.START_MESSAGE:
            structure['type'] = Events.START_MESSAGE
            structure['data'] = 'This is start message'

        if kwargs['type'] == Events.LOGIN_CODE:
            structure['type'] = Events.LOGIN_CODE
            structure['code'] = kwargs['code']

        if kwargs['type'] == Events.REGISTRATION_CODE:
            structure['type'] = Events.REGISTRATION_CODE
            structure['code'] = kwargs['code']

        if kwargs['type'] == Events.RECOVERY_CODE:
            structure['type'] = Events.RECOVERY_CODE
            structure['code'] = kwargs['code']

        if kwargs['type'] == Events.RECEIVE_REGISTRATION_CODE:
            structure['type'] = Events.RECEIVE_REGISTRATION_CODE

        return structure


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
                type=Events.MESSAGE_NEW, data='Start message', dialog_name='main')
            )

            loop.run_until_complete(asyncio.gather(data, send))

    finally:
        logger.debug('Closing event loop')
        loop.close()


