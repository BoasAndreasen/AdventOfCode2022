file = open('input.txt', 'r')


def one():
    points = 0

    for line in file:
        line = line.strip('\n').split(' ')
        if line[0] == 'A':  # rock
            if line[1] == 'Y':  # paper
                points += 6  # for winning
                points += 2  # for picking paper
            elif line[1] == 'X':  # rock
                points += 3  # for picking scissors
                points += 1  # for picking rock
            elif line[1] == 'Z':  # scissors
                points += 0
                points += 3  # for picking scissors
        elif line[0] == 'B':  # paper
            if line[1] == 'Z':  # scissors
                points += 6
                points += 3  # for picking scissors
            elif line[1] == 'Y':  # paper
                points += 3
                points += 2  # for picking paper
            elif line[1] == 'X':  # rock
                points += 0
                points += 1  # for picking rock
        elif line[0] == 'C':  # scissors
            if line[1] == 'X':  # rock
                points += 6
                points += 1  # for picking rock
            elif line[1] == 'Z':  # scissors
                points += 3
                points += 3  # for picking scissors
            elif line[1] == 'Y':  # paper
                points += 0
                points += 2  # for picking paper
    print(points)


def two():
    win = {'A': 'Y',
           'B': 'Z',
           'C': 'X'}

    draw = {'A': 'X',
            'B': 'Y',
            'C': 'Z'}

    lose = {'A': 'Z',
            'B': 'X',
            'C': 'Y'}

    points_pick = {'Z': 3,
                   'Y': 2,
                   'X': 1}

    points = 0

    for line in file:
        line = line.strip('\n').split(' ')

        # add points from winning, drawing, or losing
        if line[1] == 'Z':  # win
            points += 6
        elif line[1] == 'Y':  # draw
            points += 3
        elif line[1] == 'X':  # lose
            points += 0

        # add points from picking rock, paper, or scissors
        if line[0] == 'A':  # rock
            if line[1] == 'Y':  # draw
                points += points_pick[draw['A']]
            elif line[1] == 'X':  # lose
                points += points_pick[lose['A']]
            elif line[1] == 'Z':  # win
                points += points_pick[win['A']]
        elif line[0] == 'B':  # paper
            if line[1] == 'Y':  # draw
                points += points_pick[draw['B']]
            elif line[1] == 'X':  # lose
                points += points_pick[lose['B']]
            elif line[1] == 'Z':  # lose
                points += points_pick[win['B']]
        elif line[0] == 'C':  # paper
            if line[1] == 'Y':  # draw
                points += points_pick[draw['C']]
            elif line[1] == 'X':  # lose
                points += points_pick[lose['C']]
            elif line[1] == 'Z':  # lose
                points += points_pick[win['C']]

    return points
