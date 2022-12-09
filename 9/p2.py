with open('input') as f:
    read_data = f.read().splitlines()

class Bob:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def followHead(self, head):
        tail = (self.y, self.x)
        y_diff = head[0] - self.y
        x_diff = head[1] - self.x
        if abs(x_diff) == 2 and y_diff == 0:
            tail = (tail[0], tail[1] + sign(x_diff))
        if abs(y_diff) == 2 and x_diff == 0:
            tail = (tail[0] + sign(y_diff), tail[1])
        if abs(x_diff) and abs(y_diff) and (abs(x_diff) + abs(y_diff) > 2):
            tail = (tail[0] + sign(y_diff), tail[1] + sign(x_diff))
        self.x = tail[1]
        self.y = tail[0]
    def __getitem__(self, key):
        if key == 0:
            return self.y
        if key == 1:
            return self.x
        raise Exception()
    def __str__(self) -> str:
        return f"{self.x} {self.y}"
    def __iter__(self):
        return (self.y, self.x).__iter__()

pos = []
tail = [Bob(0, 0) for i in range(9)]
head = Bob(0, 0)
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
        y_head, x_head = head
        y_mov, x_mov = dirs[dir]
        head = (y_head + y_mov, x_head + x_mov)
        for j in range(9):
            if j == 0:
                tail[0].followHead(head) 
            else:
                tail[j].followHead(tail[j-1])
        pos += [(tail[8].y, tail[8].x)]
print(len(list(set(pos))))
