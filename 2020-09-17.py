# Today we have: Decode String
#
# Given a string with a certain rule: k [string] should be expanded to string k times. So for example, 3 [abc] should
# be expanded to abcabcabc. Nested expansions can happen, so 2 [a2 [b] c] should be expanded to abbcabbc.

# This seems like a recursion to me for sure. So after going through on the whiteboard I see a place that might trip
# me up if I'm not careful with how I run through the string. I can't just use slice notation to slice the whole
# thing because that would ruin the structure of the term.

def decodeString(s):
    if int(s[0]):
        # if the entry is a number we know a bracket follows
        bra = 1
        # so we increase bracket count by 1

        num_multiply = int(s[0])
        # store how many times to copy what is inside the bracket

        while num_multiply != 0:
            for i in s[2:]:
                pass

    else:
        pass


# So I need to first identify printed copies of what is inside the bracket. Then go through that, if another number
# happens I then identify printed copies in bracket then go through that again.

def decodeString(s, final=''):
    for i in range(0, len(s)):
        if type(s[i]) == int:
            # so if the item in the string is an integer we do something

            enum = int(s[i])
            # set a number of times to enumerate the enclosed info

            while enum != 0:
                for j in range(i + 1, len(s) - 1):
                    # this accounts for brackets

                    final += s[j]
                    # add the value to the answer

                    new = final

                    decodeString(s[i + 1:len(s) - 1], new)
                    # run through the next set

                enum = enum - 1
                # remove one enumeration

        else:
            final += s[i]
            # the value is added to the answer
    return final


print(decodeString('2[a2[b]c]'))

# It would seem that all that whiteboard work and the time on keyboard meant nothing as this seems to just return the
# encoded string. This is very upsetting. I thought given the title I was going to be able to this problem for sure.
# Alas, I thought that my method would work. I knew what I had to do from breaking down the problem on the board but
# I couldn't execute it in the time.
