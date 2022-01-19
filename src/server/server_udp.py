from setup import *


class ServerUDP(socket.socket):
    def __init__(self):
        super(ServerUDP, self).__init__(
            socket.AF_INET, socket.SOCK_DGRAM
        )
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.logger = logging.getLogger('server_udp')

        self.event_loop = asyncio.get_event_loop()

    def start_server(self):
        self.logger.debug('Start server host {}, port {}'.format(host, port))
        self.event_loop.run_until_complete(self.accepted_client())

    async def accepted_client(self):
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
