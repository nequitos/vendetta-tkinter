from data.config import db_config
import pickle

import socketserver
import psycopg2
import logging
import time


class BaseRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print(self.client_address)
        while True:
            data = self.request.recv(1024)

            if not data:
                continue
            else:
                print(data.decode('utf-8'))

    def finish(self):
        pass


if __name__ == '__main__':
    host, port = 'localhost', 65044
    now_time = time.ctime()

    logging.basicConfig(
        level=logging.DEBUG,
        filename='logs/' + time.ctime().replace(':', '.') + '.log'
    )
    logger_main = logging.getLogger('main')

    try:
        connection = psycopg2.connect(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"]
        )
    except Exception as exc:
        logger_main.error('{}'.format(exc))
    finally:
        with socketserver.ThreadingTCPServer((host, port), BaseRequestHandler, bind_and_activate=True) as server:
            server.serve_forever()