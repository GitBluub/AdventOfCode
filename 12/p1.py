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

def h(curr, end):
    y, x = curr
    y2, x2 = end
    return abs(y2 - y) + abs(x2-x)

def a_star(start, end):
    openSet = {start}
    gScore = {}
    came_from = {}
    gScore[start] = 0
    fScore = {}
    fScore[start] = h(start, end)
    global m
    while len(openSet):
        minFscore = 999999999
        curr = None
        for x in openSet:
            if x in fScore and fScore[x] < minFscore:
                curr = x
                minFscore = fScore[x]
        openSet.remove(curr)
        y,x = curr
        if curr == end:
            print(curr)
            return gScore[curr]
        neighbors = [(y+1,x), (y-1,x), (y,x+1), (y,x-1)]
        for neighbor in neighbors:
            y2, x2 = neighbor
            if y2 < 0 or y2 >= len(m) or x2 < 0 or x2 >= len(m[0]):
                continue
            if  m[y2][x2] - m[y][x] < -1:
                continue
            tentaive_gScore = gScore[curr] + 1
            if neighbor not in gScore or tentaive_gScore < gScore[neighbor]:
                came_from[neighbor] = curr
                gScore[neighbor] = tentaive_gScore
                fScore[neighbor] = tentaive_gScore + h(neighbor, end)
                if neighbor not in openSet:
                    openSet.add(neighbor)
        print(openSet)
    print("a")

a, b = start
print(a_star(start, end))
