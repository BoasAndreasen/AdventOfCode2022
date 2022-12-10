file = open('input.txt', 'r')


def one(file_input):
    cycle = 1
    total = 1

    values = [20, 60, 100, 140, 180, 220]

    res = []

    for line in file_input:
        current_line = line.strip('\n').split(' ')

        if current_line[0] == 'noop':
            cycle += 1
        elif current_line[0] == 'addx':
            cycle += 2
            total += int(current_line[1])

        if cycle in values:
            res.append(cycle * total)
            values.pop(0)
        elif cycle + 1 in values:
            res.append((cycle + 1) * total)
            values.pop(0)

    return sum(res)


def two(file_input):
    cycle = 1
    total = 1

    res = []

    for line in file_input:
        current_line = line.strip('\n').split(' ')

        #TO DO...

    return res


print(two(file))
