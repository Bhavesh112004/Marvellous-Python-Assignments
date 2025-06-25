import os
import shutil

def DirectoryFileSearch(SourceDirectory, DestinationDirectory):

    flag = os.path.isabs(SourceDirectory)

    if (flag == False):
        SourceDirectory = os.path.abspath(SourceDirectory)

    flag = os.path.exists(SourceDirectory)

    if (flag == False):
        print("Path is Invalid")
        exit()

    flag = os.path.isdir(SourceDirectory)

    if (flag == False):
        print("The path is valid but the target is not the directory")
        exit()

    flag = os.path.exists(DestinationDirectory)

    if (flag == False):
        os.makedirs(DestinationDirectory)

    

    copied_files = []

    for FolderName, SubFolders, FileNames in os.walk(SourceDirectory):
        for fname in FileNames:
            source_path = os.path.join(FolderName, fname)
            destination_path = os.path.join(DestinationDirectory, fname)
            shutil.copy2(source_path, destination_path)
            copied_files.append(fname)

    return copied_files

def main():

    source_directory = input()
    destination_directory = input()

    copied_files = DirectoryFileSearch(source_directory,destination_directory)
    

if __name__ == "__main__":
    main()