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
total_children = []
values = []
end_value = 0
i = 0
while i < len(numbers):
    num = numbers[i]
    # print(current_type)

    if current_type == "children":
        current_type = "num_metadata"
        num_children.append(num)
        total_children.append(num)
        values.append([])
        i += 1
    elif current_type == "num_metadata":
        metadata.append([])
        if num_children[-1] == 0:
            current_type = "metadata"
        else:
            current_type = "children"
        num_metadata.append(num)
        i += 1
    elif current_type == "metadata":
        num_metadata[-1] -= 1

        metadata[-1].append(num)

        i += 1

        if num_metadata[-1] != 0:
            current_type = "metadata"
        else:
            num_children[-1] -= 1
            if (num_children[-1] < 0):

                if (len(values) > 1):
                    if (total_children[-1] == 0):
                        values[-2].append(sum(metadata[-1]))
                        curvalue = 0
                    else:
                        addval = 0
                        for data in metadata[-1]:
                            if data in range(1, total_children[-1] + 1):
                                addval += values[-1][data-1]
                        values[-2].append(addval)
                else:
                    # final collapse
                    addval = 0
                    for data in metadata[-1]:
                        if data in range(1, total_children[-1] + 1):
                            addval += values[-1][data-1]
                    end_value = addval
                    break

                metadata.pop()
                num_children.pop()
                num_metadata.pop()
                total_children.pop()
                values.pop()

                if (len(num_children) == 0):
                    break
                else:
                    num_children[-1] -= 1
                    if (num_children[-1] > 0):
                        current_type = "children"
                    else:
                        current_type = "metadata"

    # print(num_children)
    # print(total_children)
    # print(num_metadata)
    # print(values)
    # print(metadata)

print(end_value)