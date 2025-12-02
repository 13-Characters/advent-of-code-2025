def invalid_ids(lower, upper):
    result = []
    # Find the lowest invalid id within the range
    j = str(lower)
    if len(j) % 2 == 0:
        j = j[:(len(j))//2] # Cut lower in half
        i_1, j = len(j), int(j)
    else:
        i_1, j = (len(j) + 1)//2, 10**((len(j) + 1)//2 - 1)
    lowest_invalid_id = (10**i_1 + 1) * j
    if lowest_invalid_id < lower:
        j += 1
        lowest_invalid_id = (10 ** i_1 + 1) * j
    if lowest_invalid_id > upper:
        return
    j = str(upper)
    if len(j) % 2 == 0:
        j = j[:len(j) // 2]  # Cut upper in half
        i_2, j = len(j), int(j)
    else:
    highest_invalid_id = (10 ** i_2 + 1) * j
    if highest_invalid_id > upper:
        j -= 1
        highest_invalid_id = (10 ** i_2 + 1) * j

    for i in range(max(i_1, 1), i_2 + 1):
        result += [(10 ** i + 1) * x for x in range(10**(i-1), 10 ** i)
                   if lowest_invalid_id <= (10 ** i + 1) * x <= highest_invalid_id]
    print(result, lowest_invalid_id, highest_invalid_id)
    return result

def part_1(fp):
    result = 0
    ranges = open(fp).read(-1).strip()
    ranges = ranges.split(",")
    ranges = [tuple(int(x) for x in y.split("-")) for y in ranges]
    print(ranges)
    for range in ranges:
        lower = range[0]
        upper = range[1]
        result += sum(invalid_ids(lower, upper))
    return result

if __name__ == "__main__":
    print(part_1("example_input"))