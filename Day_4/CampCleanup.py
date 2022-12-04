file = open('input.txt', 'r')


def one():
    result = 0

    for line in file:
        line = line.strip('\n').split(',')

        first = list(map(int, line[0].split('-')))
        second = list(map(int, line[1].split('-')))

        if first[0] <= second[0] and first[1] >= second[1]:
            result += 1
        elif first[0] >= second[0] and first[1] <= second[1]:
            result += 1

    return result


def two():
    result = 0

    for line in file:
        line = line.strip('\n').split(',')

        first = list(map(int, line[0].split('-')))
        second = list(map(int, line[1].split('-')))

        if first[0] <= second[0] <= first[1] or first[0] <= second[1] <= first[1]:
            result += 1
        elif second[0] <= first[0] <= second[1] or second[0] <= first[1] <= second[1]:
            result += 1

    return result
