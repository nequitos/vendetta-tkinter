import logging
import asyncio

import socket
import pickle

from data.config import db_config, host, port
from event_types import Events
import psycopg

from time import ctime

users = []


class BaseRequestHandler(socket.socket):
    def __init__(self):
        super(BaseRequestHandler, self).__init__(
            socket.AF_INET, socket.SOCK_STREAM
        )
        self.logger = logging.getLogger('server_tcp')

        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)

        self.set_up()

    def set_up(self):
        self.logger.debug('Create server')
        self.bind(
            (host, port)
        )
        self.listen()

        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.setblocking(False)
        self.settimeout(0)

    def start_server(self):
        self.logger.debug('Start server host {}, port {}'.format(host, port))
        self.event_loop.run_until_complete(self.accepted_client())

    async def accepted_client(self):
        while True:
            conn, addr = await self.event_loop.sock_accept(self)
            self.logger.debug('Accepted client connection {}, address {}'.format(conn, addr))
            users.append(conn)

            self.event_loop.create_task(self.listen_client(conn))

    async def listen_client(self, conn):
        while True:
            data = await self.event_loop.sock_recv(conn, 1024)
            obj = pickle.loads(data)

            if not data:
                logger.debug('Remove from active user {}'.format(conn))
                users.remove(conn)
                continue
            else:
                logger.debug('Received data {}'.format(pickle.loads(data)))

                if obj['type'] == Events.MESSAGE_NEW:
                    if obj['dialog_name'] == 'main':
                        for user in users:
                            if conn != user:
                                await self.send_data(user, dialog_name=obj['dialog_name'], data=obj['data'])

    async def send_data(self, conn, **kwargs):
        if not kwargs:
            return
        else:
            self.logger.debug('Sending data to connection {} {}'.format(conn, kwargs))
            await self.event_loop.sock_sendall(conn, pickle.dumps(kwargs))


class BaseDBHandler:
    def __init__(self):
        self.event_loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.event_loop)

        self.logger = logging.getLogger('db')

        try:
            self.connection = self.event_loop.run_until_complete(self.start_db())
        except Exception as exc:
            self.logger.debug('{}'.format(exc))
        finally:
            self.event_loop.run_until_complete(self.create_table())

    async def start_db(self):
        self.logger.debug('Create connection to database')
        async with await psycopg.AsyncConnection.connect(
                dbname=db_config["dbname"],
                user=db_config["user"],
                password=db_config["password"],
                host=db_config["host"],
                port=db_config["port"]
        ) as connection:
            return connection

    async def create_table(self):
        self.logger.debug('Creating table')
        try:
            async with self.connection.cursor() as cur:
                pass
        except Exception as exc:
            self.logger.debug('{}'.format(exc))

    async def insert_data(self):
        pass

    async def search_data(self):
        pass

    async def delete_data(self):
        pass


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.DEBUG,
        filename=None  # 'logs/' + ctime().replace(':', '.') + '.log'
    )
    logger = logging.getLogger('main')

    asyncio.set_event_loop_policy(
        asyncio.WindowsSelectorEventLoopPolicy()
    )
    try:
        with BaseRequestHandler() as server_tcp:
            server_tcp.start_server()
    except Exception as exc:
        logger.error('{}'.format(exc))