import os
from os.path import join
import shutil
import tkinter as tk
import datetime
from tkinter import BooleanVar, Variable, filedialog
from tkinter.constants import COMMAND, W
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from typing import Container, Text
from PIL import Image, ImageTk
from pathlib import Path
from tkcalendar import Calendar, DateEntry
import tkcalendar

############################################




# hidden folders?
# add date range

# tkinter stuff
root = tk.Tk()

# window name
root.title('FileShift by Mobenator APPS')

# window frame

frame0=tk.Frame(
    root,
    width=1000,
    #highlightbackground='black',
    #highlightthickness=3
)
frame0.grid(
    row=0,
    rowspan=10,
    column=0,
    columnspan=5,
    padx=10,
    pady=10
)

# logo frame
frame1=tk.Frame(
    frame0, 
    height=600, 
    #highlightbackground='red',
    #highlightthickness=3
)
frame1.grid(
    row=0,
    column=0,
    columnspan=5,
    #padx=20,
    #pady=20
)

# set app canvas
canvas = tk.Canvas(root, width=1000, height=600)
#canvas.grid(columnspan=6, rowspan=3)

# Mobenator APPS filepath
currentPath = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

imgPath = join(currentPath, 'Mobenator_APPS_headline.png')
print(imgPath)
  
# logo
logo = Image.open(imgPath)
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(frame1, image=logo)
logo_label.image = logo
logo_label.grid(
    column=0, 
    row=0, 
    columnspan= 5
)

# disclaimer
disclaimerPath = join(currentPath, 'software_disclaimer_program.txt')
disclaimerFile = open(disclaimerPath, "r")
disclaimer = disclaimerFile.read()
print(disclaimer)

# global variables
parentFolder = ''
newFolder = ''
joinedLists = []
fileSize = ''
minFileSizeBytes = 0
maxFileSizeBytes = 0

# create a list of common image file types
imageFileTypes = ['.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.png', '.gif', '.webp', '.tiff', '.tif', '.psd', '.raw', '.arw', '.cr2', '.nrw',
                '.k25', '.bmp', '.dib', '.heif', '.heic', '.ind', '.indd', '.indt', '.jp2', '.j2k', '.jpf', '.jpx', '.jpm', '.mj2', '.svg', '.svgz', '.ai', '.eps']

# create a list of common video file types
videoFileTypes = ['.webm', '.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.ogg',
                '.mp4', '.m4p', '.m4v', '.avi', '.wmv', '.mov', '.qt', '.flv', '.swf', '.avchd']

# create a list of common text file types
textFileTypes = ['.doc','.docx','.odt','.pdf','.rft','.tex','.txt','.wpd']

# create a list of common spreadsheet file types
sheetFileTypes = ['.ods','.xls','.xlsm','.xlsx']

# create a list of common presentation file types
presFileTypes = ['.key','.odp','.pps','.ppt','.pptx']

# create a list of common email file types
emailFileTypes = ['.email','.eml','.emlx','.msg','.oft','.ost','.pst','.vcf']

# create a list of common database file types
dbFileTypes = ['.csv','.dat','.db','.dbf','.log','.mdb','.sav','.sql','.tar','.xml']

# create a list of common compressed file types
compFileTypes = ['.7z','.arj','.deb','.pkg','.rar','.rpm','.tar.gz','.z','.zip']

# create a list of common disc medida file types
discFileTypes = ['.bin','.dmg','.iso','.toast','.vcd']

# create a list of common programming file types
progFileTypes = ['.c','.cgi','.pl','.class','.cpp','.cs','.h','.java','.php','.py','.sh','.swift','.vb']

# custom file types
customFileTypes = []

# create a list of file sizes
fileSizeList = ['Bytes','Kilobytes','Megabytes','Gigabytes']

# get parent directory

def set_parent_directory():
    browse_parent_text.set("loading...")
    folder = filedialog.askdirectory()
    global parentFolder
    parentFolder = folder
    if folder:
        print(folder + " was successfully loaded.")
        browse_parent_text.set("Move files from: " + folder)
    else:
        browse_parent_text.set("Browse")


