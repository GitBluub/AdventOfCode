with open('input') as f:
    read_data = f.read().splitlines()

def run_program(program):
    nb_line = 0
    executed = []
    acc = 0
    loop = False
    while nb_line < len(program):
        if nb_line in executed:
            loop = True
            break
        action, val = program[nb_line].split()
        executed += [nb_line]
        if action == "jmp":
            nb_line += int(val)
        else:
            if action == "acc":
                acc += int(val)
            nb_line += 1
    return acc, loop

possible_change = []
for nb_line, i in enumerate(read_data):
    action, val = i.split()
    if action == "jmp":
        possible_change += [ read_data[:nb_line] + ["nop " + val] + read_data[nb_line+1:]]
    
    if action == "nop":
        possible_change += [ read_data[:nb_line] + ["jmp " + val] + read_data[nb_line+1:]]

for j in possible_change:
    acc, loop = run_program(j)
    if not loop:
        print(acc)
        break