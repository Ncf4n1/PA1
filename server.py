import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(sys.argv[1])

class BattleshipHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

#init own board
own_board = []

#put own board into 2D list
with open('own_board.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        own_board.append(list(line))

def run(server_class = HTTPServer, handler_class = BaseHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
