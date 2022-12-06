with open('input') as f:
    read_data = f.read().splitlines()

nb_rows = 8
nb_col = 9
crates = read_data[:nb_rows]
r = [[] for i in range(nb_col)]
for i in range(nb_col):
  for j in range(nb_rows):
    l = crates[j][i * 4 + 1]
    if l != " ": r[i] += [l]
instr = read_data[nb_rows + 2:]
for i in instr:
    a = i.replace("move", "").replace("from", "").replace("to", "")
    n, src, dest = map(int, a.split())
    #print(n, src, dest)
    r[dest - 1] = r[src - 1][:n][::-1] + r[dest - 1]
    r[src - 1] = r[src - 1][n:]
    #print(r)
print("".join([i[0] for i in r]))
