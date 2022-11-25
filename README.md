# imgTOpdfConverter

## Versions
* imgTOpdfConsole.py
* imgTOpdfCL.py
* imgTOpdfConsole.exe

## Requirements
### imgTOpdfConsole.py & imgTOpdfCL.py
You have to install **python3** and **Pillow** python library.  
To install python3 follow the procedure on the official [python website](https://www.python.org/downloads/).  
To install Pillow library open your terminal and digit
```bash  
pip3 install pillow
```  
For every problem in this last installation follow the official [Pillow documentation](https://pillow.readthedocs.io/en/stable/installation.html)

### imgTOpdfConsole.exe
This Windows executable file should run on Windows 10 and later without any problem. 
If this doesn't work, use the .py version

## Usage
To make these programs work you have to place the .py/.exe file in a folder where an **Images** directory is present. Save your images in this folder and follow next instructions to run the application

### imgTOpdfConsole.exe
Probably yuor Windows os is going to warning you that this program is not safe but you can ignore it... Your pc will be perfectly fine : )  
To run it just double click on the icon and a new window will appear. It will ask you if you want to delete or not the images in the Images folder and the final pdf name.

### imgTOpdfConsole.py
To run this program open your terminal and navigate in the folder where you have the .py file and the Images folder. You can also open the terminal directly in the folder by right click on it and selecting 'open in terminal'.
Then launch this command:  
```bash
python3 ./imgTOpdfConsole.py
```   
At this point the instruction will be shown after the command in the terminal.

### imgTOpdfCL.py
This version is for someone who want a faster experience.  
Simply run 
```bash
python3 ./imgTOpdfCL.py [rem/notrem] [namefile]
```  
Use **rem** to remove the images in the folder after conversion or **notrem** to mantain them.  
Finally add the name you want to give to the final file (whitout extension, it will automatically generate a .pdf)