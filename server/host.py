

import socketserver

host, port = 'localhost', 65044


class BaseRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(3000000)
        addr = self.client_address
        conn = self.server


with socketserver.ThreadingTCPServer((host, port), BaseRequestHandler, bind_and_activate=True) as server:
    server.serve_forever()