# Today we have: String Compression
#
# Given an array of characters with repeats,, compress it in place. The length after compression should be less than
# or equal to the original array.
#
# Example:
# Input: ['a', 'a', 'b', 'c', 'c', 'c']
# Output: ['a', '2', 'b', 'c', '3']


# My first instinct is init on the first key and set a count to one then move till we hit something that isn't that
# key, all the while adding to the count. Then we add the key and the count to the compressed list, and init a new
# key with count 1. If the count stays at 1 then we just add the key to the list.


class Solution(object):
    def compress(self, chars):
        global key, count
        comp = []
        # create the compressed list and init the variables to be used

        for i in range(0, len(chars)):
            # over the range of the list

            if i == 0:
                key = chars[0]
                count = 1
                # init the first entry and how many times it shows up

            else:
                # if we are on any index besides 1

                if chars[i] == key:
                    count += 1
                    # if the new index matches our key we add one to the count and move on

                    if i == len(chars) - 1:
                        comp += [key]
                        comp += [str(count)]
                        # this is an escape statement for the end of the list to make sure all entries are present,
                        # that aren't of count 1

                else:
                    # if the char isn't a match

                    if count == 1:
                        comp += [key]

                        key = chars[i]
                        count = 1
                        # this is if the key only appeared once, since we only record the key and not the count in
                        # this case to save room
                        # it is assumed that any entry in the compressed list has at least one entry

                    else:
                        comp += [key]
                        comp += [str(count)]

                        key = chars[i]
                        count = 1
                        # if the the key appeared more than once we record the key and the count so we know how many
                        # keys of that kind to unpack
                if i == len(chars) - 1:
                    if count == 1:
                        comp += [key]
                        # escape statement for the end of the list to make sure that all entries are present,
                        # that are of count 1

        return comp


print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c', 'd']))

# It took me a little bit to realize that I needed an escape statement for the end but my experience in testing for
# bugs, that I've been gaining through these exercises, has helped me to know what kind of test will give me the
# information I need to find the error in my logic. My favorite part about this problem was that the answer did need
# you to add one escape statement but the second you only realize you need if you think about how your code would
# react to other inputs.

