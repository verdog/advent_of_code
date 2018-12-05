#!/usr/bin/python3

import sys

orgstring = open(sys.argv[1]).read()

newstring = ""
# print(string)

shortest = 99999999999999999

for c in "abcdefghijklmnopqrstuvqxyz":
    string = orgstring.replace(c, '').replace(c.upper(), '').replace('\n', '')

    reacted = True
    while(reacted):
        i = 0
        newstring = ""
        reacted = False
        while(i < len(string)):
            letter = string[i]
            if (i < len(string) - 1):
                nextletter = string[i+1]
            else:
                nextletter = letter

            if (letter != nextletter and letter.lower() == nextletter.lower()):
                # combine; leave out of new string
                i += 2
                reacted = True
            else:
                newstring += letter
                i += 1

        # print(newstring)
        string = newstring

    if len(string) < shortest:
        # print(string)
        shortest = len(string)

print(shortest)