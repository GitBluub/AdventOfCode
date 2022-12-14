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
import functools
p = [eval(i) for i in read_data if i != ""]
p = sorted(p + [[[2]], [[6]]], key=functools.cmp_to_key(compare))
print((p.index([[2]]) + 1)*(p.index([[6]]) + 1))
