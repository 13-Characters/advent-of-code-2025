def part_1(fp):
    return sum(sum(i for i in range(r[0], r[1]) if str(i)[:len(str(i))//2] == str(i)[len(str(i))//2:]) for r in (tuple(int(x) for x in y.split("-")) for y in open(fp).read().strip().split(",")))
def part_2(fp):
    return sum(sum(i for i in range(r[0], r[1]) if any(len(str(i)) % j == 0 and i % sum([10**(j*k) for k in range(len(str(i)) // j)]) == 0 for j in range(1, len(str(i))))) for r in (tuple(int(x) for x in y.split("-")) for y in open(fp).read().strip().split(",")))
print(part_1("input"))
print(part_2("input"))