# get new directory
def set_new_directory():
    browse_new_text.set("loading...")
    folder = filedialog.askdirectory()
    global newFolder
    newFolder = folder
    if folder:
        print(folder + " was successfully loaded.")
        browse_new_text.set("Move files to: " + folder)
    else:
        browse_new_text.set("Browse")
def printVal(boxVal):
    print(boxVal)

# join checked file types


def joinLists():
    list = []

    # add file type groups
    if imgCheckVal.get() == 1:
        for i in imageFileTypes:
            list.append(i)
    if vidCheckVal.get() == 1:
        for i in videoFileTypes:
            list.append(i)
    if textCheckVal.get() == 1:
        for i in textFileTypes:
          list.append(i)
    if sheetCheckVal.get() == 1:
        for i in sheetFileTypes:
         list.append(i)
    if presCheckVal.get() == 1:
        for i in presFileTypes:
         list.append(i)
    if emailCheckVal.get() == 1:
        for i in emailFileTypes:
            list.append(i)
    if dbCheckVal.get() == 1:
        for i in dbFileTypes:
         list.append(i)
    if compCheckVal.get() == 1:
        for i in compFileTypes:
            list.append(i)
    if discCheckVal.get() == 1:
        for i in discFileTypes:
            list.append(i)
    if progCheckVal.get() == 1:
        for i in progFileTypes:
            list.append(i)
    # add custom file types
    for i in customFileTypes:
        list.append(i)

    global joinedLists
    joinedLists = list
    return list

# checks if the input is an number

def isInt(input): 
    
    if input.isdigit(): 
        return True              
    elif input == "": 
        return True
    else: 
        return False

def isStr(input):

    if input.isalpha():
        return True
    elif input == "":
        return True
    else:
        return False

def isAlphaNumeric(input):
    return input.isalnum()
    
# file directories frame
frame2=tk.Frame(
    frame0, 
    #width=800,
    #highlightbackground='blue',
    #highlightthickness=3
)
frame2.grid(
    row=1,
    column=0,
    columnspan=5,
    padx=10,
    pady=(20,0)
)

# set the location of the files

# parent folder instructions
from_instructions = tk.Label(
    frame2, 
    text="Select the folder you want to move files from.",
    #width=224
)
from_instructions.grid(
    column=0, 
    row=0,
    #columnspan=2,
    pady=10,
    sticky=W
)

# browse parent button
browse_parent_text = tk.StringVar()
browse_parent_button = tk.Button(
    frame2, 
    textvariable=browse_parent_text, 
    command=lambda: set_parent_directory(), 
    bg="#147b90", 
    fg="white", 
    height=1, 
    width=100
)
printVal(parentFolder)
browse_parent_text.set("Browse")
browse_parent_button.grid(
    column=1,
    row=0,
    columnspan=2,
    padx=10,
    pady=10
)

# new folder instructions
from_instructions = tk.Label(
    frame2, 
    text="Select the folder you want to move the files to."
)
from_instructions.grid(
    column=0, 
    row=1,
    columnspan=2,
    pady=10,
    sticky=W
)

# browse new button
browse_new_text = tk.StringVar()
browse_new_button = tk.Button(
    frame2, 
    textvariable=browse_new_text, 
    command=lambda: set_new_directory(), 
    bg="#147b90", 
    fg="white", 
    height=1, 
    width=100
)
printVal(newFolder)
browse_new_text.set("Browse")
browse_new_button.grid(
    column=1,
    row=1,
    columnspan=2,
    padx=10,
    pady=0
)

#end set the location of the files

# include subfolders checkbox
subfolderCheckVal = tk.IntVar(value=0)
subfolders_button = tk.Checkbutton(
    frame2, 
    text='Include subfolders?', 
    variable=subfolderCheckVal, 
    onvalue=1, 
    offvalue=0
)
subfolders_button.grid(
    column=3, 
    row=0, 
    pady=10
)

