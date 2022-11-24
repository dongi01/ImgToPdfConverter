# modules
import os
import platform
from PIL import Image

# define folder separator for different OSs
WIN_FOLDER_SEPARATOR = "\\"
OSX_LNX_FOLDER_SEPARATOR = "/"

START_PATH = os.getcwd()

# sets right folder separator based on the user's os
systemOS = platform.system()
if (systemOS == "Windows"):
    FOLDER_SEPARATOR = WIN_FOLDER_SEPARATOR
elif (systemOS == "Linux" or systemOS == "Darwin"):
    FOLDER_SEPARATOR = OSX_LNX_FOLDER_SEPARATOR
else:
    print("OS not recognized")
    input("Press enter to close")
    exit()

# creates the complete Images folder path
source_dir = START_PATH + FOLDER_SEPARATOR + 'Images' + FOLDER_SEPARATOR

print("Make sure to have Images folder in the same folder of this program")

print("Would you like to delete all the images in the Images folder after conversion?(yes/no)")
deleteImages = input()

# checks for input chois about deleating img files after conversion
while(1):
    if (deleteImages.upper() == "YES"):
        print("This program is going to delete all images in the Images folder!")
        break
    elif (deleteImages.upper() == "NO"):
        print("This program is NOT going to delete all images in the Images folder")
        break
    else:
        print("Input not recognized, retry")
        deleteImages = input()

# asks for file name and check for right extension
print("Insert final pdf name: ")
while(1):
    print("Make sure to add .pdf at the end")
    nameFile = input()
    if (nameFile.split('.')[-1] == "pdf" and len(nameFile.split('.')) >= 2):
        break

outFilePath = START_PATH + FOLDER_SEPARATOR + nameFile

# control if Images folder is in the cwd
try:
    simpleFileList = os.listdir(source_dir)
except:
    print("There is not Images folder in this directory")
    input("Press enter to close")
    exit()

# for each file: open, convert and add it to the list
fileList = []
for file in simpleFileList:
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
        image = Image.open(source_dir + file )
        fileList.append(image.convert('RGB'))

# if Images folder is not empty, save the pdf and delete or not the imgs files (based on the user choice)
if (len(fileList) != 0):
    fileList[0].save(outFilePath, save_all=True, append_images=fileList)
    if (deleteImages.upper() == "YES"):
        for file in os.listdir(source_dir):
            if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
                os.remove(source_dir + file)

    print("The pdf is available in the program folder")

else:
    print("Images folder is empty")

# wait for an imput before closing
input("Press enter to close")

