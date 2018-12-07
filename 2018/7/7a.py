#!/usr/bin/python3

import sys
import re
from collections import defaultdict

data = []
with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")[:-1]
    for l in lines:
        data.append( (re.findall("Step [A-Z]", l)[0][5], re.findall("step [A-Z]", l)[0][5]) )
# print(data)

dependancies = defaultdict(lambda: [])
remaining = set()
for tup in data:
    before, step = tup
    dependancies[step].append(before)
    remaining.add(before)
    remaining.add(step)
# print(dependancies)
# print(remaining)

order = ""
while len(remaining) != 0:
    candidates = []
    for step in remaining:
        if dependancies[step] == []:
            candidates.append(step)
    candidates = sorted(candidates)

    next = candidates[0]

    order += next

    for step in dependancies:
        dependancies[step] = [c for c in dependancies[step] if c != next]
    remaining.remove(next)

print(order) 