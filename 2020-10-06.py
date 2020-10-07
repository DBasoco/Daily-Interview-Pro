# Today we have: shifted String
#
# You are given two strings, A and B. Return whether A can be shifted some number of times to get B.
#
# Eg. A = abcde, B = cdeab should return true because A can be shifted 3 times to the right to get B. A = abc and B =
# acb should return false.

def is_shifted(a, b):
    if len(a) is not len(b):
        return False
        # if the strings are different lengths than there is no way to shift them such that they are equal

    else:
        A = []
        B = []
        # it is easier to move objects around in lists than in strings

        for x in a:
            A += [x]
        for y in b:
            B += [y]
            # occupy the lists with the values from the strings

        for i in range(0, len(a)):
            # cycle for the length of the strings

            A += [A.pop(0)]
            # take the value at index 0, remove it, then add it to the end of the list

            if A == B:
                return True
                # true if equal

        return False
        # false if for the whole cycle the values never matched


print(is_shifted('abcde', 'cdeab'))

# So this problem was a real breeze and the solution is even in linear time and space. This might be one of the best
# solutions I've come up. Especially because the time to completion was so fast. These practise problems are really
# starting to pay dividends. I look forward to the next challenge to learn a new approach or computer concept.
