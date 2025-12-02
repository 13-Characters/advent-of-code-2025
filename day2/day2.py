def invalid_ids(lower, upper):
    result = []
    i_1 = (len(str(lower))+1) // 2
    i_2 = (len(str(lower))+1) // 2
    for i in range(i_1, i_2+1):
        result += [(10 ** i + 1) * x for x in range(10**(i-1), 10 ** i)
                   if lower <= (10 ** i + 1) * x <= upper]
    return result

def invalid_ids_2(lower, upper):
    result = []
    i_1 = (len(str(lower))+1) // 2
    i_2 = (len(str(lower)) + 1) // 2
    for i in range(i_1, i_2+1):
        result += [(10 ** i + 1) * x for x in range(10**(i-1), 10 ** i)
                   if lower <= (10 ** i + 1) * x <= upper]
    return result

def part_1(fp):
    result = 0
    ranges = open(fp).read(-1).strip()
    ranges = ranges.split(",")
    ranges = [tuple(int(x) for x in y.split("-")) for y in ranges]
    for range in ranges:
        lower = range[0]
        upper = range[1]
        result += sum(invalid_ids(lower, upper))
    return result

if __name__ == "__main__":
    print(part_1("input"))