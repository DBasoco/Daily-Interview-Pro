# Today we have: Room Scheduling
#
# You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be
# overlapping. Return the number of rooms that are required.
#
# For example: [(30, 75), (0, 50), (60, 150)] will return 2.


x = [(1, 3), (4, 8), (2, 5)]
print(x[2][0])
# just a test to re-familiarize myself with lists of tuples


def rooms_required(lectures):
    rooms = 1

    for i in range(0, len(lectures)):
        x, y = lectures[i][0], lectures[i][1]
        # tuples can't be altered but their entries act the same way as arrays

        for j in range(i, len(lectures)):
            if lectures[j][0] < x < lectures[j][1] or lectures[j][0] < y < lectures[j][1]:
                # if the start or end time of a lecture is in the space of another then we need another room
                rooms += 1
            else:
                pass
    return rooms

# not bad but it has a flaw with on having an issue with rooms over two intervals
# so I need to construct rooms that are lists and not just numbers


import numpy as np


def rooms_required(lectures):
    start, end = lectures[0][0], lectures[0][1]
    rooms = np.array([[start, end]])
    # done with just numbers but I need arrays/lists so I can manipulate the data freely

    for i in range(1, len(lectures)):
        x, y = lectures[i][0], lectures[i][1]
        print(x, y)

        for j in range(0, len(rooms)):
            if rooms[j][0] < x < rooms[j][1] or rooms[j][0] < y < rooms[j][1]:
                rooms += [x, y]
                # so if the start and end times overlap that lecture gets added to the rooms as a new list
            else:
                rooms[j] += [[x, y]]
                # if it doesn't overlap it is added to a preexisting room
    return len(rooms), rooms


print(rooms_required([(30, 75), (0, 50), (60, 150)]))

# This one was interesting. Having just graduated it is cool to see how the system helped to keep students from
# double booking their schedule.

