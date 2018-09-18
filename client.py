#!/usr/bin/python3

import sys

#Print statements to show input values
print ('Server IP: ', sys.argv[1])
print ('Server Port: ', sys.argv[2])
print ('Salvo Coordinates: ', sys.argv[3], ', ', sys.argv[4])
#Put board coords in recognizable var
x = sys.argv[3]
y = sys.argv[4]

#init opponent board
opp_boa = []
#put opponent board into 2d list
with open('opponent_board.txt', 'r') as f:
    while True:
        c = f.readline()
        if not c:
            break
        opp_boa.append(list(c))

#from result from server, modify opponent board with hit or miss
hit = True
if(hit):
    opp_boa[int(y)-1][int(x)-1] = 'H'

#copy opponent board back into file
with open('opponent_board.txt', 'w') as f:
    for y in range(len(opp_boa)):
        for x in range(len(opp_boa[y])):
            f.write(opp_boa[y][x])
