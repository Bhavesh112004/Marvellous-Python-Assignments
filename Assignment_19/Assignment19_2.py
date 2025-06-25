import os

def DirectoryFileSearch(Directory_name, Extension1, Extension2):

    flag = os.path.isabs(Directory_name)

    if (flag == False):
        directory_name = os.path.abspath(Directory_name)

    flag = os.path.exists(Directory_name)

    if (flag == False):
        print("Path is Invalid")
        exit()

    flag = os.path.isdir(Directory_name)

    if (flag == False):
        print("The path is valid but the target is not the directory")
        exit()

    renamed_files = []

    for FolderName, SubFolders, FileNames in os.walk(Directory_name):
        for fname in FileNames:
            if (fname.endswith(Extension1)):
                old_path = os.path.join(FolderName, fname)
                Root, _ = os.path.splitext(old_path)
                new_path = Root + Extension2
                os.rename(old_path, new_path)
                renamed_files.append(os.path.basename(new_path))

    return renamed_files

def main():

    directory_name = input()
    first_extension = input()
    second_extension = input()

    renamed_files = DirectoryFileSearch(directory_name,first_extension,second_extension)
    

if __name__ == "__main__":
    main()