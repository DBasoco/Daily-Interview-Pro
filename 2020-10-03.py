# Today we have: Subarray With Target Sum
#
# You are given an array of integers, and an integer K. Return the subarray which sums to K. You can assume that a
# solution will always exist.

# The subarray will be continuous so I can use the sums of the continuous arrays to find the solution.

def find_continuous_k(list, k):
    test = []
    return sum(test)

# so the sum of nothing is 0


def find_continuous_k(list, k):
    for i in range(0, len(list)):
        li = []
        for x in range(0, i):
            li += [list[x]]
        # so first we create a list for one subarray

        si = sum(li)
        # we then sum it

        for j in range(i, len(list)):
            lj = []
            for y in range(0, j + 1):
                lj += [list[y]]
            # now we make a sub array for every other possible array that can be continuously constructed from the list

            sj = sum(lj)
            # and sum that up to

            print('sj - si = %d' % (sj - si))

            if sj - si == k:
                # we check if the summed difference between these two arrays is k, if it is then we have our subarray

                print('\nThis is the one!\n%s and %s' % (lj, li))
                sub = []
                for k in range(i, j + 1):
                    sub += [list[k]]
                    # the solution subarray will be the array that only exists in the array lj and not in li

                return sub
            else:
                pass


print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))

# This was a good problem. I got to use more math to solve it which is always my favorite method. True it is cool to
# come up interesting construction methods for list and stored data but I really like it when the solution can be
# easily found using math. It really puts me into my bailiwick. I'm surprised I didn't end up using my whiteboard for
# this problem. I'm sure it could have sped things along but I think it is a good sign that my spatial thinking in
# the cyber space is improving.

