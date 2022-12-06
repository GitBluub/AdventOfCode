with open('input') as f:
    read_data = f.read().splitlines()

i = 25

read_data = [int(i) for i in read_data]
def pair_to_get_val(l, value):
    for i, val in enumerate(l):
        missing = value - val
        if missing in l[:i] + l[i+1:]:
            return True
    return False


target = 0
while i < len(read_data):
    preamble = read_data[i - 25: i]
    val = read_data[i]
    if not pair_to_get_val(preamble,val):
        target = val
        break
    i += 1

print(target)

def find_weakness(read_data):
    for i, val in enumerate(read_data):
        for j in range(i+1, len(read_data)):
            if sum(read_data[i:j]) == target:
                print(read_data[i:j])
                print(min(read_data[i:j]))
                print(max(read_data[i:j]))
                return min(read_data[i:j]) + max(read_data[i:j])
    return -1

print(find_weakness(read_data))