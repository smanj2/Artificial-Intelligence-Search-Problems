#!/usr/local/bin/python3
#
# find_luddy.py : a simple maze solver
#
# Submitted by : [SRI HARSHA MANJUNATH - SRMANJ]
# Based on skeleton code by Z. Kachwala, 2019
#

import sys
import json

# Parse the map from a given filename
def parse_map(filename):
    with open(filename, "r") as f:
        return [[char for char in line] for line in f.read().split("\n")]

# Check if a row,col index pair is on the map
def valid_index(pos, n, m):
    return 0 <= pos[0] < n  and 0 <= pos[1] < m

# Find the possible moves from position (row, col)
def moves(map, row, col):
    moves=(((row+1,col),"S"), ((row-1,col),"N"), ((row,col-1),"W"), ((row,col+1),"E"))
    # Return only moves that are within the board and legal (i.e. on the sidewalk ".")
    return [ move for move in moves if valid_index(move[0], len(IUB_map), len(IUB_map[0]))and(IUB_map[move[0][0]][move[0][1]] in ".@" )]

# Perform search on the map
def search1(IUB_map):
    you_loc=[(row_i,col_i) for col_i in range(len(IUB_map[0])) for row_i in range(len(IUB_map)) if IUB_map[row_i][col_i]=="#"][0]
    fringe=[(you_loc,0,'')]

    while fringe:
        (curr_move, curr_dist,cord)=fringe.pop(0)
        visited.append(curr_move)

        for move in moves(IUB_map, *curr_move):
            if IUB_map[move[0][0]][move[0][1]] == '@':
                curr_dist = curr_dist+1
                fringe.append((move[0], curr_dist,cord + move[1]))
                return curr_dist, cord+move[1]
            else:
                if move[0] in visited:
                    pass
                else:
                    fringe.append((move[0], curr_dist + 1,cord + move[1]))


# Main Function
if __name__ == "__main__":
    visited = []
    IUB_map=parse_map(sys.argv[1])
    print("Shhhh... quiet while I navigate!")
    solution = search1(IUB_map)
    if solution is None:
        print('Inf')
    else:
        print("Here's the solution I found:")
        print(solution[0],solution[1])
