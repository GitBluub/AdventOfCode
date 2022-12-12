import sys
sys.setrecursionlimit(3000)
with open('input') as f:
    read_data = f.read().splitlines()
m = [list(map(ord, [x for x in i])) for i in read_data]
start = (0, 0)
end = (0, 0)
for y in range(len(m)):
    for x in range(len(m[y])):
        if m[y][x] == 83:
            end = (y, x)
            m[y][x] = 97
        if m[y][x] == 69:
            start = (y, x)
            m[y][x] = 122
evaluated = {}
def path(y, x, done):
    global m
    global end
    global evaluated
    minSteps = 99999999
    #print(y,x)
    #if evaluated.get(f"{y} {x}"):
    #    return evaluated[f"{y} {x}"]
    if (y, x) == end:
    #    print("wow")
        return 0
    #k = [["." for _ in range(len(m[0]))] for _ in range(len(m))]
    #for a,b in done:
    #    k[a][b] = "x"
    #for a in k:
    #    print("".join(a))
    #input()

    # top
    if y >= 1 and m[y - 1][x] - m[y][x] >= -1 and   m[y - 1][x] - m[y][x] <= 0 and not (y-1,x) in done:
        minSteps = min(minSteps, path(y-1, x, done + [(y, x)]))
   # left
    if x >= 1 and m[y][x-1] - m[y][x] >= -1 and   m[y][x-1] - m[y][x] <= 0 and not (y,x-1) in done:
        minSteps = min(minSteps, path(y, x-1, done + [(y, x)]))
    # down
    if y < len(m)- 1 and m[y + 1][x] - m[y][x] >= -1 and   m[y + 1][x] - m[y][x] <= 0 and not (y+1,x) in done:
        minSteps = min(minSteps, path(y+1, x, done + [(y, x)]))
 
    # right
    if x < len(m[0]) - 1 and  m[y][x+1] - m[y][x] >= -1 and   m[y][x+1] - m[y][x] <= 0 and not (y,x+1) in done:
        minSteps = min(minSteps, path(y, x + 1, done + [(y, x)]))         
    #evaluated[f"{y} {x}"] = minSteps + 1
    return minSteps + 1
a, b = start
print(path(a, b, [(a,b)]))
