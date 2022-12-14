import sys
s = "input"
if len(sys.argv) > 1:
    s = sys.argv[1]
with open(s) as f:
    read_data = f.read().splitlines()
r = 0
rocks = [list(map(lambda x: list(map(int, x.split(","))), i.split("->"))) for i in read_data]
sandFall = 500
maxLeft = min([min(i, key=lambda x: x[0]) for i in rocks])[0]
maxDown = 0
for i in rocks:
    for j in i:
        maxDown = max(j[1], maxDown)
maxRight = max([max(i, key=lambda x: x[0]) for i in rocks])[0]
m = [["." for _ in range(maxRight * 10)] for _ in range(maxDown + 2)]
for i in rocks:
    for j in range(len(i) - 1):
        from_ = i[j]
        to = i[j+1]
        if from_[0] == to[0]:
            a, b = min(from_[1], to[1]), max(from_[1], to[1])
            for k in range(a, b+1):
                m[k][to[0]] = "#"
        else:
            a, b = min(from_[0], to[0]), max(from_[0], to[0])
            for k in range(a,b+1):
                m[to[1]][k] = "#"
while True:
    x, y = 500, 0
    r += 1
    while True:
        if y > maxDown:
            m[y][x] = "o"
            break
        if m[y+1][x] == ".":
            y += 1
        elif m[y+1][x-1] == ".":
            y += 1
            x -= 1
        elif m[y+1][x+1] == ".":
            y += 1
            x += 1
        else:
            m[y][x] = "o"
            if y == 0 and x == 500:
                print(r)
                exit()
            break
        
print(r)


