class Node(object):
    def __init__(self, size, name, parent):
        self.size = size
        self.name = name
        self.children = []
        self.parent = parent

    def add_child(self, obj):
        self.children.append(obj)

    def get_child(self, obj):
        for child in self.children:
            if child.name == obj:
                return child

    def size_of_all_children(self):
        if not self.children:
            return self.size

        return sum([child.size_of_all_children() for child in self.children])

    '''
    def size_of_small_dir(self):
        if not self.children and self.size_of_all_children() <= 100000:
            return self.size #* self.depth_of_node()

        return sum([child.size_of_all_children() for child in self.children])

    def depth_of_node(self):
        counter = 0
        current = self

        while current.parent is not None:
            if 0 < current.size_of_all_children() <= 100000:
                counter += 1
            current = current.parent

        return counter

    def size_of_current_dictionary(self):
        # if self is root
        if self.parent is None:
            return self.size

        current = self.parent

        total = 0

        for child in current.children:
            total += child.size

        return total
    '''

    # incomplete
    def ree(self, total=0):
        for ch1 in self.children:
            # if ch1.name[:3] == 'dir' and 368913 > ch1.size_of_all_children() > 358913:  # dir ptgn 366028 min
            if ch1.name[:3] == 'dir' and 368913 > ch1.size_of_all_children() <= 100000:  # sum all sizes
                print(ch1.name, ch1.size_of_all_children())
                total += ch1.size_of_all_children()

        for ch1 in self.children:
            ch1.ree()

        return total


file = open('input.txt', 'r')


def one():
    root = Node(0, 'dir root', None)
    current = root

    '''
    current.add_child(Node(0, 'dir a', current))
    current.add_child(Node(14848514, 'b.txt', current))
    current.add_child(Node(8504156, 'c.dat', current))
    current.add_child(Node(0, 'dir d', current))

    current = current.get_child('dir a')
    current.add_child(Node(0, 'dir e', current))
    current.add_child(Node(29116, 'f', current))
    current.add_child(Node(2557, 'g', current))
    current.add_child(Node(62596, 'h.lst', current))

    current = current.get_child('dir e')
    current.add_child(Node(584, 'i', current))

    current.add_child(Node(0, 'dir p', current))

    current = current.parent
    current = current.parent
    current = current.get_child('dir d')

    current.add_child(Node(4060174, 'j', current))
    current.add_child(Node(8033020, 'd.log', current))
    current.add_child(Node(5626152, 'd.ext', current))
    current.add_child(Node(7214296, 'k', current))

    '''
    for line in file:
        current_line = line.strip('\n').strip('$ ').split(' ')
        # print(current_line)

        if current_line[0] == 'cd' and current_line[1] == '/':
            current = root
        elif current_line[0] == 'cd' and current_line[1] == '..':
            current = current.parent
        elif current_line[0] == 'cd':
            current = current.get_child('dir ' + current_line[1])
        elif current_line[0] == 'dir':
            current.add_child(Node(0, 'dir ' + current_line[1], current))
        elif current_line[0] == 'ls':
            continue
        else:
            current.add_child(Node(int(current_line[0]), current_line[1], current))

    print(root.ree())


one()
