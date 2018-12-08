#!/usr/bin/python3

import sys

numbers = []
with open(sys.argv[1], "r") as f:
    numbers = [int(i) for i in f.readline().split()]
# print(numbers) 

current_type = "children"
metadata = []
num_metadata = []
num_children = []
i = 0
while i < len(numbers):
    num = numbers[i]
    # print(current_type)

    if current_type == "children":
        current_type = "num_metadata"
        num_children.append(num)
        i += 1
    elif current_type == "num_metadata":
        if num_children[-1] == 0:
            current_type = "metadata"
        else:
            current_type = "children"
        num_metadata.append(num)
        i += 1
    elif current_type == "metadata":
        metadata.append(num)
        num_metadata[-1] -= 1
        i += 1

        if num_metadata[-1] != 0:
            current_type = "metadata"
        else:
            num_children[-1] -= 1
            if (num_children[-1] < 0):
                num_children.pop()
                num_metadata.pop()
                if (len(num_children) == 0):
                    break
                else:
                    num_children[-1] -= 1
                    if (num_children[-1] > 0):
                        current_type = "children"
                    else:
                        current_type = "metadata"

    # print(num_children)
    # print(num_metadata)
    # print(metadata)

print(sum(metadata))