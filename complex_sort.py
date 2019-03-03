# I
L = [('hi', 2), ('what', 1), ('is', 3), ('your', 1), ('name', 3),
     ('my', 2), ('bond', 2), ('james', 1), ('damme', 4), ('van', 3),
     ('claude', 2), ('jean', 1)]
s = sorted(L, key=lambda x: x[0])
L = sorted(s, key=lambda x: x[1], reverse=True)


# II
li = [('fink', 3), ('flip', 3), ('flock', 4), ('foo', 12), 
      ('foot', 20), ('football', 20), ('futz', 10), ('flip', 3), 
      ('flank', 3), ('flop', 3)]
sorted_li = sorted(li, key=lambda x: (-x[1], x[0]))
