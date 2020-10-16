# Today we have: Reverse a Directed Graph
#
# Given a directed graph, reverse the directed graph so all directed edges are reversed.
#
# Example:
# Input:
# A -> B, B -> C, A -> C
#
# Output:
# B -> A, C -> B, C -> A

# I understand the concept that I need to reverse how the nodes are connected to each other. The issue is that I'm
# not sure on the construction set in place for it.
#
# My hangup is that graph is already a dictionary so what purpose is there to have a separate dictionary of lists
# through defaultdict. I'll use it as a carrier of information then use it to rewrite the givens.
#
# From the print call I need to have the reverse_graph return something that has the ability to call the items()
# function. It seems like this is where defaultdict comes in. The documentation supports the items function. It just
# returns a list of the dictionary of lists.

from collections import defaultdict


class Node:
    def __init__(self, value):
        self.adjacent = []
        self.value = value


def reverse_graph(graph):
    d = defaultdict(list)
    for i in graph:
        d.setdefault(i, [])
    # makes the dictionary with the given keys

    print(d.items())

    return d


# making some progress but the given return is still vexing


def reverse_graph(graph):
    d = defaultdict(list)
    for i in graph:
        d.setdefault(i, graph[i].adjacent)
    # keeps the same dictionary build but now includes the nodes that it is adjacent to

    print('Node format: ', d)

    for j in d:
        print(j, 'j')
        for pos in range(0, len(j)):
            print(j[pos], 'pos')
            j = j[pos]

    print('String foramt: ', d)
    # I was trying to make the print out human readable before I piped it into a logic tree to make the new reversed
    # graph

    return d


a = Node('a')
b = Node('b')
c = Node('c')

a.adjacent += [b, c]
b.adjacent += [c]
# so by the transitive property we don't need to list that b is adjacent to a and we need no information to establish
# c's geometry

graph = {
    a.value: a,
    b.value: b,
    c.value: c
}

for _, val in reverse_graph(graph).items():
    print(val.adjacent)

# []
# ['a', 'b']
# ['a']

# Wow this was an uphill breakdown. I do enjoy the challenge of trying to understand now what something does but why
# it's needed at that time. Which this whole problem was! Trying to break down and understand a construction that I
# don't use frequently like defaultdict was an extra cherry on top. My next step after human readability would be to
# call the reverse function on a range of the graph/d. Then I'd add the values in but reverse.
