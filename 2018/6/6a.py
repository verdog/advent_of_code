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

idletter = 'a'
def genletter():
    global idletter
    retval = idletter
    idletter = chr(ord(idletter) + 1)
    return retval

areas = defaultdict(lambda: 0)
pointtoletter = defaultdict(genletter)

visualmap = ""
for y in range(miny-1, maxy+2):
    for x in range(minx-1, maxx+2):
        lowdist = None
        lowpoint = None
        seen = defaultdict(lambda: 0)
        for point in points:
            dist = mandist((x, y), point)
            seen[dist] += 1

            if lowdist == None or dist < lowdist:
                lowdist = dist
                lowpoint = point
            
        if seen[lowdist] == 1:
            # print(x, y, lowpoint, lowdist, seen[lowdist])
            areas[lowpoint] += 1
            if (lowdist == 0):
                visualmap += pointtoletter[lowpoint].upper()
            else:
                visualmap += pointtoletter[lowpoint]
                
        else:
            visualmap += "."
        
    visualmap += "\n"

print(visualmap)

bad = defaultdict(lambda: False)

def markbad(xlow, xhigh, ylow, yhigh):
    global bad
    for x in range(xlow, xhigh+1):
        for y in range(ylow, yhigh+1):
            lowdist = None
            lowpoint = None
            seen = defaultdict(lambda: 0)
            for point in points:
                dist = mandist((x, y), point)
                seen[dist] += 1

                if lowdist == None or dist < lowdist:
                    lowdist = dist
                    lowpoint = point
                
            if seen[lowdist] == 1:
                # print("kill", lowpoint)
                bad[lowpoint] = True

markbad(minx, maxx, miny, miny)
markbad(minx, maxx, maxy, maxy)
markbad(minx, minx, miny, maxy)
markbad(maxx, maxx, miny, maxy)

# print(areas)
print(max([areas[p] for p in points if bad[p] == False]))
