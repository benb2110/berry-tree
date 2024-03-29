commands = []

with open('Data.txt') as d: #importing data
    for line in d:
        commands.append(line.split())
d.close()

print(commands)


class Folder:
    size = 0
    name = "New Folder"
    parent = None
    contents = []

    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.contents = []
        self.parent = parent
        if parent:
            parent.contents.append(self)


class File:
    size = 0
    name = "New File"
    parent = None

    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        if parent:
            parent.contents.append(self)


root = Folder('/', 0, None)


def directory_sort(data):
    directory = root
    for i in range(len(data)):
        #print(i)
        #print(root.contents) # DEBUG
        if data[i][0] == '$':  #commands
            if data[i][1] == 'cd':
                if data[i][2] == '..': #Directory out
                    directory = directory.parent
                elif data[i][2] == '/': #Root directory
                    directory = root
                elif data[i][1] == 'ls': #print lists command (ignore)
                    continue
                else: #directory change
                    found_match = False
                    for possible_match in directory.contents:
                        if possible_match.name == data[i][2]:
                            found_match = True
                            directory = possible_match
                            break
                    if not found_match:
                        folder = Folder(str(data[i][1]), 0, directory)
                        directory = folder
        elif data[i][0] == 'dir': #create directory (Folder) in current location if it does not exist
            found_match = False
            for possible_match in directory.contents:
                if possible_match.name == data[i][1]:
                    found_match = True
                    break
            if not found_match:
                Folder(str(data[i][1]), 0, directory)
        else: #create file in current location if it does not exist
            found_match = False
            for possible_match in directory.contents:
                if possible_match.name == data[i][1]:
                    found_match = True
                    break
            if not found_match:
                File(str(data[i][1]), int(data[i][0]), directory)


def file_size(folder):
    for item in folder.contents:
        if isinstance(item, Folder):
            file_size(item)
            folder.size += item.size
        elif isinstance(item, File):
            folder.size += item.size


def size_limit(folder):
    tot = 0
    for item in folder.contents:
        if isinstance(item, Folder):
            if item.size < 100000:
                tot += item.size
            tot += size_limit(item)
    return tot


directory_sort(commands)
file_size(root)
print(size_limit(root))

