import os

def search_string_in_files(directory, search_string):
    matching_files = []
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r') as f:
                    # Check if the search string is in the file
                    if search_string in f.read():
                        #matching_files.append(file_path)
                        matching_files.append(os.path.basename(file_path))
            except (UnicodeDecodeError, FileNotFoundError):
                # Handle files that can't be read or don't exist
                print("cannot read file: ")
                continue

    return matching_files

if __name__ == "__main__":
    #dir_to_search = input("C:\\Users\\Philipp\\Desktop_PC\\DM 2.24.10.1\\Database\\OBDProtocols")
    dir_to_search = "C:\\Users\\Philipp\\Desktop_PC\\DM 2.24.10.1\\Database\\OBDProtocols"
    #string_to_search = input("143938")
    string_to_search = "954412"
    
    # Check if the provided path is absolute
    if not os.path.isabs(dir_to_search):
        print("Please provide an absolute path.")
    else:
        print("Start...")
        results = search_string_in_files(dir_to_search, string_to_search)
        print("END")
        if results:
            print("Files containing the string:")
            size = 0
            for file in results:
                size = size + 1
                file = file.split('.')[0] # 9ford_ahcm_kuga20.acp wird zu 9ford_ahcm_kuga20
                print(file, end=' ')
            print("Size: ",size)
        else:
            print("No files found containing the string.")