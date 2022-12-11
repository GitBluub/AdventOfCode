with open('input') as f:
    read_data = f.read().split("\n\n")
class Monkey:
    def __init__(self, items, operation, test, true, false):
        self.items = items
        self.op = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspected = 0
    def inspectAll(self, monkeys):
        for k in self.items:
            self.inspect(k, monkeys)
            #input()
        self.items = []
    def add(self, new):
        self.items += [new]
    def inspect(self, old, monkeys):
        print(f"\tmonkeys inspects an itme with a worry level of {old}")
        self.inspected += 1
        new = eval(self.op)

        print(f"\t\tnew worry level {new}")
        new = new // 3
        print(f"\t\tmonkey is bored, level is now {new}")
        print(f"\t\tis item divisible by {self.test}")
        if new % self.test == 0:
            print(f"\t\titem with worry level {new} is thrown to monkey {self.true}")
            monkeys[self.true].add(new)
        else:
            print(f"\t\titem with worry level {new} is thrown to monkey {self.false}")
            monkeys[self.false].add(new)

monkeys = []
for i in read_data:
    j = i.splitlines()
    _, st, op, test, true, false = j
    items = list(map(int, st.split(":")[1].replace(" ", "").split(",")))
    operation = op.split("=")[1]
    test = int(test.split()[-1])
    true = int(true.split()[-1])
    false = int(false.split()[-1])
    m = Monkey(items, operation, test, true, false)
    monkeys += [m]
for i in range(20):
    for m in monkeys:
        print("Monkey x:")
        m.inspectAll(monkeys)
    for j in range(len(monkeys)):
        print(f"monkeys {j}: {monkeys[j].items}")
a = [m.inspected for m in monkeys]
a.sort()
print(a[-1] * a[-2])
