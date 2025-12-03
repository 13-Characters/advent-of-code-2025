def part_1(file_name):
    result = 0
    for line in open(file_name):
        mx = 0
        for i, digit_1 in enumerate(line):
            for j, digit_2 in enumerate(line[i+1:]):
                joltage = int(digit_1+digit_2)
                if joltage > mx:
                    mx = joltage
        result += mx
    return result

n = 12
digits = [9, 8, 7, 6, 5, 4, 3, 2, 1]
def biggest(line, n):
    for digit in digits:
        if (s:=str(digit)) in line and len(subline:=line[line.find(s)+1:]) >= n-1:
            if n <= 1:
                return int(digit)
            return int(str(digit)+str(biggest(subline, n-1)))
def part_2(file_name):
    result = 0
    for line in open(file_name):
        result += biggest(line.strip(), 12)
    return result


if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))