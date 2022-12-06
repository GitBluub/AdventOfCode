with open('input') as f:
    read_data = f.read().splitlines()

whole_list = []
L=[]
for i in read_data:
    if i != '':
        L += [i]
    else:
        whole_list += [' '.join(L)]
        L = []

whole_list += [' '.join(L)]

def is_valid_passport(passport):
    for k in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if k not in passport.keys():
            return 0
    return 1

def is_valid_number_between(nb, min_range, max_range):
    if int(nb) <= max_range and int(nb) >= min_range:
        return 1
    return 0

def is_valid_height(hgt):
    nb = ''
    unit = ''
    for i in hgt:
        if i.isdigit():
            nb += i
        else:
            unit += i
    if unit == 'in' and int(nb) <= 76 and int(nb) >= 59:
        return 1
    if unit == 'cm' and int(nb) <= 193 and int(nb) >= 150:
        return 1
    return 0

def is_valid_hair_color(hair_color):
    if hair_color[0] == '#' and len(hair_color) == 7:
        for i in hair_color[1:]:
            if i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                return 0
        return 1
    return 0

def is_valid_eye_color(eye_color):
    if eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return 1
    return 0

def is_valid_pid(pid):
    if len(pid) == 9:
        for i in pid:
            if not i.isdigit():
                return 0
        return 1
    return 0


def is_valid_passport_2(passport):
    res = not is_valid_number_between(passport['byr'], 1920, 2002)
    res += not is_valid_number_between(passport['iyr'], 2010, 2020)
    res += not is_valid_number_between(passport['eyr'], 2020, 2030)
    res += not is_valid_height(passport['hgt'])
    res += not is_valid_hair_color(passport['hcl'])
    res += not is_valid_eye_color(passport['ecl'])
    res += not is_valid_pid(passport['pid'])
    if res >= 1:
        return 0
    return 1

    

res = 0
for i in whole_list:
    add = 1
    categories = i.split()
    passport = {}
    for j in categories:
        key, value = j.split(':')
        passport[key] = value
    if is_valid_passport(passport):
        add = is_valid_passport_2(passport)
    else:
        add = 0
    res += add

print(res)