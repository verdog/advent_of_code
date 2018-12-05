#!/usr/bin/python3

import sys

orgstring = open(sys.argv[1]).read()
shortest = None

for c in "abcdefghijklmnopqrstuvqxyz":
    # string = orgstring.replace(c, '').replace(c.upper(), '').replace('\n', '')
    string = orgstring.replace(c+c.upper()+"\n", '')

    i = 0
    while (i < len(string) - 1):
        letter = string[i]
        nextletter = string[i+1]

        if (letter != nextletter and letter.lower() == nextletter.lower()):
            # match and react
            string = string[:i] + string[min(i+2, len(string)):]
            i = max(0, i-1)
        else:
            # no match, move on
            i += 1

    if (shortest is None or len(string) < shortest):
        shortest = len(string)

print(shortest)