# file types frame
frame3=tk.Frame(
    frame0, 
    #width=320,
    highlightbackground='green',
    highlightthickness=3
)
frame3.grid(
    row=2,
    column=0,
    columnspan=2,
    padx=10,
    pady=(20,10),
    sticky=W
)

# file types instructions
fileTypesInstructions = tk.Label(
    frame3, 
    text="Select at least one file type group."
)
fileTypesInstructions.grid(
    column=0,
    row=0,
    padx=(0,10),
    pady=10,
    sticky=tk.W
)

# file types

allCheckVal = tk.IntVar()
allCheckBox = tk.Checkbutton(
    frame3, 
    text='All files', 
    variable=allCheckVal, 
    onvalue=1, 
    offvalue=0
)
allCheckBox.grid(
    column=1, 
    row=0, 
    pady=10,
    sticky=tk.W
)
allCheckBox.pack

# custom file types

addCustomFileTypeInstructions = tk.Label(
    frame3, 
    text="Add a a file type manually."
)
addCustomFileTypeInstructions.grid(
    column=2,
    row=0,
    columnspan=2,
    padx=(0,10),
    pady=10,
    sticky=tk.W
)

# custom file type entry
customFileTypeInput = tk.Entry(frame3)
customFileTypeInput.grid(
    column=2, 
    row=2,
    padx=10,
    pady=0,
    sticky=tk.W
)
reg = frame3.register(isAlphaNumeric) 

customFileTypeInput.config(
    validate ="key",  
    validatecommand =(
        reg, 
        '%P'
    )
)

# add custom file type button

addFileTypeButton = tk.Button(
    frame3, 
    text='Add',
    command=lambda: addCustomFileType(customFileTypeInput.get())
)
addFileTypeButton.grid(
    column=3, 
    row=2,
    padx=0, 
    pady=0,
    sticky=tk.E
)
addFileTypeButton.pack

# clear custom file types button

clearFileTypeButton = tk.Button(
    frame3,
    text='Clear all.',
    command=lambda: clearCustomFileType()
)
clearFileTypeButton.grid(
    column=3,
    row=3,
    padx=0,
    pady=0,
    sticky=tk.E
)

def addCustomFileType(input):
    withDot = '.' + str(input)
    customFileTypes.append(withDot)
    print(customFileTypes)
    updateShowCustomFileTypesVar()

def clearCustomFileType():
    customFileTypes.clear()
    print(customFileTypes)
    updateShowCustomFileTypesVar()

# list of file types added box
showCustomFileTypesVar = tk.StringVar('')
showCustomFileTypesLabel = tk.Label(
    frame3,
    textvariable=showCustomFileTypesVar
)
showCustomFileTypesLabel.grid(
    column=2,
    row=3,
    rowspan=4,
    sticky=tk.NW
)

def updateShowCustomFileTypesVar():
    s = ''
    c = 0
    for i in customFileTypes:
        s = s + ' ' + i
        c = c + 1
        if c % 5 == 0:
            s = s + '\n'
    showCustomFileTypesVar.set(s)

def updateShiftFilesButton():
    shiftFilesText.set

# submit file types
shiftFilesText = tk.StringVar()
shiftFilesText.set('FileShift')
print(shiftFilesText)
shiftFiles = tk.Button(
    frame0, 
    textvariable=shiftFilesText,
    command=lambda: moveFilesHandler()
)
shiftFiles.grid(
    column=4, 
    row=2,
    padx=10, 
    pady=10,
    sticky=tk.SE
)
shiftFiles.pack

def conformation():
    conformationYesNo = messagebox.askquestion('FileShift Confirmation','FileShift will move files from the directory/s to another directory.\n\nThis cannot be undone. Do you want to proceed?')
    return conformationYesNo

def readDisclaimer():
    disclaimerQuestion = 'Have you read the disclaimer?\n\n' + disclaimer
    disclaimerYesNo = messagebox.askquestion('Disclaimer', disclaimerQuestion)
    return disclaimerYesNo

