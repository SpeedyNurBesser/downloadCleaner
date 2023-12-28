import subprocess
import os
from os import listdir

# path of the folder that you want to clean (you might want to go for an input statement?):
FOLDER = 'C:/Users/Ole/Downloads'
# path of your QuickLook (https://apps.microsoft.com/detail/9NV4BS3L1H4S?hl=en-US&gl=US) install:
QUICKLOOK = 'D:\Program Files\QuickLook\QuickLook.exe'

# file types (e.g.: '.mp4' for videos)
# paths of your default directories:
VIDEO_TYPES = ['.mp4', '.mov', '.mkv']
VIDEO = 'C:/Users/Ole/Videos'

PICTURE_TYPES = ['.png','.jpg','.jpeg', '.webp', '.pdn', '.gif']
PICTURE = 'C:/Users/Ole/Pictures'

AUDIO_TYPES = ['.mp3', '.wav']
AUDIO = 'D:/Music Library'

DOCUMENT_TYPES = ['.md', '.doc', '.docx', '.pdf']
DOCUMENT = 'D:/Dokumente'

# open file using QuickLook
def openFile(filename: str):
    return subprocess.Popen([QUICKLOOK, filename])

# get all files of a specific directory
def getFiles(dirpath: str):
    return listdir(dirpath)

# well, deletes the file
def deleteFile(filename: str):
    path = FOLDER + '/' + filename
    os.remove(path)
    print(f"Deleted {filename}")

# moves file to a folder called 'temp' for further processing
def tempFile(filename: str):
    tempFolder = f"{FOLDER}/temp/"
    if not os.path.exists(tempFolder):
        os.makedirs(tempFolder)
    os.replace(f"{FOLDER}/{filename}", f"{tempFolder}{filename}")
    print(f"Moved {filename} to {tempFolder}")

# moves file to default directories: .mp4 -> Videos; .wav -> Music; .png -> Pictures 
def moveFile(filename: str):
    fileExtension = os.path.splitext(filename)[1]
    if fileExtension in VIDEO_TYPES:
        os.replace(f"{FOLDER}/{filename}", f"{VIDEO}/{filename}")
        print(f"Moved {filename} to {VIDEO}")
    
    elif fileExtension in PICTURE_TYPES:
        os.replace(f"{FOLDER}/{filename}", f"{PICTURE}/{filename}")
        print(f"Moved {filename} to {PICTURE}")
    
    elif fileExtension in AUDIO_TYPES:
        os.replace(f"{FOLDER}/{filename}", f"{AUDIO}/{filename}")
        print(f"Moved {filename} to {AUDIO}")
    
    elif fileExtension in DOCUMENT_TYPES:
        os.replace(f"{FOLDER}/{filename}", f"{DOCUMENT}/{filename}")
        print(f"Moved {filename} to {DOCUMENT}")
    
    else:
        print(f"Couldn't find a fitting directory for {filename}; kept file")

# skip file - honestly, it's only an print command
def skipFile(filename: str):
    print(f"Skipped {filename}")


if __name__ == "__main__":
    fileList = getFiles(FOLDER)
    for i in range(0, len(fileList)):
        process = openFile(FOLDER + '/' + fileList[i])
        # input on how to handle the current file
        fileName = fileList[i]
        handleFile = input(f"{fileName} - delete, skip, move, temp, exit (d/s/m/t/e)")

        if handleFile == "d" or handleFile == "D":
            deleteFile(fileName)
        elif handleFile == 's' or handleFile == 'S':
            skipFile(fileName)
        elif handleFile == 'm' or handleFile == 'M':
            moveFile(fileName)
        elif handleFile == 't' or handleFile == 'T':
            tempFile(fileName)
        elif handleFile == 'e' or handleFile == 'E':
            print("Quit.")
            quit()
        else:
            skipFile(fileName)
            
    process.terminate()