# Today we have: Distribute Bonuses
#
# You are the manager of a number of employees who all sit in a row. The CEO would like to give bonuses to all of
# your employees, but since the company did not perform so well this year the CEO would like to keep the bonuses to a
# minimum.
#
# The rules of giving bonuses is that: - Each employee begins with a bonus factor of 1x. - For each employee,
# if they perform better than the person sitting next to them, the employee is given a +1 higher bonus (and up to +2
# if they better than both people to their sides).
#
# Given a list of employee's performance, find the bonuses each employee should get.
#
# Example:
# Input: [1, 2, 3, 2, 3, 5, 1]
# Output: [1, 2, 3, 1, 2, 3, 1]

# So this is a very real world applicable problem. Many companies do similar things to this so the chance to break
# down how to do is great. It doesn't at first seem like recursive problem as the numbers are only in comparison to
# those immediately around you.

import numpy as np
# this will be super helpful in making the initial bonus list


def getBonuses(performance):
    bonus = np.ones(len(performance), dtype=int)
    for i in range(0, len(performance)):
        if i == len(performance) - 1:
            pass
            # when we get to the last entry we do nothing
        else:
            # we did nothing because we compare each number to the one that follows it and make additions this way so
            # we don't go over the +2 max
            if performance[i] > performance[i + 1]:
                bonus[i] += 1
                # if first number is bigger it grows

            else:
                bonus[i + 1] += 1
                # if second number is bigger it grows

    return bonus


print(getBonuses([1, 2, 3, 2, 3, 5, 1]))

# This wasn't too crazy but it was interesting to work out. Even if I were limited to not be able to use numpy I
# still need only make a list of ones. It wouldn't cause too much of drawback.
