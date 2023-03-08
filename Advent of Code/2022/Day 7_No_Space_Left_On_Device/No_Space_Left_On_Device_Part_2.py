commands = []

with open('Data.txt') as d: #importing data
    for line in d:
        commands.append(line.split())
d.close()

#print(commands)
diskspace = 70000000


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


root = Folder('/', 0, None) #Creating instance of root directory


def directory_sort(data): #creates the file/folder structure based on instructions
    directory = root        #sets directory pointer location
    for i in range(len(data)):
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


def folder_size(folder):  #recurse through files/folders and calculates foldersizes
    for item in folder.contents:
        if isinstance(item, Folder):
            folder_size(item)
            folder.size += item.size
        elif isinstance(item, File):
            folder.size += item.size


folder_sizes = []


def folder_sort(root): #creates a list of all folder sizes and then sorts them low to high
    for item in root.contents:
        if isinstance(item, Folder):
            folder_sort(item)
            folder_sizes.append(item.size)
    folder_sizes.sort()


directory_sort(commands) #creates the file/folder structure based on instructions
folder_size(root) #calculates filesizes


space = diskspace - root.size
space_needed = 30000000 - space

folder_sort(root)


for i in range(len(folder_sizes)):  #finds the smallest folder that is larger than the space needed
    if folder_sizes[i] > space_needed:
        print(folder_sizes[i])
        break
