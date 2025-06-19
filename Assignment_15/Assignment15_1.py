import os

def CheckFile(directory_name,file_name):

    flag = os.path.isabs(directory_name)

    if (flag == False):
        directory_name = os.path.abspath(directory_name)

    flag = os.path.exists(directory_name)

    if (flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(directory_name)

    if (flag == False):
        print("The path is valid but the target is not the directory")
        exit()

    for FolderName, Subfolders, filenames in os.walk(directory_name):
        for fname in filenames:
            if (fname == file_name):
                print("Present")
                break
            else: 
                pass
                
            

def main():

    print("Enter the name oo directory you want to check : ")
    file_name = input()

    CheckFile("Sample", file_name)


if __name__ == "__main__":
    main()