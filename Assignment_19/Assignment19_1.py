import os

def DirectoryFileSearch(directory_name, extension):

    flag = os.path.isabs(directory_name)

    if (flag == False):
        directory_name = os.path.abspath(directory_name)

    flag = os.path.exists(directory_name)

    if (flag == False):
        print("Path is Invalid")
        exit()

    flag = os.path.isdir(directory_name)

    if (flag == False):
        print("The path is valid but the target is not the directory")
        exit()

    for FolderName, SubFolders, FileNames in os.walk(directory_name):
        for fname in FileNames:
            if (fname.endswith(".txt")):
                print(fname)


def main():

    DirectoryName = input()
    Extension = input()

    DirectoryFileSearch(DirectoryName, Extension)

if __name__ == "__main__":
    main()