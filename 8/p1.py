with open('input') as f:
    read_data = f.read().splitlines()
f = [[] for i in range(len(read_data))]
for j, i in enumerate(read_data):
    for k in i:
        f[j] += [int(k)]
r = len(read_data) * 4 - 4
for i in range(1, len(read_data) - 1):
    for j in range(1, len(read_data) - 1):
        top = [read_data[x][j] for x in range(i)]
        down = [read_data[x][j] for x in range(i + 1, len(read_data))]
        left = [read_data[i][x] for x in range(j)]
        right = [read_data[i][x] for x in range(j + 1, len(read_data))]
        for k in [top, down, left, right]:
            if len(k) > 0 and max(k) < read_data[i][j]:
                r += 1
                break
print(r)
