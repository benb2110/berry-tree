commands = []

with open('../../../../Non Git/Test Data.txt') as d: #importing data
    for line in d:
        commands.append(line.split())
d.close()

#print(commands)


class Folder:
    size = 0
    name = "New Folder"
    parent = None
    contents = []

    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        if parent:
            parent.contents.add(self)


class File:
    size = 0
    name = "New File"
    parent = None

    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        if parent:
            parent.contents.add(self)


root = Folder('/', 0, None)


def directory_sort(data):
    directory = root
    for i in range(len(data)):
        print(root.contents)
        if data[i][0] == '$':
            if data[i][1] == 'cd':
                if data[i][2] == '..': #Directory out
                    print(data[i])
                    print(directory.parent)
                    directory = directory.parent
                elif data[i][2] == '/': #Root directory
                    directory = root
                else: #directory change
                    directory = data[i][2]
            elif data[i][1] == 'ls': #lists (ignore)
                continue
        elif data[i][0] == 'dir': #directory in current location
            if (data[i][1]):
                continue
            else:
                print('true4')
                Folder(str(data[i][2]), 0, directory)
        else: #file in current location
            if data[i][1]:
                print('true2')
                continue
            else:
                print('true3')
                File(str(data[i][1]), int(data[i][0]), directory)


directory_sort(commands)



#print(root.size)
