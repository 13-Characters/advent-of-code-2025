from itertools import combinations_with_replacement
from functools import reduce
from operator import xor

class Machine:
    def __init__(self, line):
        l = line.strip().split()
        lights = l[0].removeprefix("[").removesuffix("]")
        self.lights = int(lights[::-1].replace(".","0").replace("#","1"),2)
        self.buttons = [sum(2**a for a in map(int,b[1:-1].split(","))) for b in l[1:-1]]
        self.joltage = tuple(map(int, l[-1][1:-1].split(",")))
    def find_fewest_button_presses(self, pattern=None):
        r = 1
        pattern = pattern if pattern else self.lights
        while True:
            for comb in combinations_with_replacement(self.buttons, r):
                if reduce(xor, comb) == pattern:
                    return r
            r += 1

    def find_fewest_button_presses_with_joltage(self, joltage=None):
        # https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/
        joltage = joltage if joltage else self.joltage
        pass



def part_1(fp):
    result = 0
    for line in open(fp):
        m = Machine(line)
        result += m.find_fewest_button_presses()
    return result
def part_2(fp):
    result = 0
    for line in open(fp):
        m = Machine(line)
        result += m.find_fewest_button_presses_with_joltage()
    return result
if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))