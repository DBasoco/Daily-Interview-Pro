# Today we have: Look and Say Sequence
# A look-and-say sequence is defined as the integer sequence beginning with a
# single digit in which the next term is obtained by describing the previous term. An example is easier to
# understand.

# 1, None
# 11, one 1's
# 21, two 1's
# 1211, one 2, and one 1
# 111221, one 1, 1 two, and two 1's

# Your task is, return the nth term of this sequence.

# Okay it makes way more sense after the example honestly. I was very confused for a second there.
# So integers have no length so I'll need to convert the sequence into a form I can traverse easily.


def look_and_say(sequence, n):
    seq = str(sequence)
    num = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    if len(seq) <= 1:  # so from the example I know what to do on len=1 but what about odd len?
        return num[0]
    elif n % 2 != 0:
        return num[int(seq[n - 1])]
    else:
        ans = seq[n - 1]
        if num[int(seq[n - 2])] == 'one':
            return ans
        else:
            return ans + "'s"


print(look_and_say(211231, 1))
print(look_and_say(211231, 2))
print(look_and_say(211231, 3))
print(look_and_say(211231, 4))
print(look_and_say(211231, 5))
print(look_and_say(211231, 6))

# added a few test cases to make sure it worked


# This is some code that I removed after I realized a better way to do it.
#     else:
#         even = []
#         odd = []
#         for i in seq:
#             if seq[i] % 2 == 0:     # defines the even entries
#                 # I don't actually need to return the full string I just need the nth entry
#                 even += seq[i]
#             else:
#                 odd += seq[i]
