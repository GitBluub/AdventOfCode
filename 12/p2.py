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
def a_star(start, end):
    openSet = {start}
    gScore = {}
    came_from = {}
    gScore[start] = 0
    fScore = {}
    fScore[start] = 0
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
        if m[y][x] == 97:
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
                fScore[neighbor] = tentaive_gScore
                if neighbor not in openSet:
                    openSet.add(neighbor)
        #print(openSet)
    print("failure")

a, b = start
print(a_star(start, end))