def subFolders(directory):
    foldersArray = []
    for root, dirs, files in os.walk(directory):
        for d in dirs:
            foldersArray.append(join(root,d))
    return foldersArray

# create a list of file names

def getFileNames(folder):
    print('getFileNames')
    print('folder: ' + folder)
    filesArray = [f.name for f in os.scandir(folder) if f.is_file()]
    return filesArray

def fileSizeInBytes(size, byteSize):
    print('fileSizeInBytes')
    if byteSize == 'Bytes':
        return size
    elif byteSize == 'Kilobytes':
        return size * 1024
    elif byteSize == 'Megabytes':
        return size * 1024 * 1024
    elif byteSize == 'Gigabytes':
        return size * 1024 * 1024 * 1024
    else:
        return 0

def convertUserSizesToBytes():
    print('convertUserSizesToBytes')
    if useSizeVal.get() == 1:
        return
    else:
        byteSize = sizeMenuVal.get()
        minSize = int(minSizeVal.get())
        maxSize = int(maxSizeVal.get())

        minSize = fileSizeInBytes(minSize, byteSize)
        global minFileSizeBytes
        minFileSizeBytes = minSize
        
        maxSize = fileSizeInBytes(maxSize, byteSize)
        global maxFileSizeBytes
        maxFileSizeBytes = maxSize

def moveFilesHandler():
    print('moveFiles')
    if folderCheck() == False:
        return
    elif readDisclaimer() == 'No':
        return
    elif conformation() == 'No':
        return
    else:

        shiftFilesText.set('Shifting...')

        joinLists()

        convertUserSizesToBytes()
        
        moveFiles()

        shiftFilesText.set('Finished!')
        

def moveFiles():
    # move files in parent folder
    files = getFileNames(parentFolder)
    for file in files:
        moveFile(
            file, 
            parentFolder
        )

    # move files in subfolders
    if subfolderCheckVal.get() == 1:
    
        #folders = getFolderNames()

        folders = subFolders(parentFolder)

        for folder in folders:
            print('folder: ' + folder)
            files = getFileNames(folder)
            for file in files:
                moveFile(
                    file, 
                    folder
                )

def folderCheck():
    if parentFolder == '' or parentFolder == ' ':
        shiftFilesText.set('Parent folder is blank.')
        return False
    elif newFolder == '' or newFolder == ' ':
        shiftFilesText.set('New folder is blank.')
        return False
    elif parentFolder == newFolder:
        shiftFilesText.set('Parent folder cannot equal new folder.')
        return False
    else:
        return True

def moveFile(fileName, currentFilePath):
    print('moveFile')
    currentFullFilePath = os.path.join(currentFilePath, fileName)
    if checks(currentFullFilePath) == True:
        
        timeStamp(currentFullFilePath)

        newFullFilePath = os.path.join(newFolder, fileName)

        shutil.move(currentFullFilePath, newFullFilePath)

# checks if the file size is between the two size parameters
def fileSizeCheck(fullFilePath):
    print('fileSizeCheck')
    # exit if all sizes are included
    if useSizeVal.get() == 1:
        return True
    
    # get the file size in bytes
    fileSizeB = os.path.getsize(fullFilePath)
    
    # check if the file size is within bounds
    if fileSizeB >= minFileSizeBytes and fileSizeB <= maxFileSizeBytes:
        return True
    else:
        return False

# checks if file type is in the list of file types
def fileTypeCheck(fileType):
    print('fileTypeCheck')
    if fileType in joinedLists or allCheckVal.get() == 1:
        return True
    else:
        return False

def checks(fullFilePath):
    print('checks')
    # check if the file size is within bounds
    if fileSizeCheck(fullFilePath) == True:
        # check if the file type is in the target array
        if fileTypeCheck(Path(fullFilePath).suffix) == True:
            return True
        else:
            return False
    else:
        return False

def fileStats(fullFilePath):
    fname = Path(fullFilePath)

    

    print(fname.stat())

