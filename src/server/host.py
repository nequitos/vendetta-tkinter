from data.config import db_config
import pickle

import socketserver
import psycopg2
import logging


class BaseRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        logger.debug('Received connection from host {}, port {}'.format(*self.client_address))
        while True:
            logger.debug('Waiting for data')
            data = pickle.loads(self.request.recv(1024))

            if not data:
                continue
            else:
                logger.debug('Received data {}'.format(data))
                print(data)

    def finish(self):
        pass


if __name__ == '__main__':
    from time import ctime

    logging.basicConfig(
        level=logging.DEBUG,
        filename='logs/' + ctime().replace(':', '.') + '.log'
    )
    logger = logging.getLogger('main')

    try:
        logger.debug('Database connection')
        connection = psycopg2.connect(
            dbname=db_config["dbname"],
            user=db_config["user"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"]
        )
        connection.autocommit = True

        logger.debug('Create user table')
        with connection.cursor() as cur:
            logger.debug('Create users database')
            # cur.execute(
            #     """
            #     CREATE TABLE users (
            #     id serial PRIMARY KEY,
            #     nick_name varchar(50) NOT NULL);
            #     """
            # )
            logger.debug('Users database successful created')

    except Exception as exc:
        logger.error('{}'.format(exc))
    else:
        logger.debug('Server start')
        try:
            host, port = 'localhost', 65044
            with socketserver.ThreadingTCPServer((host, port), BaseRequestHandler, bind_and_activate=True) as server:
                server.serve_forever()
        except Exception as exc:
            logger.error('{}'.format(exc))
        finally:
            logger.debug('Closing server')
            server.server_close()

            logger.debug('Closing database connection')
            connection.close()
