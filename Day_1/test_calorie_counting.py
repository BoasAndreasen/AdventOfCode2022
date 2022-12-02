from calorie_counting import CalorieCounting


def test_star1_input1():
    file = open('input1.txt', 'r')
    calorie = CalorieCounting(file)

    assert calorie.star1() == 68787


def test_star1_input2():
    file = open('input2.txt', 'r')
    calorie = CalorieCounting(file)

    assert calorie.star1() == 24000


def test_star2_input1():
    file = open('input1.txt', 'r')
    calorie = CalorieCounting(file)

    assert calorie.star2() == 198041


def test_star2_input2():
    file = open('input2.txt', 'r')
    calorie = CalorieCounting(file)

    assert calorie.star2() == 45000
