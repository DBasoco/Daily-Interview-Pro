# Today we have: Consecutive Ones
#
# Return the longest run of 1s for a given integer n's binary representation.
#
# Example:
# Input: 242
# Output: 4
#
# 242 in binary is 0b11110010, so the longest run of 1 is 4.

# So like the last one this has to do with base conversion but here we also have run through the result and find the
# greatest consecutive string of 1's. That's an interesting inclusion. So I know recursion is the answer.


#def dectobin(n):
#    if n > 1:
#        dectobin(n//2)
#
#    return n % 2


def longest_run(n):
    d = bin(n)
    # this is a function I was taught in school which does what the above attempts

    count = []
    x = 0
    # a list and marker

    #print(d)
    # see how the bin() function returns, this is important for indexing

    for i in range(0, len(d)):
        # over the length of d

        if d[i] == '1':
            x += 1
            # if it is one the marker goes up

            if x == len(d) - 2:
                count += [x]
                # for the case where the binary is all 1's
                # this escapes the function when the marker is equal to the length of the binary number
                # minus 2 because of 0b

        else:
            count += [x]
            x = 0
            # if anything else the marker is added to the count list and marker is reset

    #print(count)

    for j in range(0, len(count)):
        # now we need to go over the length of count to find the largest

        if j == 0:
            y = count[0]
            # establish base case

        else:
            y = max(y, count[j])
            # compare previous max to current index and return the larger value

    return y


print(longest_run(15))
