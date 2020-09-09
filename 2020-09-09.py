# Today we have: Angles of a Clock
#
# Given a time in the format of hour and minute, calculate the angle of the hour and minute hand on a clock.

# First thoughts are: radians or degrees, start from hour or minute hand, determine angle based on standard cartesian
# rotation going counterclockwise or the other way
# So right off the bat without the example I am left to decide for myself what they want.


# print(calcAngle(3, 30)) # the sample says this is suppose to produce 75, wrong: 90 correct
# print(calcAngle(12, 30)) # the sample says this is suppose to produce 165, wrong: 180 correct
# This means two things: they want the answer in degrees, and they are bad at maths
# That should 180 as they are anti-parallel to one another. Which is always 180.


def calcAngle(h, m):
    minute = m * 6
    # each minute has degrees equal to 6 degrees

    if h % 12 == 0:
        hour = (30 + (m * 0.5))
        # if it is 12 then I need to only include the displacement of the minute hand
    else:
        hour = (h * 30) + (m * 0.5)
    # each hour has degrees equal to 30 plus half a degree for each minute that passes

    # note that all angles are based on position to 12 and grow clockwise
    if hour > minute:
        return hour - minute
    else:
        return minute - hour


print(calcAngle(3, 30))
print(calcAngle(12, 30))


# Okay so at first I made a few mistakes but luckily when I ran through it on my whiteboard I was able to see,
# physically, that I had made a mistake. So even though I thought I was right it was good to run through a diagram
# just how I use to do for physics problems. Seeing the diagram helps to understand how the system works. Honestly,
# I really enjoyed this one since I got to make a mistake and learn from it, and learn from it using something that I
# am familiar with and can use more of in the future.

# Possible changes to the code would be done in the second if statement to determine directionality of the angle.
