# Logan Vining & Glen Johnson
# Battleship Network Application PA1
# September 20, 2018
# YouTube Video Link: https://youtu.be/DZxl4h9Yejg

import sys      # Used to get Command Line Arguments
import re       # Used for Coordinates Regex

# Used to Send and Receive HTTP Messages to client.py
from http.server import HTTPServer, BaseHTTPRequestHandler

# Get Port from Command Line Argument
PORT = int(sys.argv[1])

# initialize counters to track sinking of ships
CARRIER = 0
BATTLESHIP = 0
SUBMARINE = 0
CRUISER = 0
DESTROYER = 0

#initialize own board
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

    # Function to handle incoming HTTP GET Messages
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Statements to print own_board and opponent_board to a web browser
        if(self.path == "/opponent_board.html"):
            with open('opponent_board.txt', 'r') as f:
                while True:
                    c = f.readline()
                    self.wfile.write(bytes("<p>" + c + "<p>", "utf-8"))
                    if not c:
                        break
        elif(self.path == "/own_board.html"):
            with open('own_board.txt', 'r') as f:
                while True:
                    c = f.readline()
                    self.wfile.write(bytes("<p>" + c + "<p>", "utf-8"))
                    if not c:
                        break

    # Function called when POST message received
    def do_POST(self):

        # First use regex to get the coordinates from the fire message
        content_length = int(self.headers['Content-length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        print(post_data)
        coord_list = re.findall(r'\d+', str(post_data))

        # Check if the coordinates are formatted correctly
        if len(coord_list) != 2:
            self.send_response(400)
            self.end_headers()
        else:
            x = int(coord_list[0])
            y = int(coord_list[1])

            # Check if the coordinates are out of index range
            if ( (x > 9 or y > 9) or (x < 0 or y < 0) ):
                self.send_response(404)
                self.end_headers()

            # Then check if the coordinates were already sent
            elif ( own_board[y][x] == 'H' or own_board[y][x] == 'M'):
                self.send_response(410)
                self.end_headers()
            else:
                hit = 0

                # Determine if a ship was hit, and if so, which one
                if own_board[y][x] != '_':
                    hit = 1
                    if own_board[y][x] == 'C':
                        global CARRIER
                        CARRIER += 1
                        own_board[y][x] = 'H'
                    elif own_board[y][x] == 'B':
                        global BATTLESHIP
                        BATTLESHIP += 1
                        own_board[y][x] = 'H'
                    elif own_board[y][x] == 'R':
                        global CRUISER
                        CRUISER += 1
                        own_board[y][x] = 'H'
                    elif own_board[y][x] == 'S':
                        global SUBMARINE
                        SUBMARINE += 1
                        own_board[y][x] = 'H'
                    elif own_board[y][x] == 'D':
                        global DESTROYER
                        DESTROYER += 1
                        own_board[y][x] = 'H'
                else:
                    own_board[y][x] = 'M'


                # Update own_board with opponents hits and misses
                with open('own_board.txt', 'w') as f:
                    for y in range(len(own_board)):
                        for x in range(len(own_board[y])):
                            f.write(own_board[y][x])

                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                # Format and return a hit (and possibly sink) message
                message = "hit=" + str(hit)

                message_add = '\&sink=0'
                if CARRIER == 5:
                    message_add = '\&sink=C'
                    CARRIER += 1
                elif BATTLESHIP == 4:
                    message_add = '\&sink=B'
                    BATTLESHIP += 1
                elif CRUISER == 3:
                    message_add = '\&sink=R'
                    CRUISER += 1
                elif SUBMARINE == 3:
                    message_add = '\&sink=S'
                    SUBMARINE += 1
                elif DESTROYER == 2:
                    message_add = '\&sink=D'
                    DESTROYER += 1

                # Send backt the return message to the client
                message = (message + message_add).encode('utf-8')
                print(message.decode('utf-8'))
                self.wfile.write(bytes(message))


# Function that initializes and runs the actual server process
def run(server_class = HTTPServer, handler_class = BattleshipHTTPRequestHandler):
    server_address = ('', PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

init_board()
run()
