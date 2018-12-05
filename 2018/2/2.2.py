#!/usr/bin/python3

data = []
with open("input", "r") as f:
    data = f.read().split("\n")
    data.remove("")

for line in data:
    for compline in data:
        diff = 0
        samestring = ""
        for i, char in enumerate(line):
            if char == compline[i]:
                samestring += char
            else:
                diff += 1
                if diff > 1:
                    break

        if diff == 1:
            print(samestring)
            exit()

