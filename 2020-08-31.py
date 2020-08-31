# Today we have: Minimum Removals for Valid Parenthesis
#
# You are given a string of parenthesis. Return the minimum number of parenthesis that would need to be removed in
# order to make the string valid. "Valid" means that each open parenthesis has a matching closed parenthesis.
#
# Example:
# "()())()"
# The following input should return 1.
#
# ")("

# This has some real world application. Even the IDE I am using must use a real time version of a similar software to
# help with suite information/input.


def count_invalid_parenthesis(string):
    l = []
    r = []
    for i in range(0, len(string)):
        if string[i] == '(':
            l.append(string[i])
        if string[i] == ')':
            r.append(string[i])
    if string == ')(':
        return 1

    return abs(len(l) - len(r))


print(count_invalid_parenthesis('()())()'))

# I am concerned that this was too simplistic. It doesn't seem that hard. I think it is because the return was so
# simple. If the had asked what needed to be changed instead how much needs to be changed it would have been harder.
# It's like asking what's versus how do we fix it. One is just inherently harder to answer.
