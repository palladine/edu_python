def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    L = []
    c = 0
    if len(line) > 0:
        sym = line[0]
        sub = line[0]
        for x in line[1:]:
            if x == sym:
                sub += x
                sym = x
                L.append(sub)
            else:
                L.append(sub)
                sub = x
                sym = x
    for z in L:
        if c < len(z):
            c = len(z)
    return c