def timeStamp(filePath):

    p = Path(filePath)

    stamp = datetime.datetime.fromtimestamp(p.stat().st_ctime)

    #print("last modified: %s" % os.path.time.ctime(os.path.getmtime(filePath)))

    print(stamp)

    return stamp

def updateDateSel():
    cd = dateDialog()
    print(cd.result)
    
    dateSelVar.set(cd.result)

imgCheckVal = tk.IntVar()   
imgCheckBox = tk.Checkbutton(
    frame3, 
    text='Images', 
    variable=imgCheckVal, 
    onvalue=1, 
    offvalue=0
)
imgCheckBox.grid(
    column=0, 
    row=2, 
    pady=0,
    sticky=tk.W
)
imgCheckBox.pack

vidCheckVal = tk.IntVar()
vidCheckBox = tk.Checkbutton(
    frame3, 
    text='Videos', 
    variable=vidCheckVal, 
    onvalue=1, 
    offvalue=0
)
vidCheckBox.grid(
    column=1, 
    row=2, 
    pady=0,
    sticky=tk.W
)
vidCheckBox.pack

textCheckVal = tk.IntVar()
textCheckBox = tk.Checkbutton(
    frame3, 
    text='Texts', 
    variable=textCheckVal, 
    onvalue=1, 
    offvalue=0
)
textCheckBox.grid(
    column=0, 
    row=3, 
    pady=0,
    sticky=tk.W
)
textCheckBox.pack

sheetCheckVal = tk.IntVar()
sheetCheckBox = tk.Checkbutton(
    frame3, 
    text='Spreadsheets', 
    variable=sheetCheckVal, 
    onvalue=1, 
    offvalue=0
)
sheetCheckBox.grid(
    column=1, 
    row=3, 
    pady=0,
    sticky=tk.W
)
sheetCheckBox.pack

presCheckVal = tk.IntVar()
presCheckBox = tk.Checkbutton(
    frame3, 
    text='Presentations', 
    variable=presCheckVal, 
    onvalue=1, 
    offvalue=0
)
presCheckBox.grid(
    column=0, 
    row=4, 
    pady=0,
    sticky=tk.W
)
presCheckBox.pack

emailCheckVal = tk.IntVar()
emailCheckBox = tk.Checkbutton(
    frame3, 
    text='Emails', 
    variable=emailCheckVal, 
    onvalue=1, 
    offvalue=0
)
emailCheckBox.grid(
    column=1, 
    row=4, 
    pady=0,
    sticky=tk.W
)
emailCheckBox.pack

dbCheckVal = tk.IntVar()
dbCheckBox = tk.Checkbutton(
    frame3, 
    text='Databases', 
    variable=dbCheckVal, 
    onvalue=1, 
    offvalue=0
)
dbCheckBox.grid(
    column=0, 
    row=5, 
    pady=0,
    sticky=tk.W
)
dbCheckBox.pack

compCheckVal = tk.IntVar()
compCheckBox = tk.Checkbutton(
    frame3, 
    text='Compressed/zipped', 
    variable=compCheckVal, 
    onvalue=1, 
    offvalue=0
)
compCheckBox.grid(
    column=1, 
    row=5, 
    pady=0,
    sticky=tk.W
)
compCheckBox.pack

discCheckVal = tk.IntVar()
discCheckBox = tk.Checkbutton(
    frame3, 
    text='Disc images', 
    variable=discCheckVal, 
    onvalue=1, 
    offvalue=0
)
discCheckBox.grid(
    column=0, 
    row=6, 
    pady=0,
    sticky=tk.W
)
discCheckBox.pack

progCheckVal = tk.IntVar()
progCheckBox = tk.Checkbutton(
    frame3, 
    text='Programming/scripts', 
    variable=progCheckVal, 
    onvalue=1, 
    offvalue=0
)
progCheckBox.grid(
    column=1, 
    row=6, 
    pady=0,
    sticky=tk.W
)
progCheckBox.pack

# file size frame
frame4=tk.Frame(
    frame0, 
    #width=320,
    highlightbackground='yellow',
    highlightthickness=3
)
frame4.grid(
    row=2,
    column=2,
    #columnspan=2,
    padx=(20,0),
    pady=(20,0),
    sticky=tk.NW
)

