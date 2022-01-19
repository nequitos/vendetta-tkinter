from setup import *


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
    BaseDBHandler()