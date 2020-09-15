# Today we have: Min Stack
#
# Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.
#
# push(x) -- Push element x onto stack
# pop() -- Removes the element on top of the stack
# top() -- Get the top element
# getMin() -- Retrieve the minimum element in the stack
#
# Note: be sure that pop() and top() handle being called on an empty stack.

# So this is a very involved problem, but it is very similar to what I have to do for my classes in my MPU project
# the only hang up is that I'm not fully sure what a stack is in this case nor how to construct one. It seems very
# similar to a binary tree but with only one vector direction.

# I decided to try a list method before I went to nested value method like in a binary tree

class minStack(object):
    def __init__(self):
        self.stack = []
        # use a similar structure in my MPU program to store cards in hand, library, field, etc

    def push(self, x):
        self.stack += [x]
        # adds the entry onto the stack of items in the last position so that everything is ordered correctly

    def pop(self):
        if not self.stack:
            pass
            # nothing in the stack so nothing happens

        else:
            x = []
            # new list

            for i in range(0, len(self.stack) - 1):
                x += [self.stack[i]]
                # populate the new list with every item of the old one except for the last entry, based on range

            self.stack = x
            # rewrite the stack to be the new list

    def top(self):
        if not self.stack:
            pass
            # nothing in the stack so nothing happens

        else:
            return self.stack[-1]
            # spit out the most recent entry to the list which is also the top of the stack

    def getMin(self):
        x = self.stack[0]
        # set the first comparison to the first entry

        for i in range(0, len(self.stack)):
            x = min(x, self.stack[i])
            # go up the list finding the smallest number

        return x


# That was a good first run but not everything was in constant time. getMin() and pop() are in linear time.
# I think I can do getMin() by using min() on all the values at once.

class minStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack += [x]

    def pop(self):
        if not self.stack:
            pass

        else:
            x = []

            for i in range(0, len(self.stack) - 1):
                x += [self.stack[i]]

            self.stack = x

    def top(self):
        if not self.stack:
            pass

        else:
            return self.stack[-1]

    def getMin(self):
        x = min(self.stack)
        # fixed that issue now I need to look at the pop()

        return x


# Not really sure what the play here is because I assume I can't just call the built in pop() function haha

class minStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack += [x]

    def pop(self):
        if not self.stack:
            pass

        else:
            x = self.stack[:-1]
            # now I just copy over the whole list except for the last entry and then just rewrite it

            self.stack = x

    def top(self):
        if not self.stack:
            pass

        else:
            return self.stack[-1]

    def getMin(self):
        x = min(self.stack)

        return x


x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
x.pop()
print(x.top())
print(x.getMin())

# Well I'm certain if slice notation is constant but regardless it is far cleaner and easier to understand. I
# actually really appreciated this problem. As I said earlier it parallels my own personal project, which funny
# enough has something called a stack as well. Now, because of this problem, I have a starting point to use for my
# own work.

