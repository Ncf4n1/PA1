import sys      # Used to get Command Line Arguments
import re       # Used for Coordinates Regex

# Used to Send and Receive HTTP Messages to client.py
from http.server import HTTPServer, BaseHTTPRequestHandler

# Get Port from Command Line Argument
PORT = int(sys.argv[1])

#init own board
own_board = []

# Function to initialize the player's own_board
def init_board():

    #put own board into 2D list
    with open('own_board.txt', 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            own_board.append(list(line))


# Class that handles incoming fire messages from client
class BattleshipHTTPRequestHandler(BaseHTTPRequestHandler):

    # Function called when POST message received
    def do_POST(self):
        content_length = int(self.headers['Content-length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        coord_list = re.findall(r'\d', str(post_data))
        x = int(coord_list[0])
        y = int(coord_list[1])

        hit = 0
        if own_board[y][x] != '_':
            hit = 1

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        message = ("hit=" + str(hit)).encode('utf-8')
        print(hit)
        self.wfile.write(bytes(message))


# Function that initializes and runs the actual server process
def run(server_class = HTTPServer, handler_class = BattleshipHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

init_board()
run()
