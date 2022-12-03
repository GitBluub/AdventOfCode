with open('input') as f:
    read_data = f.read().splitlines()

L = {}

for i in read_data:
    i = i.replace('.', '')
    i = i.replace('bags', '')
    i = i.replace('bag', '')
    l, r = i.split(" contain ")
    bag_name = " ".join(l.split())
    bags = r.split(', ')
    L[bag_name] = bags

def detect_number_bag(L: dict, root: str, target: str = None) -> int:
    count = 0
    bags = L[root]
    if isinstance(bags, int):
        return bags
    
    if root == target:
        for bag in bags:
            print(bag)
    elif bags[0] != "no other ":
        for bag in bags:
            v = bag.split()
            num = v[0]
            clr = " ".join(v[1:])
            if clr == target:
                count += int(num)
                continue
            count += int(num) * detect_number_bag(L, clr, target)
    if target is None:
        count += 1
    L[root] = count
    return count

print(detect_number_bag(L, "shiny gold") - 1)