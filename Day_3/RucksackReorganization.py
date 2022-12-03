file = open('input.txt', 'r')


def one():
    res = 0

    for line in file:
        d1 = {}
        d2 = {}

        line = line.strip('\n')
        # first half of list
        for el in line[:len(line) // 2]:
            if el in d1:
                d1[el] += 1
            else:
                d1[el] = 1

        # second half of list
        for el in line[len(line) // 2:]:
            if el in d2:
                d2[el] += 1
            else:
                d2[el] = 1

        # find common elements
        for common in d1.keys() & d2.keys():
            if common.islower():
                res += ord(common) - 96
            elif common.isupper():
                res += ord(common) - 38  # 96 + 58

    return res


def two():
    res = 0

    d1 = {}
    d2 = {}
    d3 = {}

    line_number = 1

    for line in file:
        line = line.strip('\n')
        for el in line:
            if line_number == 1:
                if el in d1:
                    d1[el] += 1
                else:
                    d1[el] = 1
            elif line_number == 2:
                if el in d2:
                    d2[el] += 1
                else:
                    d2[el] = 1
            elif line_number == 3:
                if el in d3:
                    d3[el] += 1
                else:
                    d3[el] = 1

        if line_number == 3:
            # every three lines have 1 common element
            common = (d1.keys() & d2.keys() & d3.keys()).pop()

            if common.islower():
                res += ord(common) - 96
            elif common.isupper():
                res += ord(common) - 38  # 96 + 58

            line_number = 1
            d1 = {}
            d2 = {}
            d3 = {}
        else:
            line_number += 1

    return res
