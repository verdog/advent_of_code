#!/usr/bin/python3

data = []
with open("input", "r") as f:
    data = f.read().split("\n")

twos = 0
threes = 0

for line in data:
    counts = dict()
    for letter in line:
        if letter in counts:
            counts[letter] += 1
        else:
            counts[letter] = 1

    for letter in counts:
        if counts[letter] == 2:
            twos += 1
            break;

    for letter in counts:
        if counts[letter] == 3:
            threes += 1
            break;

print(twos * threes)