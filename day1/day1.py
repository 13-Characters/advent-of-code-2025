def part_1(input):
    dial = 50
    password = 0
    for line in open(input):
        direction, amount = line[0], line[1:]
        if direction == "L":
            dial = (dial - int(amount)) % 100
        if direction == "R":
            dial = (dial + int(amount)) % 100
        if dial == 0:
            password += 1
    return password

def increment(dial, amount):
    if amount < 0:
        dial = (-dial) % 100
        amount = -amount
    return (dial + amount) // 100
def part_2(input):
    dial = 50
    password = 0
    for line in open(input):
        direction, amount = line[0], line[1:]
        amount = int(amount)
        if direction == "L":
            amount = -amount
        if dial == 0:
            password += increment(dial, amount)
        else:
            password += increment(dial, amount)
        dial += amount
        dial = dial % 100
    return password

if __name__ == "__main__":
    print(part_1("input"))
    print(part_2("input"))