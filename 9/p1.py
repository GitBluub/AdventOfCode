with open('input') as f:
    read_data = f.read().splitlines()

pos = [(0, 0)]
tail = (0, 0)
head = (0, 0)
dirs = {
        "R": (0, 1),
        "L": (0, -1),
        "U": (1, 0),
        "D": (-1, 0),
        }
def sign(x):
    return (x > 0) - (x < 0)

for i in read_data:
    dir, times = i.split()
    for _ in range(int(times)):
        y_tail, x_tail = tail
        y_head, x_head = head
        y_mov, x_mov = dirs[dir]
        head = (y_head + y_mov, x_head + x_mov)
        y_diff = head[0] - y_tail
        x_diff = head[1] - x_tail
        if abs(x_diff) == 2 and y_diff == 0:
            tail = (tail[0], tail[1] + sign(x_diff))
        if abs(y_diff) == 2 and x_diff == 0:
            tail = (tail[0] + sign(y_diff), tail[1])
        if abs(x_diff) and abs(y_diff) and (abs(x_diff) + abs(y_diff) > 2):
            tail = (tail[0] + sign(y_diff), tail[1] + sign(x_diff))
        pos += [tail]
print(len(list(set(pos))))
