file = open('input.txt', 'r')


def one(num_stacks=9):
    current = file.readline().strip('\n')

    stacks = [[] for _ in range(num_stacks)]

    # fill initial stacks
    while '[' in current:
        # number of stacks changes each line
        num_stacks_line = round((len(current) + 1) / 4)

        for i in range(num_stacks_line):
            if current[1 + i * 4] != ' ':
                stacks[i].append(current[1 + i * 4])

        current = file.readline().strip('\n')

    # skip line
    file.readline()
    current = file.readline().strip('\n').split(' ')

    while current != ['']:
        amount = int(current[1])
        source = int(current[3]) - 1
        dest = int(current[5]) - 1

        stacks[dest] = stacks[source][:amount][::-1] + stacks[dest]
        stacks[source] = stacks[source][amount:]

        current = file.readline().strip('\n').split(' ')
    print(stacks)

    res = []

    for i in range(len(stacks)):
        res.append(stacks[i][0])
    print("".join(res))


# same solution as above without reverse
def two(num_stacks=9):
    current = file.readline().strip('\n')

    stacks = [[] for _ in range(num_stacks)]

    # fill initial stacks
    while '[' in current:
        # number of stacks changes each line
        num_stacks_line = round((len(current) + 1) / 4)

        for i in range(num_stacks_line):
            if current[1 + i * 4] != ' ':
                stacks[i].append(current[1 + i * 4])

        current = file.readline().strip('\n')

    # skip line
    file.readline()
    current = file.readline().strip('\n').split(' ')

    while current != ['']:
        amount = int(current[1])
        source = int(current[3]) - 1
        dest = int(current[5]) - 1

        stacks[dest] = stacks[source][:amount] + stacks[dest]
        stacks[source] = stacks[source][amount:]

        current = file.readline().strip('\n').split(' ')

    res = []

    for i in range(len(stacks)):
        res.append(stacks[i][0])
    print("".join(res))

