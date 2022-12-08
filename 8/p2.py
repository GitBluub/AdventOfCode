with open('input') as f:
    read_data = f.read().splitlines()
f = [[] for i in range(len(read_data))]
for j, i in enumerate(read_data):
    for k in i:
        f[j] += [int(k)]
r = 0
for i in range(0, len(read_data)):
    for j in range(0, len(read_data)):
        top = [read_data[x][j] for x in range(i)]
        top.reverse()
        down = [read_data[x][j] for x in range(i + 1, len(read_data))]
        left = [read_data[i][x] for x in range(j)]
        left.reverse()
        right = [read_data[i][x] for x in range(j + 1, len(read_data))]
        score = 1
        for k in [top, down, left, right]:
            a = 0
            for l in k:
                a += 1
                if int(l) >= int(read_data[i][j]):
                    break
            score *= a
        r = max(r, score)
print(r)
