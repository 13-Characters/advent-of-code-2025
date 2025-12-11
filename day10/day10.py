from itertools import combinations_with_replacement
from functools import reduce
from operator import xor

# is there really no built in thing in Python that does this exact thing
class TupleIterator:
    def __init__(self, size):
        self.size = size
        self.next = (0,)*size
        self.maxm = 0
    def __next__(self):
        old_next = self.next
        new_next = list(self.next)
        for i in range(len(new_next)):
            if new_next[i] < self.maxm:
                new_next[i] += 1
                break
            else:
                new_next[i] = 0
        if max(new_next) < self.maxm:
            for i in range(len(new_next)):
                if new_next[i]:
                    new_next[i] = self.maxm
                    break
        self.next = tuple(new_next)
        if not any(new_next): # If we have the matrix of all 0s
            self.maxm += 1
            self.next = (self.maxm,) + (0,) * (self.size - 1)
        return old_next
    def __iter__(self):
        return TupleIterator(self.size)

class Machine:
    def __init__(self, line):
        l = line.strip().split()
        lights = l[0].removeprefix("[").removesuffix("]")
        self.lights = int(lights[::-1].replace(".","0").replace("#","1"),2)
        self.buttons = [sum(2**a for a in map(int,b[1:-1].split(","))) for b in l[1:-1]]
        self.joltage = tuple(map(int, l[-1][1:-1].split(",")))
    def find_fewest_button_presses(self):
        r = 1
        while True:
            for comb in combinations_with_replacement(self.buttons, r):
                if reduce(xor, comb) == self.lights:
                    return r
            r += 1
    def get_matrix(self):
        return list(map(list, zip(*[list(map(int, f"{b:0{len(self.joltage)}b}"))[::-1] for b in self.buttons])))
    def find_fewest_button_presses_with_joltage(self):
        matrix = self.get_matrix()
        fewest = float('inf')
        nullity = len(self.buttons) - len(self.joltage)
        if nullity == 0:
            # Row reduce an augmented square matrix
            augmented_matrix = [row+[jolt] for row,jolt in zip(matrix, self.joltage)]
            return sum(row_reduce(augmented_matrix))
        elif nullity < 0:
            print("more columns than rows")
            pass
        else:
            print("more rows than columns")
            pass
        return 0

# Row reduce a square matrix, return the final answer
def row_reduce(m):
    def swap(m, i, j):
        tmp = m[i].copy()
        m[i] = m[j].copy()
        m[j] = tmp
    def add_mult_of_row(m, a, i, j):
        m[j] = [int(x+a*y) for x,y in zip(m[j], m[i])]
    def mult_row(m, a, i):
        m[i] = [int(a*x) for x in m[i]]

    # We assume this is a square matrix for now
    for i in range(len(m)):
        if m[i][i] == 0:
            for j in range(i+1, len(m)):
                if m[j][i] != 0:
                    swap(m, i, j)
                    break



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