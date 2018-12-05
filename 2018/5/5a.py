#!/usr/bin/python3

import sys

string = open(sys.argv[1]).read()

reacted = True
newstring = ""
# print(string)

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

print(len(string)- 1)