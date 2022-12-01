f = open('input.txt', 'r')

maximum_elf = 0
counter = 0

for line in f:
    if len(line.strip('\n')) == 0:
        maximum_elf = max(maximum_elf, counter)
        counter = 0
    else:
        counter += int(line.strip('\n'))

# check last line since it might not be empty
maximum_elf = max(maximum_elf, counter)

print(maximum_elf)

f.close()
