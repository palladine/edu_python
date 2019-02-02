s = "12:15"

L = s.split(':')
if 18 < int(L[0]) < 6:
    print("I don't see the sun!")
else:
    aph = 90/6
    apm = aph/60
    print((((int(L[0]))-6)*aph)+apm*int(L[1]))