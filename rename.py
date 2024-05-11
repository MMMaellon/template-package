import os

rootPath = os.path.dirname(os.path.abspath(__file__))
oldLowerCaseName = "lower-case-name"
oldUpperCaseName = "STARDENBURDENHARDENBART"

print("renaming all files in: " + rootPath)

lowerCaseName = " "

while lowerCaseName.count(" ") > 0:
    lowerCaseName = input("lower-case-name: ").lower()
upperCaseName = input("Upper Case Name: ")

confirm = ""
while len(confirm) <= 0:
    confirm = input("confirm? [y/n]: ")

if confirm != "y":
    print("cancelling")
    exit()

dryRun = False


def renameFolders(root, oldString, newString):
    for _, dirs, _ in os.walk(root):
        for dir in dirs:
            if dir.count(oldString) > 0:
                path = os.path.relpath(dir, root)
                path = os.path.abspath(path)
                newPath = os.path.relpath(dir.replace(oldString, newString), root)
                newPath = os.path.abspath(newPath)
                if dryRun:
                    print(newPath)
                else:
                    os.rename(path, newPath)  # rename your file


def renameFilenames(root, oldString, newString):
    for subdir, _, files in os.walk(root):
        for filename in files:
            if filename.find(oldString) > 0:
                subdirectoryPath = os.path.relpath(
                    subdir, root
                )  # get the path to your subdirectory
                filePath = os.path.join(
                    subdirectoryPath, filename
                )  # get the path to your file
                filePath = os.path.abspath(filePath)
                newFileName = filename.replace(
                    oldString, newString
                )  # create the new name
                newFilePath = os.path.join(
                    subdirectoryPath, newFileName
                )  # get the path to your file
                newFilePath = os.path.abspath(newFilePath)
                if dryRun:
                    print(newFileName)
                else:
                    os.rename(filePath, newFilePath)  # rename your file


def renameInFilenames(root, oldString, newString):
    for subdir, _, files in os.walk(root):
        for filename in files:
            subdirectoryPath = os.path.relpath(
                subdir, root
            )  # get the path to your subdirectory
            filePath = os.path.join(
                subdirectoryPath, filename
            )  # get the path to your file

            filePath = os.path.abspath(filePath)

            # Read in the file
            with open(filePath, "r") as file:
                try:
                    filedata = file.read()
                except:
                    continue
            if filedata.count(oldString) <= 0:
                continue
            filedata = filedata.replace(oldString, newString)
            if dryRun:
                for line in filedata.splitlines():
                    print(line)
                    continue
            else:
                with open(filePath, "w") as outfile:
                    outfile.write(filedata)


roots = [os.path.join(rootPath, "Packages"), os.path.join(rootPath, ".github")]

for root in roots:
    print("Renaming Folders: ")
    renameFolders(root, oldLowerCaseName, lowerCaseName)
    print("Renaming Files: ")
    renameFilenames(rootPath, oldLowerCaseName, lowerCaseName)
    print("Renaming Inside Files: ")
    renameInFilenames(rootPath, oldLowerCaseName, lowerCaseName)
    renameInFilenames(rootPath, oldUpperCaseName, upperCaseName)
