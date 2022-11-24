# modules
import os
import sys
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
    print("error: os not recognized")
    exit()

# creates the complete Images folder path
source_dir = START_PATH + FOLDER_SEPARATOR + 'Images' + FOLDER_SEPARATOR

if (len(sys.argv) != 3):
    print("error: use 'python3 imgTOpdfCL.py [rm/notrm] [namefile]'")
    exit()

deleteImages = sys.argv[1]
# checks for input chois about deleating img files after conversion
if (deleteImages.upper() != "RM" and deleteImages.upper() != "NOTRM"):
    print("Input not recognized")
    exit()

nameFile = sys.argv[2]
outFilePath = START_PATH + FOLDER_SEPARATOR + nameFile + ".pdf"

# control if Images folder is in the cwd
try:
    simpleFileList = os.listdir(source_dir)
except:
    print("error: Images folder is not in this directory")
    exit()

# for each file: open, convert and add it to the list
fileList = []
for file in simpleFileList:
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
        try:
            image = Image.open(source_dir + file )
        except:
            print("error: unrecognized image")
            exit()
        
        fileList.append(image.convert('RGB'))

tmpList = []
for i in range(1, len(fileList)):
    tmpList.append(fileList[i])

# if Images folder is not empty, save the pdf and delete or not the imgs files (based on the user choice)
if (len(fileList) != 0):
    fileList[0].save(outFilePath, save_all=True, append_images=tmpList)
    if (deleteImages.upper() == "RM"):
        for file in os.listdir(source_dir):
            if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
                os.remove(source_dir + file)

    print("The pdf is available in the program folder")

else:
    print("Images folder is empty")
