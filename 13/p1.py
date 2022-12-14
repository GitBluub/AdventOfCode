import sys
s = "input"
if len(sys.argv) > 1:
    s = sys.argv[1]
with open(s) as f:
    read_data = f.read().splitlines()
index = 1
r = 0

def compare(left, right):
    if left == []: return 0 if right == [] else -1
    if right == []: return 1
    if isinstance(left, list) and isinstance(right, list):
        cmp = compare(left[0], right[0])
        if cmp == 0:
            return compare(left[1:], right[1:])
        return cmp
    if isinstance(left, list):
        return compare(left, [right])
    if isinstance(right, list):
        return compare([left], right)
    return -1 if left < right else 1 if right < left else 0
for i in range(0, len(read_data), 3):
    left = eval(read_data[i])
    right = eval(read_data[i+1])
    if compare(left, right) <= 0:
        #print(index)
        r += index
    index += 1
print(r)
