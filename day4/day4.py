def valid(pos, grid):
    width, height = len(grid[0]), len(grid)
    x, y = pos[0], pos[1]
    return (0 <= x < width and 0 <= y < height) and (grid[y][x])
def part_1(fp):
    grid = []
    result = 0
    for row in open(fp):
        row = row.strip()
        grid.append([x=="@" for x in row])

    for y, row in enumerate(grid):
        for x, roll in enumerate(row):
            if roll:
                adjacent_positions = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1),
                                      (x+1, y-1), (x+1, y), (x+1, y+1)]
                adjacent_positions = list(filter(lambda j: valid(j, grid), adjacent_positions))
                if len(adjacent_positions) < 4:
                    result += 1
    return result

def part_2(fp):
    grid = []
    result = 0
    for row in open(fp):
        row = row.strip()
        grid.append([x=="@" for x in row])
    grid_new = [line.copy() for line in grid]

    while True:
        for y, row in enumerate(grid_new):
            for x, roll in enumerate(row):
                if roll:
                    adjacent_positions = [(x-1, y-1), (x-1, y), (x-1, y+1), (x, y-1), (x, y+1),
                                          (x+1, y-1), (x+1, y), (x+1, y+1)]
                    adjacent_positions = list(filter(lambda j: valid(j, grid), adjacent_positions))
                    if len(adjacent_positions) < 4:
                        grid_new[y][x] = False
                        result += 1
        if grid_new == grid:
            break
        else:
            grid = [line.copy() for line in grid_new]
    return result


if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))