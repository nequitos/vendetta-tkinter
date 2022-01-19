from setup import *


class ServerTCP(socket.socket):
    def __init__(self):
        super(ServerTCP, self).__init__(
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

            self.event_loop.create_task(self.listen_client(conn))

    async def listen_client(self, conn):
        while True:
            data = await self.event_loop.sock_recv(conn, 1024)

            if not data:
                continue
            else:
                logger.debug('Received data {}'.format(pickle.loads(data)))
                print(pickle.loads(data))

    async def send_data(self, conn, data=None):
        if not data:
            return
        else:
            self.logger.debug('Sending data {}'.format(data))
            await self.event_loop.sock_sendall(conn, pickle.dumps(data))


if __name__ == '__main__':
    with ServerTCP() as server_tcp:
        server_tcp.start_server()