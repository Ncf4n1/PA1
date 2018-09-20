#!/usr/bin/python3

import sys, http.client, re

#Print statements to show input values
print ('Server IP: ', sys.argv[1])
ip = sys.argv[1]
print ('Server Port: ', sys.argv[2])
port = sys.argv[2]
print ('Salvo Coordinates: ', sys.argv[3], ', ', sys.argv[4])

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
print(res.status, res.reason)
mess = res.read().decode('utf-8')
#look for relevent info in response
match = re.search('hit=(.*)&sink=(.*)', mess)
hit = match.group(1)
sink = match.group(2)

#result from server, modify opponent board with hit or miss
if hit == "1":
    if sink == "D"
        opp_boa[int(y)-1][int(x)-1] = 'S'
        print("You sunk the Destroyer!")
    elif sink == "S"
        opp_boa[int(y)-1][int(x)-1] = 'S'
        print("You sunk the Submarine!")
    elif sink == "R"
        opp_boa[int(y)-1][int(x)-1] = 'S'
        print("You sunk the Cruiser!")
    elif sink == "B"
        opp_boa[int(y)-1][int(x)-1] = 'S'
        print("You sunk the Battleship!")
    elif sink == "C"
        opp_boa[int(y)-1][int(x)-1] = 'S'
        print("You sunk the Carrier!")
    else
        opp_boa[int(y)-1][int(x)-1] = 'H'
        print("You hit something!")
else:
    opp_boa[int(y)-1][int(x)-1] = 'M'
    print("You missed!")


#copy opponent board back into file
with open('opponent_board.txt', 'w') as f:
    for y in range(len(opp_boa)):
        for x in range(len(opp_boa[y])):
            f.write(opp_boa[y][x])
