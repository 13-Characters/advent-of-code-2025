from collections import Counter
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
def split_quantum(beams: Counter, row):
    new_beams = Counter()
    for beam in beams:
        if beam in row:
            new_beams[beam-1] += beams[beam]
            new_beams[beam+1] += beams[beam]
        if beam not in row:
            new_beams[beam] += beams[beam]
    return new_beams, 0
def calculate_total_splits(start, splitters, quantum=False):
    beams = Counter({start:1}) if quantum else [start]
    result = 0
    for row in splitters:
        beams, split_count = split_quantum(beams, row) if quantum else split(beams, row)
        result += split_count if not quantum else 0
    return result if not quantum else sum(beams.values())

def part_1(fp):
    return calculate_total_splits(*(parse(fp)))
def part_2(fp):
    return calculate_total_splits(*(parse(fp)), quantum=True)

if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))