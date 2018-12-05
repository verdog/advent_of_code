#!/usr/bin/python3

import sys
import re

days_to_date = {
    "01": 0,
    "02": 31,
    "03": 59,
    "04": 90,
    "05": 120,
    "06": 151,
    "07": 181,
    "08": 212,
    "09": 243,
    "10": 273,
    "11": 304,
    "12": 334
}

class Event:
    def __init__(self, day, minute, t):
        self.day = day
        self.minute = minute
        self.type = t
        self.id = -1

    def setID(self, ide):
        self.id = ide

events = []
lines = []
with open(sys.argv[1], "r") as f:
    for line in f:
        lines.append(line.strip())

for line in lines:
    if "wakes" in line:
        t = "wake"
    elif "falls" in line:
        t = "sleep"
    elif "begins" in line:
        t = "start"
    
    numbers = re.findall(r"\d+", line)
    day = days_to_date[numbers[1]] + int(numbers[2])

    minute = int(numbers[4])
    if int(numbers[3]) == 23:
        minute -= 60
        day += 1

    event = Event(day, minute, t)

    if t == "start":
        event.setID(int(numbers[5]))
    
    events.append(event)

events = sorted(events, key=lambda e: e.day * 1000 + e.minute)

total = dict()
schedule = dict()
currentID = -1
sleep_min = -1
wake_min = -1
for e in events:
    if e.type == "start":
        currentID = e.id
    elif e.type == "sleep":
        sleep_min = e.minute
    elif e.type == "wake":
        wake_min = e.minute

        if currentID in total:
            total[currentID] += wake_min-sleep_min
        else:
            total[currentID] = wake_min-sleep_min

        if currentID in schedule:
            for m in range(sleep_min, wake_min):
                schedule[currentID][m] += 1
        else:
            schedule[currentID] = dict()
            for m in range(-60, 60):
                schedule[currentID][m] = 0

max_sleep_id = -1
max_sleep = 0
for guard in total:
    if total[guard] > max_sleep:
        max_sleep = total[guard]
        max_sleep_id = guard

max_min = -1
max_min_id = -100
for i, minute in schedule[max_sleep_id].items():
    if minute > max_min:
        max_min = minute
        max_min_id = i

print(total[max_sleep_id])
print(schedule[max_sleep_id])

print(max_sleep_id)
print(max_min_id)
print(max_sleep_id * max_min_id)