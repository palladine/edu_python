# Define a function that generates medial values between two coordinates
# and returns them in an array from start to target.
# For example, if the starting point is [1,1] and the target point is [3,2]
# then the shortest route from start to target would be [[1,1], [2,2], [3,2]].
# The route should go only through integral coordinates.
#
# Note: you should move diagonally until the path from your current position
# to the target can be represented as a fully horizontal/vertical line.




def p(start, target):
    xs_ys = tuple(zip(start, target))

    xval = [x for x in range(min(xs_ys[0]), max(xs_ys[0])+1)]
    yval = [y for y in range(min(xs_ys[1]), max(xs_ys[1])+1)]

    print(xval)
    print(yval)

    return True

print(p((1,1),(3,2)))