# size based move files
useSizeVal = tk.IntVar()
useSizeBox = tk.Checkbutton(
    frame4, 
    text='All files sizes?', 
    variable=useSizeVal, 
    onvalue=1, 
    offvalue=0
)
useSizeBox.grid(
    column=0,
    row=0,
    padx=(0,10),
    pady=(10,0),
    sticky=W
)
useSizeBox.pack

# size instructions
sizeInstructions = tk.Label(
    frame4, 
    text='Or, files between two sizes.', 
)
sizeInstructions.grid(
    column=0,
    row=1, 
    pady=(10,0),
    sticky=W
)
sizeInstructions.pack

# file size menu instructions
sizeMenuInstructions = tk.Label(
    frame4, 
    text='File size Category.'
)
sizeMenuInstructions.grid(
    column=0, 
    row=2, 
    pady=(10,0),
    sticky=W
)
sizeMenuInstructions.pack

# file sizes
sizeMenuVal = tk.StringVar()
sizeMenuVal.set(fileSizeList[0])

sizeMenu = tk.OptionMenu(
    frame4, 
    sizeMenuVal, 
    *fileSizeList,
)
sizeMenu.grid(
    column=1, 
    row=2,
    padx=10,
    pady=(10,0),
    sticky=W
)
sizeMenu.pack

# minimum file size
minFileSizeInstructions = tk.Label(
    frame4, text="Enter the minimum file size.")
minFileSizeInstructions.grid(
    column=0, 
    row=3, 
    pady=(5,0)
)

# minimum file size
minSizeVal = tk.Entry(frame4)
minSizeVal.grid(
    column=1, 
    row=3,
    padx=10,
    pady=0
)
reg = frame4.register(isInt) 

minSizeVal.config(
    validate ="key",  
    validatecommand =(
        reg, 
        '%P'
    )
)

# maximum file size
maxFileSizeInstructions = tk.Label(
    frame4, 
    text="Enter the maximum file size."
)
maxFileSizeInstructions.grid(
    column=0, 
    row=4,
    pady=(5,0)
)

# maximum file size
maxSizeVal = tk.Entry(frame4)
maxSizeVal.grid(
    column=1, 
    row=4,
    padx=10,
    pady=0
)
reg = frame4.register(isInt) 

maxSizeVal.config(
    validate ="key",  
    validatecommand =(
        reg, 
        '%P'
    )
)

# file dates frame
frame5=tk.Frame(
    frame0, 
    #width=320,
    highlightbackground='purple',
    highlightthickness=3
)
frame5.grid(
    row=2,
    column=3,
    #columnspan=2,
    padx=(20,0),
    pady=(20,0),
    sticky=tk.NW
)

def dateDialog():
    top = tk.Toplevel(root)

    tk.Label(top, text='Choose date').pack(padx=10, pady=10)

    cal = DateEntry(top, width=12, background='darkblue',
                    foreground='white', borderwidth=2)
    cal.pack(padx=10, pady=10)

    #dateSelVar.set(cal.get_date)

    print(cal.get_date())

#dateSelVar = 'Date from'
#dateSel = tk.Button(
    #frame5,
    #textvariable=dateSelVar,
    #command=dateFromDiaglog
#)
#dateSel.grid(
#    row=0,
#    column=0
#)
#dateSel.pack




root.mainloop()

############################################
def new_checkbox(self, name, colPos, rowPos):
    button = self.buttons
    parent = self.parent

    button[name] = {}
    button[name]["name"] = name
    button[name]["colPos"] = colPos
    button[name]["rowPos"] = rowPos
    button[name]["button"] = tk.Checkbutton(parent, text=name)

    button[name]["button"].grid(column=colPos, row=rowPos)

def show_buttons(self, name):
    for key, value in self.buttons[name].items():
        print(f"{key}: {value}")


new_checkbox(root, name="disc", colPos=1, rowPos=8)
show_buttons("disc")