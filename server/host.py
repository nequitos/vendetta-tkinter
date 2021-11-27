import asyncio
import socketserver
import pickle
import os


class BaseRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        while True:
            data = self.request.recv(1024)
            print(data.decode('utf-8'))

    def finish(self):
        raise NotImplementedError


if __name__ == '__main__':
    with socketserver.ThreadingTCPServer(('localhost', 65044), BaseRequestHandler, bind_and_activate=True) as server:
        server.serve_forever()
