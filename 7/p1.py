class Tree:
    def __init__(self, name, isDirectory, size, parent):
        self.children = []
        self.isDirectory = isDirectory
        self.data = size
        self.name = name
        self.parent = parent
    def getSize(self):
        if self.isDirectory:
            return sum([x.getSize() for x in self.children])
        else:
            return self.data
    def __str__(self) -> str:
        return f"{self.name} {self.isDirectory} {self.data} {len(self.children)}"

with open('input') as f:
    read_data = f.read().splitlines()


root = Tree("/", True, 0, None)
curr = root
i = 0
while i < len(read_data):
    if read_data[i][0] == "$":
        cmd = read_data[i].split()[1]
        if cmd == "cd":
            _, cmd, target = read_data[i].split()
            if target == "/":
                curr = root
            elif target == "..":
                curr = curr.parent if curr.parent else root
            else:
                curr = next((x for x in curr.children if x.name == target), root)
            i += 1
        if cmd == "ls":
            i += 1
            while i < len(read_data) and not read_data[i].startswith("$") :
                n, name = read_data[i].split()
                if n == "dir":
                    new = Tree(name, True, 0, curr)
                else:
                    new = Tree(name, False, int(n), curr)
                curr.children += [new]
                i += 1
    else:
        i += 1


c = root
r = 0
def a(t):
    global r
    size = t.getSize()
    if size <= 100000 and t.isDirectory:
        r += size
    for i in t.children:
        a(i)
a(root)
print(r)
