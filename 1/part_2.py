f = open('input.txt', 'r')

maximum_elves = [0, 0, 0]
counter = 0

for line in f:
    if len(line.strip('\n')) == 0:
        # if larger than largest, set current to largest
        # and set largest to second largest and second largest to third largest

        for i in range(len(maximum_elves)):
            if maximum_elves[i] <= counter:
                maximum_elves[i+1:] = maximum_elves[i:-1]
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

print("Sum of top three elves is: " + str(sum(maximum_elves)))

f.close()
