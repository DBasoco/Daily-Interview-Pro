# Today we have: No Adjacent Repeating
#
# Given a string, rearrange the string so that no character next to each other are the same. If no such arrangement
# is possible, then return None.
#
# Example:
# Input: abbccc
# Output: cbcbca

# This seems to have me stumped... The problem I am thinking is that there are multiple ways to construct a list that
# meets these criteria and to have to find every single one could take far too long. The easiest way to go about this
# is by making the mode number the first number and going from there.

# Take the example: we could go with cbacbc instead of the one that was given as the output. It just seems too open
# ended. So will just have to pick a strategy and stick to it.

# Assume that the given string will be ordered s.t. similar char's are next to each other.

def rearrangeString(s):
    ref = {i: 0 for i in s}
    for i in s:
        ref[i] += 1
    # create a dictionary, in linear time, of all the entries in the string, then count them in linear time to assign
    # a reference value

    new = ''
    # make a new string to return so we don't destroy the original

    for i in range(0, len(s)):
        # we only need to do this process a number of times equal to the length of the string s

        new = ''.join(max(ref, key=ref.get))
        # add the key from the reference that has the largest value

        print('test, %s' % new)
        # was just getting c returned

    return new


# So I can now pull the biggest number next I need to add logic to reduce the number of each in the dictionary and
# make sure that there isn't a char next to itself.

def rearrangeString(s):
    ref = {i: 0 for i in s}
    for i in s:
        ref[i] += 1

    new = ''

    for i in range(0, len(s)):
        x = max(ref, key=ref.get)
        new += x
        # the key with the max is now a variable and the string cat is simpler

        ref[x] += -1
        # when a key is used the value of that key is reduced by one

        print('test, %s' % new)
        # returned correct but couldn't handle the None escapement

    return new


# Now some refinement to include the None requirement


def rearrangeString(s):
    ref = {i: 0 for i in s}
    for i in s:
        ref[i] += 1

    new = ''

    for i in range(0, len(s)):
        x = max(ref, key=ref.get)
        if i == 0:
            new += x
            ref[x] += -1
            # init the first value to avoid index length errors

        else:
            if x != new[i - 1]:
                new += x
                ref[x] += -1
                # if the value is different than the one before it then we add

            else:
                return None
            # if it's different than this particular construction method has no chance of success so the response is
            # None

    return new


print(rearrangeString('abbccc'))

# This had me using dictionaries in a way I have never done before so it was really exciting to learn this new tool I
# can use in python. Given how using dictionaries in this way uses constant memory and linear time,
# I may be incorporating them in more code that I write. This was the exact type of problem I needed at this stage in
# my coding career.
