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
                elif diff_prev[1] > 0 or diff[1] < 0:
                    winding_number -= 1
        diff_prev = diff
    return winding_number != 0

def make_compression(points):
    x_values = list(sorted(set(point[0] for point in points)))
    y_values = list(sorted(set(point[1] for point in points)))
    size = (2*len(x_values)+1, 2*len(y_values)+1)
    def search_range(a, values):
        if a < values[0]:
            return 0
        elif a > values[-1]:
            return len(values)*2
        i,j = 0,len(values)-1
        while abs(j-i) > 1:
            if values[i] < a < values[j//2]:
                j = j//2
            else:
                i = j//2
        return i+j + 1
    def compression(x,y):
        if x in x_values:
            x_new = x_values.index(x)*2 + 1
        else:
            x_new = search_range(x, x_values)
        if y in y_values:
            y_new = y_values.index(y)*2 + 1
        else:
            y_new = search_range(y, y_values)
        return x_new,y_new
    return compression, size


def part_1(fp):
    return max(get_matrix(fp)[1].values())

def part_2(fp):
    points, mat = get_matrix(fp)
    keys_to_check = sorted(mat.keys(),key=lambda x: mat[x], reverse=True)
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    # Computing this takes O(n^3) time
    outside_points = [(x, y) for x in x_values for y in y_values if not is_inside((x, y), points)]
    for key in keys_to_check:
        i,j = key
        a,b = points[i], points[j]
        x_left, x_right = min(a[0], b[0]), max(a[0], b[0])
        y_up, y_down = min(a[1], b[1]), max(a[1], b[1])
        good = not any(point for point in outside_points if x_left<=point[0]<=x_right and y_up<=point[1]<=y_down)
        if good:
            print(a, b)
            return area(a,b)

def part_2_fast(fp):
    points_uncompressed, mat = get_matrix(fp)
    keys_to_check = sorted(mat.keys(), key = lambda x: mat[x], reverse = True)
    compression,size = make_compression(points_uncompressed)
    points = [compression(*p) for p in points_uncompressed]
    inside={(i,j): False for i in range(size[0]) for j in range(size[1])}

    # Draw the outline
    for p1,p2 in zip(points,points[1:]+[points[0]]):
        x_min, x_max = min(p1[0], p2[0]), max(p1[0], p2[0])
        y_min, y_max = min(p1[1], p2[1]), max(p1[1], p2[1])
        for x in range(x_min,x_max+1):
            for y in range(y_min, y_max + 1):
                inside[x,y] = True

    # Fill the inside
    for y in range(size[1]):
        fill = False
        for x in range(0, size[1] - 1):
            if fill:
                inside[x,y] = True
            if inside[x,y]:
                fill = not inside[x+1,y]

    for key in keys_to_check:
        i,j = key
        a,b = points[i], points[j]
        x_left, x_right = min(a[0], b[0]), max(a[0], b[0])
        y_up, y_down = min(a[1], b[1]), max(a[1], b[1])
        for x in x_values:
            for y in y_values:
                pass

if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))