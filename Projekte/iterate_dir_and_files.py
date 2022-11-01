import os

for path, currentDirectory, files in os.walk("../GUI"):
    for file in files:
        print(path)
        print(file)
        #print(os.path.join(path, file))