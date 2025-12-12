def parse(fp):
    shapes = []
    parse_shapes = True
    current_shape = []
    requirements = []
    for line in open(fp):
        if "x" in line:
            parse_shapes = False
        if parse_shapes:
            if line.strip() and ":" not in line:
                current_shape.append([1 if i=="#" else 0 for i in line.strip()])
            elif not line.strip():
                shapes.append(current_shape)
                current_shape = []
        if not parse_shapes:
            dimensions, nums = line.split(":")
            dimensions = tuple(map(int, dimensions.split("x")))
            nums = tuple(map(int, nums.split()))
            requirements.append((dimensions, nums))
    return shapes, requirements

def area(shape):
    return sum(sum(row) for row in shape)
def check_min_size(requirement, shape):
    pass
def part_1(fp):
    shapes, requirements = parse(fp)
    result = 0
    # Make a guess
    for requirement in requirements:
        num_shapes = requirement[1]
        total_area_rect = requirement[0][0]*requirement[0][1]
        total_area_shapes = sum(n*area(shape) for n,shape in zip(num_shapes,shapes))
        if total_area_shapes < total_area_rect:
            result += 1
    return result
def part_2(fp):
    pass

if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))