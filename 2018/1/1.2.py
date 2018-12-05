#!/usr/bin/python3

seen = dict()

seen[0] = True

freq = 0
done = False
while not done:
    with open("input", "r") as f:
        for line in f:
            freq += int(line)

            if freq in seen and seen[freq] == True:
                done = True
                break
            else:
                seen[freq] = True

print(freq)