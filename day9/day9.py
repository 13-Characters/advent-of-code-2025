from math import prod
def area(a,b):
    return prod(abs(y-x)+1 for x,y in zip(a,b))
def parse(fp):
    return [tuple(map(int, l.strip().split(","))) for l in open(fp)]
def get_matrix(fp):
    points = parse(fp)
    mat = {(i, j): area(points[i], points[j]) for i in range(len(points)) for j in
           range(len(points)) if i<j}
    return points, mat

def is_inside(point_1, loop):
    # Implementation of the winding number algorithm
    winding_number = 0
    diff_prev = False
    for point_2 in loop:
        diff = tuple(y-x for x,y in zip(point_1, point_2))
        if diff_prev and diff[0]>0:
            if diff_prev[1]*diff[1] < 0:
                if diff_prev[1] < 0:
                    winding_number += 2
                else:
                    winding_number -= 2
            if diff_prev[1]*diff[1] == 0:
                if diff_prev[1] < 0 or diff[1] > 0:
                    winding_number += 1
                else:
                    winding_number -= 1
        diff_prev = diff
    return winding_number != 0


def part_1(fp):
    return max(get_matrix(fp)[1].values())

def part_2(fp):
    points, mat = get_matrix(fp)
    keys_to_check = sorted(mat.keys(),key=lambda x: mat[x], reverse=True)
    for key in keys_to_check:
        i,j = key
        a,b = points[i], points[j]
        x_left, x_right = min(a[0], b[0]), max(a[0], b[0])
        y_up, y_down = min(a[1], b[1]), max(a[1], b[1])

        x_values = [point[0] for point in points if point[0] in range(x_left, x_right+1)]
        x_values = set((x+y)//2 for x,y in zip(x_values[0:-1],x_values[1:]))
        y_values = [point[1] for point in points if point[1] in range(y_up, y_down+1)]
        y_values = set((x + y) // 2 for x, y in zip(y_values[0:-1], y_values[1:]))

        good = True
        for x in x_values:
            if not is_inside((x, y_up), points) or not is_inside((x, y_down), points):
                good = False
        for y in y_values:
            if not is_inside((x_left, y), points) or not is_inside((x_right, y), points):
                good = False
        if good:
            return area(a,b)

if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))