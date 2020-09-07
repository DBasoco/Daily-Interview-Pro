# Today we have: Given Two Arrays, Write a Function to Compute Their Intersection
#
# Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in
# both arrays.
#
# Example:
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]
#
# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]

# The good part about this is that they don't ask that the intersection be ordered in a unique way. The fastest way
# would be to first identify which list is shortest, then traverse that. This works because intersection requires
# that the value be in both lists so we need only check one.

class Solution:
    def intersection(self, nums1, nums2):
        inter = []
        if len(nums1) <= len(nums2):
            # so this finds the shortest list, or if they are the same I'll just use the first as the set

            for i in nums1:
                # traverse each value
                try:
                    if nums2.index(i):
                        inter += [i]
                        print(nums2, i)
                        # if the value in 1 has an index in 2 then add that to the intersection

                    else:
                        pass
                except ValueError:
                    print(i)

            return inter

        else:
            # so this is if the second list is longer

            for i in nums2:
                try:
                    if nums1.index(i):
                        inter += [i]
                        nums1.remove(i)
                except ValueError:
                    pass
            return inter


# So for some reason this was just returning 4 and just ignoring the 9. I can't seem to figure out why.

class Solution:
    def intersection(self, nums1, nums2):
        inter = []
        if len(nums1) <= len(nums2):
            # so this finds the shortest list, or if they are the same I'll just use the first as the set

            for i in nums1:
                # traverse each value
                try:
                    if nums2.index(i):
                        inter += [i]
                        print(nums2, i)
                        # if the value has an index number in 2 then add it to intersection

                except ValueError:
                    # if is doesn't it will return an error so we can just move past this
                    print(i)

            return inter
            # This is in the right place and when I move the 4 around and when I print i on except it return 5 but
            # not 9. I actually have no idea why.

        else:
            # so this is if the second list is longer

            for i in nums2:
                try:
                    if nums1.index(i):
                        inter += [i]
                        nums1.remove(i)
                except ValueError:
                    pass
            return inter


print(Solution().intersection([4, 7, 5], [9, 4, 9, 7, 4]))


# Alright so my logic and use of try/except methodology is good in this problem. I have do some ways to test where
# the flaw is in yuor code but I didn't find why 9 was having such an issue. I mean 7 works and the problem isn't a
# repeat value like with 4.

# I have one last idea before I time runs out.

class Solution:
    def intersection(self, nums1, nums2):
        inter = []
        if len(nums1) <= len(nums2):
            # so this finds the shortest list, or if they are the same I'll just use the first as the set

            for i in nums1:
                # traverse each value
                try:
                    if nums2.index(i):
                        inter += [i]
                        print(nums2, i)
                        # if the value has an index number in 2 then add it to intersection

                except ValueError:
                    # if is doesn't it will return an error so we can just move past this
                    print(i)

            return inter
            # This is in the right place and when I move the 4 around and when I print i on except it return 5 but
            # not 9. I actually have no idea why.

        else:
            # so this is if the second list is longer

            for i in nums2:
                try:
                    if nums1.index(i) >= 0:
                        inter += [i]
                        nums1.remove(i)
                except ValueError:
                    pass
            return inter


print(Solution().intersection([4, 9, 5], [9, 4, 9, 7, 4]))

# Nope the greater than or equal to sign did nothing to fix the problem. Well that was my last attempt.
