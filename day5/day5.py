def is_fresh(id, ranges):
    for r in ranges:
        if id in range(*r):
            return True
    return False

def count_all_fresh(ranges):
    result = 0
    bounds = [i for r in ranges for i in r]
    bounds.sort()
    for i, bound in enumerate(bounds):
        next_bound = bounds[i+1] if i+1 < len(bounds) else None
        if next_bound and is_fresh(bound+1, ranges):
            result += next_bound - bound
        else:
            result += 1 if not next_bound or (next_bound != bound) else 0
    return result


def part_1(fp):
    ranges = []
    result = 0
    for line in open(fp):
        if "-" in line:
            ranges.append(tuple(int(x) for x in line.strip().split("-")))
        elif l:=line.strip():
            id = int(l)
            if is_fresh(id, ranges):
                result += 1
    return result

def part_2(fp):
    ranges = [tuple(int(x) for x in line.strip().split("-")) for line in open(fp) if "-" in line]
    return count_all_fresh(ranges)


if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))