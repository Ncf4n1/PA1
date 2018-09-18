import sys      # Used to get Command Line Arguments
import re       # Used for Coordinates Regex

# Used to Send and Receive HTTP Messages to client.py
from http.server import HTTPServer, BaseHTTPRequestHandler

# Get Port from Command Line Argument
PORT = int(sys.argv[1])

# Class that handles incoming fire messages from client
class BattleshipHTTPRequestHandler(BaseHTTPRequestHandler):

    # Function called when POST message received
    def do_POST(self):
        content_length = int(self.headers['Content-length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        coord_list = re.findall(r'\d', str(post_data))
        x = int(coord_list[0])
        y = int(coord_list[1])
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = "hit"
        self.wfile.write(message)

#init own board
own_board = []

#put own board into 2D list
with open('own_board.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        own_board.append(list(line))

def run(server_class = HTTPServer, handler_class = BattleshipHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
