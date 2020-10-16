# Today we have: Compare Version Numbers
#
# Version numbers are strings that are used to identify unique states of software products. A version number is in
# the format a.b.c.d and so on where a, b, etc. are numeric strings separated by dots. These generally represent a
# hierarchy from major to minor changes. Given two version numbers version1 and version2, conclude which is the
# latest version number. Your code should do the following.
#
# if version1 > version2 return 1
# if version1 < version2 return -1
# otherwise return 0
#
# Note that the numeric strings such as a, b, c, d, etc. may have leading zeroes, and that the version strings do not
# start or end with dots. Unspecified level revision numbers default to 0.

# I'm thinking split('.') and the int() function to change the data. Maybe have a secondary function for recursion.

class Solution:
    def compareVersion(self, version1, version2):
        x = version1.split('.')
        y = version2.split('.')
        # get rid of all the dots and make the string a list

        tally = 0
        # a marker for the final answer, we assume that they are the same version to start

        for t in range(0, max(len(x), len(y))):
            # we cycle over a number of times equal to the length of the longest list
            # this makes sure that each minor version update is considered as well

            try:
                one = int(x[t])

            except IndexError:
                one = 0

            try:
                two = int(y[t])

            except IndexError:
                two = 0
            # so we could have used logic statements but this is easier
            # here we take the str at index t, of the lists, then turn that string into an int
            # the problem is that they don't have to be the same length, to overcome this I used try suites to ignore
            # the index error and just make it a 0 as default from the problem

            if tally == 0:
                # nothing has changed with tally then we compare
                # this is because once one number in the list is different it doesn't matter what the tailing ones are
                # major updates come first and those are what we care more about

                if one > two:
                    tally += 1

                elif one < two:
                    tally += (-1)

                else:
                    pass
                # compares size of the numbers and changes tally appropriately or does nothing

            else:
                pass

        return tally


version1 = '1.0.1'
version2 = '1'

print(Solution().compareVersion(version1, version2))

# So instead of doing the recursion idea I had planned I switched over to the better try suite. It makes logic so
# much easier when you can just ignore mistakes and put in a default. This meant that I didn't have to worry about
# the list length I just needed to focus on the logic to change the tally value. Overall it was fun to find a simple
# function to compare a str type as an int type that had so many restrictions.
