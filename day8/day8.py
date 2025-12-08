from math import prod
def parse(fp):
    return [tuple(map(int, line.strip().split(","))) for line in open(fp)]
def dist(a, b):
    return sum((y-x)**2 for x,y in zip(a,b))
def same_circuit(circuits, a, b):
    for circuit in circuits:
        if a in circuit and b in circuit:
            return True
        elif a in circuit or b in circuit:
            return False
    return None

def part_1(fp):
    points = parse(fp)
    mat = {(i,j): dist(points[i], points[j]) for i in range(len(points)) for j in range(len(points))}
    circuits = [[i] for i in range(len(points))]
    keys_to_check = list(sorted((k for k in mat.keys() if k[0] < k[1]), key=lambda k: mat[k]))
    counter = 0
    for x,y in keys_to_check:
        if counter >= 1000:
            break
        if not same_circuit(circuits, x, y):
            x_index = [x in c for c in circuits].index(True)
            y_index = [y in c for c in circuits].index(True)
            circuits[x_index].extend(circuits[y_index])
            del circuits[y_index]
        counter += 1
    circuits.sort(key=len, reverse=True)
    return prod(len(circuit) for circuit in circuits[:3])

def part_2(fp):
    points = parse(fp)
    mat = {(i,j): dist(points[i], points[j]) for i in range(len(points)) for j in range(len(points))}
    circuits = [[i] for i in range(len(points))]
    keys_to_check = list(sorted((k for k in mat.keys() if k[0] < k[1]), key=lambda k: mat[k]))
    for x,y in keys_to_check:
        if not same_circuit(circuits, x, y):
            x_index = [x in c for c in circuits].index(True)
            y_index = [y in c for c in circuits].index(True)
            circuits[x_index].extend(circuits[y_index])
            del circuits[y_index]
            if len(circuits) == 1:
                return points[x][0] * points[y][0]


if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))