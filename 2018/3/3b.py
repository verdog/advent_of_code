#!/usr/bin/python3

import sys

class Coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False

    def __ne__(self, other):
        return not self == other

    def __hash__(self):
        return ( self.x ) << 32 | self.y

class Claim:
    def __init__(self, x, y, w, h, id):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.id = id

    def __str__(self):
        return str(self.x) + ',' + str(self.y) + ': ' + str(self.w) + 'x' + str(self.h)

    def __eq__(self, other):
        if other == None:
            return False
        return self.x == other.x and self.y == other.y and self.w == other.w and self.h == other.h

def get_overlap(a: Claim, b: Claim):
    if a.x < b.x + b.w and \
       a.x + a.w > b.x and \
       a.y < b.y + b.h and \
       a.y + a.h > b.y:
        return Claim(max(a.x, b.x), max(a.y, b.y), min(a.x + a.w, b.x + b.w) - max(a.x, b.x), min(a.y + a.h, b.y + b.h) - max(a.y, b.y), -1)

    else:
        return None

marked = set()
def mark_squares(claim: Claim):
    global marked
    for i in range(claim.x, claim.x+claim.w):
        for j in range(claim.y, claim.y+claim.h):
            marked.add(Coords(i, j))

rawlines = []
claims = []

with open(sys.argv[1], "r") as f:
    for line in f:
        rawlines.append(line.strip())

for line in rawlines:
    split = line.split()
    # oof
    claims.append(Claim(int(split[2].split(',')[0]), int(split[2].split(',')[1][:-1]), int(split[3].split('x')[0]), int(split[3].split('x')[1]), int(split[0][1:])))

for claim in claims:
    no_collisions = True
    for other in claims:
        if claim == other:
            continue

        overlap = get_overlap(claim, other)
        if (overlap != None):
            no_collisions = False
            break

    if no_collisions == True:
        print(claim.id)
        break