class CalorieCounting:
    def __init__(self, file):
        self.file = file

    def star1(self):
        maximum_elf = 0
        counter = 0

        for line in self.file:
            if len(line.strip('\n')) == 0:
                maximum_elf = max(maximum_elf, counter)
                counter = 0
            else:
                counter += int(line.strip('\n'))

        # check last line since it might not be empty
        maximum_elf = max(maximum_elf, counter)

        return maximum_elf

    def star2(self):
        maximum_elves = [0, 0, 0]
        counter = 0

        for line in self.file:
            if len(line.strip('\n')) == 0:
                # if larger than largest, set current to largest
                # and set largest to second largest and second largest to third largest
                for i in range(len(maximum_elves)):
                    if maximum_elves[i] <= counter:
                        maximum_elves[i + 1:] = maximum_elves[i:-1]
                        maximum_elves[i] = counter
                        break
                counter = 0
            else:
                counter += int(line.strip('\n'))

        # check last line since it might not finish with empty line
        for i in range(len(maximum_elves)):
            if maximum_elves[i] <= counter:
                maximum_elves[i + 1:] = maximum_elves[i:-1]
                maximum_elves[i] = counter
                break

        # return sum of top three elves
        return sum(maximum_elves)
