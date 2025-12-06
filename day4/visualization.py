from PIL import Image
def valid(pos, grid):
    width, height = len(grid[0]), len(grid)
    x, y = pos[0], pos[1]
    return (0 <= x < width and 0 <= y < height) and (grid[y][x])

def to_image(grid, grid_new, output_name):
    width, height = len(grid[0]), len(grid)
    white = (255, 255, 255)
    red = (255, 0, 0)
    black = (0, 0, 0)
    image_bytes = bytearray()
    for y in range(height):
        for x in range(width):
            old = grid[y][x]
            new = grid_new[y][x]
            if old != new:
                image_bytes.extend(red)
            else:
                if old:
                    image_bytes.extend(white)
                else:
                    image_bytes.extend(black)
    image = Image.frombytes("RGB", (width, height), image_bytes)
    image.save(f"visualization/{output_name}.png")


def part_2(fp):
    grid = []
    result = 0
    for row in open(fp):
        row = row.strip()
        grid.append([x=="@" for x in row])
    grid_new = [line.copy() for line in grid]

    counter = 0
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
        to_image(grid, grid_new, str(counter))
        counter += 1
        if grid_new == grid:
            break
        else:
            grid = [line.copy() for line in grid_new]
    return result

if __name__ == "__main__":
    print(part_2("input"))