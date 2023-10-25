from pathlib import Path
from datetime import datetime


def getDirectory():

    global root_path

    while True:
        
        root_path = Path(input("Enter Directory Path: ").replace('"', ""))

        if root_path.is_dir():
            print(f"\n{root_path.name} Direcotry is Identified...\n")
            break
        else:
            print("\nInvalid Directory! Please try again...\n")
            continue


def updatePathList(pathList):
    for filepath in root_path.rglob("*"):
        if filepath.is_file():
            pathList.append(filepath)


def directoryManager(filePath, dirName, logfilePath):

    with logfilePath.open(mode="a") as logfile:
        logfile.write(f"\nOld File Location: \n{filePath}")

    parentname = filePath.parent
    fileName = filePath.name
    if parentname.name != dirName:
        newPath = Path(parentname, dirName, fileName)
        if not Path(parentname / dirName).exists():
            Path.mkdir(parentname / dirName)
            filePath.replace(newPath)
            with logfilePath.open(mode="a") as logfile:
                logfile.write(f"\nNew {dirName} Directory created...\nFile Name: {fileName}\nNew file Location: \n{newPath}\n")
        else:
            filePath.replace(newPath)
            with logfilePath.open(mode="a") as logfile:
                logfile.write(f"\n{fileName} File Moved...\nNew file Location: \n{newPath}\n")
    else:
        with logfilePath.open(mode="a") as logfile:
            logfile.write(f"\nFile did not move to a new directory\n")
    

def main(): 

    pathList = []

    getDirectory()

    updatePathList(pathList)

    logfilePath = Path(root_path, "Log File.txt")
    
    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with logfilePath.open(mode="w") as logfile:
        logfile.write(f"Time: {time} \nDirectory Location: {root_path.name}\n")
 
    for filePath in pathList:
        
        fileExt = filePath.suffix[1:]

        if fileExt == "docx":
            dirName = "Word Documents"
        elif fileExt == "pdf":
            dirName = "PDF Documents"
        elif fileExt == "txt":
            dirName = "Text Documents"
        elif fileExt == "jpg" or fileExt == "png" or fileExt == "webp" or fileExt == "jpeg":
            dirName = "Image Files"
        elif fileExt == "pptx":
            dirName = "Powerpoint Files"
        elif fileExt == "xlsx" or fileExt == "xls":
            dirName = "Excel Documents"
        elif fileExt == "mp4" or fileExt == "mkv" or fileExt == "webm" or fileExt == "avi" or fileExt == "m4v" or fileExt == "m4p":
            dirName = "Video Files"
        elif fileExt == "mp3":
            dirName = "Audio Files"
        elif fileExt == "zip" or fileExt == "rar":
            dirName = "Zip Files"
        elif fileExt == "exe":
            dirName = "Executable Package"
        else:
            dirName = "Other Files"
        
        directoryManager(filePath, dirName, logfilePath)

        print("Files organized...")

main()