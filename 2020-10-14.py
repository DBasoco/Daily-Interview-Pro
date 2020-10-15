# Today we have: Absolute Path
#
# Given a file path with folder names, '..'(Parent directory), and '.'(Current directory), return the shortest
# possible file path(Eliminate all the '..' and '.')
#
# Example:
# Input: '/Users/Joma/Documents/../Desktop/./../'
# Output: '/Users/Joma/'

# So I'm thinking I will use split('/')
# '..' means remove what came before and everything after
# '.' means remove this and everything after
# Basically what comes before or at that spot

def shortest_path(file_path):
    x = file_path.split('/')
    print(x)
    # remove the '/' and make the string into an iterable list

    for i in range(0, len(x)):
        if x[i] == '..':
            # for parent

            for j in range(i - 1, len(x)):
                x[j] = ''
                print(x, '..')
            # starting at the index prior or the parent, redact everything that follows

        elif x[i] == '.':
            # for current

            for j in range(i, len(x)):
                x[j] = ''
                print(x, '.')
            # starting at the index or current, redact everything that follows

        else:
            pass

    return x


# now if I need to add the info that wasn't redacted into a file format and print it


def shortest_path(file_path):
    x = file_path.split('/')

    for i in range(0, len(x)):
        if x[i] == '..':
            for j in range(i - 1, len(x)):
                x[j] = ''

        elif x[i] == '.':
            for j in range(i, len(x)):
                x[j] = ''

        else:
            pass

    path = '/'
    # make a new string

    for j in range(0, len(x)):
        if x[j] == '':
            pass
        # if it's redacted

        else:
            path = path + x[j] + '/'
        # add it to the string with the correct syntax

    return path


print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))

# Well this was a good test of manipulating data and breaking down an unknown operation scheme. 
