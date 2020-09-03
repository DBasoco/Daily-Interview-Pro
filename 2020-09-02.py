# Today we have: Running Median
#
# You are given a stream of numbers. Compute the median for each new element.
#
# Example: Given [2, 1, 4, 7, 2, 0, 5], the algorithm should output [2, 1.5, 2, 3.0, 2, 2.0, 2]

# Hmm so it was never stated but we need to order the list as we traverse it

# So for odd entry I use the order, for even I do the math

def running_median(stream):
    median = []
    # stores the answer from each operation

    order = []
    # stores an ordered list of ascending numbers for the median check

    for i in range(0, len(stream)):
        # since it is running we must go the length of the stream

        if i == 0:
            order = [stream[i]]
            median = [stream[i]]
            print(median)
            # the first entry is automatically in the median

        else:
            # there are two cases: first is when there are
            if i % 2 == 0:  # the ordered ones aka odd
                for j in range(0, len(order)):
                    if j == len(order) - 1:  # for getting to the end
                        order[-1] = stream[i]

                    elif order[j] < stream[i] < order[j + 1]:  # for comparing positions, when it fits we put it in
                        order[j + 1] = stream[i]

                    else:  # if it doesn't fit and we aren't at the end we move to the next position
                        pass
                median[i] = order[(len(order) / 2) - 0.5]

            else:  # the math ones aka even
                x = 0
                for k in order:
                    x += k
                    print(x)
                median += [x / 2]
                print(median)

    return print(median)


# Okay I see where I made my mistake, for the even case I still need to add to order. This means that the code for
# both cases is the same but how we construct the median from it is very different. This seems simple to grasp but in
# practice these small things slip your mind.

import math


def running_median(stream):
    median = []
    # stores the answer from each operation

    order = []
    # stores an ordered list of ascending numbers for the median check

    for i in range(0, len(stream)):
        # since it is running we must go the length of the stream

        if i == 0:
            order = [stream[i]]
            median = [stream[i]]
            # the first entry is automatically in the median

        else:
            # there are two cases: first is when there are
            if i % 2 == 0:  # the ordered ones aka odd

                for j in range(0, len(order)):
                    if j == len(order) - 1:  # for getting to the end
                        order[-1] = stream[i]

                    elif order[j] < stream[i] < order[j + 1]:  # for comparing positions, when it fits we put it in
                        order[j + 1] = stream[i]

                    else:  # if it doesn't fit and we aren't at the end we move to the next position
                        pass

                median[i] = [order[math.floor((len(order) / 2))]]

            else:  # the math ones aka even

                for j in range(0, len(order)):
                    if j == len(order) - 1:  # for getting to the end
                        order[-1] = stream[i]

                    elif order[j] < stream[i] < order[j + 1]:  # for comparing positions, when it fits we put it in
                        order[j + 1] = stream[i]

                    else:  # if it doesn't fit and we aren't at the end we move to the next position
                        pass
                x = 0
                for k in order:
                    x += k
                median += [x / 2]

    return print(median)


running_median([2, 1, 4, 7, 2, 0, 5])


# Some list index issues are coming up which means something wrong with the syntax and not the logic. 
