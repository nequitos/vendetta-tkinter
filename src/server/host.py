from server_tcp import ServerTCP

from setup import *


if __name__ == '__main__':
    try:
        with BaseDBHandler() as db:
            pass

        with ServerTCP() as server_tcp:
            server_tcp.start_server()

    except Exception as exc:
        logger.error('{}'.format(exc))