commands = []

with open('Test Data.txt') as d: #importing data
    for line in d:
        commands.append(str(line.strip()))
d.close()

print(commands)


class Folder:
    name = "New Folder"
    size = -1
    parent = None
    contents = []

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        if parent:
            parent.contents.add(self)


class File:
    name = "New File"
    size = -1
    parent = None

    def __init__(self, size, name, parent):
        self.name = name
        self.size = size
        self.parent = parent
        if parent:
            parent.contents.add(self)


root = Folder("/", None)
pointer = root

for i in range(len(commands)):
    if commands[i][0] == "$":
        if "ls" in commands[i]:
            if "dir" in commands[i]:
                Folder(commands[i-1], pointer)
            else:
                var = commands[i].split()
                print(var)
                File(var[1], var[0], pointer)
        elif "cd" in commands[i]:
            pass


print(root.contents)





