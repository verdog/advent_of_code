#!/usr/bin/python3

import sys
import re
from collections import defaultdict

def steptime(c):
    # return ord(c) - 64
    return ord(c) - 64 + 60

data = []
with open(sys.argv[1], "r") as f:
    lines = f.read().split("\n")[:-1]
    for l in lines:
        data.append( (re.findall("Step [A-Z]", l)[0][5], re.findall("step [A-Z]", l)[0][5]) )
# print(data)

dependancies = defaultdict(lambda: [])
remaining = set()
all_steps = ""
for tup in data:
    before, step = tup
    dependancies[step].append(before)
    remaining.add(before)
    remaining.add(step)
# print(dependancies)
# print(remaining)

num_workers = 5
workers = defaultdict(lambda: None)
work_remaining = { c : steptime(c) for c in remaining }
done = ""
time_elapsed = 0

# print(work_remaining)
while len(remaining) != 0:
    # check if there are any free workers
    for i in range(num_workers):
        if workers[i] == None: # not assigned
            # assign to next 
            candidates = sorted([s for s in remaining if dependancies[s] == []])
            candidates = [c for c in candidates if c not in [workers[j] for j in range(num_workers)]]
            # print(candidates)
            if len(candidates) != 0:
                workers[i] = candidates[0]

    # print("assigned (1): ")
    # print(workers)

    # do a time step
    time_elapsed += 1
    for worker, job in workers.items():
        if job != None:
            work_remaining[job] -= 1

            if work_remaining[job] <= 0:
                # done, free the worker
                done += job
                remaining = [r for r in remaining if r != job]
                workers[worker] = None
                for step in dependancies:
                    dependancies[step] = [c for c in dependancies[step] if c != job]

    # print(work_remaining)
    # print(dependancies)

print(done)
print(time_elapsed)