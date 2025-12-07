def parse(fp):
    lines = open(fp).readlines()
    splitters = [[i for i in range(len(l)) if l[i] == "^"] for l in lines]
    splitters = list(filter(bool, splitters))
    start = lines[0].find("S")
    return start, splitters
def split(beams, row):
    new_beams = []
    split_count = 0
    for splitter in row:
        if splitter in beams:
            new_beams.extend([splitter-1, splitter+1])
            split_count += 1
    new_beams = set(new_beams) | set(beam for beam in beams if beam not in row)
    return new_beams, split_count
def calculate_total_splits(start, splitters):
    beams = [start]
    result = 0
    for row in splitters:
        print("".join(["|" if i in beams else "." for i in range(141)]))
        print("".join(["^" if i in row else ("|" if i in beams else ".") for i in range(141)]))
        beams, split_count = split(beams, row)
        result += split_count
    return result
def part_1(fp):
    return calculate_total_splits(*(parse(fp)))

if __name__ == "__main__":
    print(part_1("input"))