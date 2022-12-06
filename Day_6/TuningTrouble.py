file = open('input.txt', 'r')


def one():
    current = file.readline().strip('\n')

    for i in range(len(current)-3):
        if len(set(current[i:i+4])) == len(current[i:i+4]):
            return i+4


def two():
    current = file.readline().strip('\n')

    for i in range(len(current)-13):
        if len(set(current[i:i+14])) == len(current[i:i+14]):
            return i+14

