#!/usr/bin/python3

import sys

print ('Server IP: ', sys.argv[1])
print ('Server Port: ', sys.argv[2])
print ('Salvo Coordinates: ', sys.argv[3], ', ', sys.argv[4])
x = sys.argv[3]
y = sys.argv[4]

opp_boa = []
with open('opponent_board.txt', 'r') as f:
    while True:
        c = f.readline()
        if not c:
            break
        opp_boa.append(list(c))

hit = True
if(hit):
    opp_boa[int(y)-1][int(x)-1] = 'H'

with open('opponent_board.txt', 'w') as f:
    for y in range(len(opp_boa)):
        for x in range(len(opp_boa[y])):
            f.write(opp_boa[y][x])
