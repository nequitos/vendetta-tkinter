from src.client.handlers.server_handler import BasicDispatchClient

connection = BasicDispatchClient()
event_loop = connection.event_loop
