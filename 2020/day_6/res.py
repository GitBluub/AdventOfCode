with open('input') as f:
    read_data = f.read().splitlines()


L = []
l = []
for i in read_data:
    if i == "":
        L += [l]
        l = []
    else:
        l += [i]

L += [l]

total = 0
for j in L:
    '''
    answers = []
    answer for part 1
    for k in j:
        for c in k:
            if c not in answers:
                answers += [c]
                '''
    result = set()
    start = True
    for k in j:
        v = set(k)
        if not len(result) and start:
            result = v
            start = False
        else:
            result = result & v
    total += len(result)
print(total)