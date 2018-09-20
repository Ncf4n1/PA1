#!/usr/bin/python3
# Logan Vining & Glen Johnson
# Battleship Network Application PA1
# September 20, 2018
# YouTube Video Link: https://youtu.be/DZxl4h9Yejg

import sys, http.client, re

ip = sys.argv[1]

port = sys.argv[2]

#init opponent board
opp_boa = []
#put opponent board into 2d list
with open('opponent_board.txt', 'r') as f:
    while True:
        c = f.readline()
        if not c:
            break
        opp_boa.append(list(c))
#Put board coords in recognizable var
x = sys.argv[3]
y = sys.argv[4]

#connect to the server
conn = http.client.HTTPConnection(ip + ':' + port)

#Send the message to the server
conn.request("POST", "/", "x=" + x + "&y=" + y)
#Receive response
res = conn.getresponse()
#Check if it was a good request
if(res.status == 200):
    mess = res.read().decode('utf-8')
    #look for relevent info in response
    match = re.findall('([0,1])|([0,D,S,R,B,C])', mess)
    hit = match[0][0]
    sink = match[1][1]

    #result from server, modify opponent board with hit, sink, or miss
    if hit == "1":
        if sink == "D":
            opp_boa[int(y)][int(x)] = 'H'
            print("You sunk the Destroyer!")
        elif sink == "S":
            opp_boa[int(y)][int(x)] = 'H'
            print("You sunk the Submarine!")
        elif sink == "R":
            opp_boa[int(y)][int(x)] = 'H'
            print("You sunk the Cruiser!")
        elif sink == "B":
            opp_boa[int(y)][int(x)] = 'H'
            print("You sunk the Battleship!")
        elif sink == "C":
            opp_boa[int(y)][int(x)] = 'H'
            print("You sunk the Carrier!")
        else:
            opp_boa[int(y)][int(x)] = 'H'
            print("You hit something!")
    else:
        opp_boa[int(y)][int(x)] = 'M'
        print("You missed!")
else:
    print(res.status, res.reason)


#copy opponent board back into file
with open('opponent_board.txt', 'w') as f:
    for y in range(len(opp_boa)):
        for x in range(len(opp_boa[y])):
            f.write(opp_boa[y][x])
