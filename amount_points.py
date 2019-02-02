games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']

def points(games):
    count = 0
    for x in games:
        count += 3 if int(x[0]) > int(x[2]) else abs(bool(int(x[2])-int(x[0]))-1)
    return count

print(points(games))