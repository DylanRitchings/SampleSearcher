#!/usr/bin/env python

import os

# import shutil

newDir = "/NewSamples"
oldDir = "/OldSamples"
startDirectory = os.getcwd()
newPath = startDirectory + newDir
wordDict = {
    "kick": "/kick/",
    "snare": "/snare/",
    "hat": "/hats/",
    "crash": "/crash/",
    "tambourine": "/tambourine/",
}
moveCount = 0
memMoved = 0


# fPath needs to be  new file path
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
    os.rename(fPath, newPath)
    global moveCount
    # print(newDir)
    # print(fPath)
    moveCount += 1
    print(moveCount, " files moved", end="\r")


# Checks if file has word from wordDict
# returns new path
def checkFile(fPath):
    for word, newDir in wordDict.items():
        newCompPath = newPath + newDir

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


def main():
    folderLoop(startDirectory + oldDir)


if __name__ == "__main__":
    main()
