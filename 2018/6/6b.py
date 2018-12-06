#!/usr/bin/python3

import sys
from collections import defaultdict

def mandist(a, b):
    return(abs(b[0] - a[0]) + abs(b[1] - a[1]))

with open(sys.argv[1], "r") as f:
    data = f.read().split('\n')[:-1]

minx = None
miny = None
maxx = None
maxy = None

points = []
for coords in data:
    points.append((int(coords.split(",")[0]), int(coords.split(",")[1])))

for point in points:
    if (minx == None or point[0] < minx):
        minx = point[0]
    if (maxx == None or point[0] > maxx):
        maxx = point[0]
    if (miny == None or point[1] < miny):
        miny = point[1]
    if (maxy == None or point[1] > maxy):
        maxy = point[1]

bound = int(sys.argv[2])
cap = int(sys.argv[3])
minx -= bound
miny -= bound
maxx += bound
maxy += bound

totalarea = 0
for y in range(miny-1, maxy+2):
    for x in range(minx-1, maxx+2):
        total = 0
        for point in points:
            dist = mandist((x, y), point)
            total += dist
        
        if total < cap:
            totalarea += 1
                
print(totalarea)
