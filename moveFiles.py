#!/usr/bin/env python

import os

# import shutil

newDir = "/NewSamples"
oldDir = "/OldSamples"
startDirectory = os.getcwd()
newPath = startDirectory + newDir
wordDict = {
    # Breaks
    "break": "/drums/breaks/",
    "beat": "/drums/breaks/",
    "roll": "/drums/breaks/rolls/",
    "fill": "/drums/breaks/fills/",
    "ride": "/drums/breaks/rides/",
    "hats": "/drums/breaks/hats/",
    "tops": "/drums/breaks/tops/",
    "crescendo": "/drums/breaks/crescendo/",
    # One Shots
    "kick": "/drums/oneshots/kicks/",
    "bell": "/drums/oneshots/bells/",
    "mallet": "/drums/oneshots/mallets/",
    "tom": "/drums/oneshots/toms/",
    "snare": "/drums/oneshots/snares/",
    "hat": "/drums/oneshots/hats/",
    "crash": "/drums/oneshots/crash/",
    "tambourine": "/drums/oneshots/tambourines/",
    "shaker": "/drums/oneshots/shakers/",
    # AFRICAN
    "slit": "/drums/oneshots/African/slits/",
    "burundi": "/drums/oneshots/African/burundi/",
    "log": "/drums/oneshots/African/logs/",
    "udu": "/drums/oneshots/African/Nigerian Udus/",
    "conga": "/drums/oneshots/African/congas/",
    # Other
    "piano": "/piano/",
    "fx": "/FX/",
    "pluck": "/pluck/",
    "pick": "/picking/",
    "horn": "/horn/",
    "arp": "/arps/",
    # "am": "/tuned/",
    # "bm": "/tuned/",
    # "cm": "/tuned/",
    # "dm": "/tuned/",
    # "em": "/tuned/",
    # "fm": "/tuned/",
    # "gm": "/tuned/",
    "#": "/tuned/",
}
moveCount = 0
noMoveCount = 0
memMoved = 0


# Checks if new file with same name already exists
def fileExists(fileName, newDir):
    count = 0
    fPath = newDir + fileName
    newPath = fPath
    while True:
        if os.path.exists(newPath):
            count += 1
            # fPath += 1
        else:
            break
        splitPath = fPath.split(".")
        newPath = splitPath[0] + str(count) + "." + splitPath[1]
    return newPath


def moveFile(fPath, newPath):
    # newFPath = fileExists(fPath)
    # os.rename(fPath, newPath)
    global moveCount
    moveCount += 1
    print(moveCount, " files moved", end="\r")


# Checks if file has word from wordDict
# returns new path
def checkFile(fPath):
    for word, newDir in wordDict.items():
        newCompPath = newPath + newDir

        # Create new folder if it doesn't exist
        if not os.path.exists(newCompPath):
            os.makedirs(newCompPath)

        if word in fPath.lower():
            # aa(fPath, word)
            return newCompPath
            # moveFile(fPath, startDirectory + newDir)
            # break


# def folderOrFile(fPath):
#     if os.path.isdir(fPath):
#         folderLoop(fPath)
#     elif os.path.isfile(fPath):
#         checkFile(fPath)


def folderLoop(dirPath):
    global noMoveCount
    for fileName in os.listdir(dirPath):
        currentFPath = dirPath + "/" + fileName

        # Folder or file
        if os.path.isdir(currentFPath):
            folderLoop(currentFPath)
        elif os.path.isfile(currentFPath):
            newDir = checkFile(currentFPath)
            if newDir is not None:
                # START HERE
                newPath = fileExists(fileName, newDir)
                moveFile(currentFPath, newPath)

            # Print uncaptured file
            else:
                noMoveCount += 1
                print(currentFPath)


def main():
    folderLoop(startDirectory + oldDir)
    print(moveCount, " files moved")
    print(noMoveCount, " files not moved")


if __name__ == "__main__":
    main()
