def parse_part_1(fp):
    grid = [[x for x in line.split(" ") if x.strip()] for line in open(fp)]
    return grid
def parse_part_2(fp):
    lines = open(fp).readlines()
    m = ["*" in l or "+" in l for l in lines].index(True)
    size = max([len(l) for l in lines])
    indices = [i for i in range(len(lines[m])) if lines[m][i] in ["+", "*"]] + [size]
    grid = [[line[a:b-1] for a, b in zip(indices[:-1], indices[1:])] for line in lines]
    return grid

# somehow i feel like these could be useful for part 2... (it wasn't)
def multiply(a, b):
    return a*b
def add(a, b):
    return a+b
def apply_all(nums, operation):
    while len(nums) > 1:
        temp = nums[-1]
        del nums[-1]
        nums[-1] = operation(nums[-1], temp)
    return nums[0]

def transpose(nums):
    return ["".join(nums[j][i] for j in range(len(nums))) for i in range(len(nums[0]))]

def part_1(fp):
    result = 0
    grid = parse_part_1(fp)
    size = len(grid[0])
    for j in range(size):
        nums = [grid[i][j] for i in range(len(grid))]
        operation = multiply if nums.pop() == "*" else add
        nums = list(map(int, nums))
        result += apply_all(nums, operation)
    return result

def part_2(fp):
    result = 0
    grid = parse_part_2(fp)
    size = len(grid[0])
    for j in range(size):
        nums = [grid[i][j] for i in range(len(grid))]
        operation = multiply if nums.pop().strip() == "*" else add
        nums = list(map(int, transpose(nums)))
        result += apply_all(nums, operation)
    return result

if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))