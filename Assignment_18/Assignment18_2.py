import os

def ReadFileContent(directory_name, file_name):

    flag = os.path.isabs(directory_name)

    if (flag == False):
        directory_name = os.path.abspath(directory_name)

    flag = os.path.exists(directory_name)

    if (flag == False):
        print("The path is not valid")
        exit()

    flag = os.path.isdir(directory_name)

    if (flag == False):
        print("The path is valid but target is not the directory")
        exit()

    for FolderName,Subfolders,FileNames in os.walk(directory_name):
        for fname in FileNames:
            if (fname == file_name):
                file_path = os.path.join(FolderName, fname)
                Fobj = open(file_path,"r")
                data = Fobj.read()
                print(data)
                break
    
def main():

    FileName = input()
    ReadFileContent("Sample",FileName)

if __name__ == "__main__":
    main()