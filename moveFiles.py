#!/usr/bin/env python

import os
import shutil

newDir = "/NewSamples"
oldDir = "/OldSamples"
startDirectory = os.getcwd()
newPath = startDirectory + newDir
wordDict = {"kick": "/kick/", "snare": "/snare/", "hat": "/hats/"}
moveCount = 0
memMoved = 0


def aa(one, two):
    print("AAAAAAAAAAAAAAAAa")
    print(one)
    print(two)


# fPath needs to be  new file path
def fileExists(fPath):
    count = 1
    while True:
        if os.path.exists(fPath):
            aa(fPath, newDir)
            count += 1
        else:
            False
    if count == 1:
        return fPath
    else:
        splitPath = fPath.split(".")
        return splitPath[0] + count + splitPath[1]


def moveFile(fPath, newDir):
    newFPath = fileExists(fPath)
    shutil.move(newFPath, newDir)
    global moveCount
    print(newDir)
    print(fPath)
    moveCount += 1
    print(moveCount, " files moved", end="\r")


# Checks if file has word from wordDict
# returns new path
def checkFile(fPath):
    for word, newDir in wordDict.items():
        if word in fPath.lower():
            # aa(fPath, word)
            return newPath + newDir
            # moveFile(fPath, startDirectory + newDir)
            # break


# def folderOrFile(fPath):
#     if os.path.isdir(fPath):
#         folderLoop(fPath)
#     elif os.path.isfile(fPath):
#         checkFile(fPath)


def folderLoop(dirPath):
    for filename in os.listdir(dirPath):
        currentFPath = dirPath + "/" + filename

        # Folder or file
        if os.path.isdir(currentFPath):
            folderLoop(currentFPath)
        elif os.path.isfile(currentFPath):
            newDir = checkFile(currentFPath)
            if newDir is not None:
                # START HERE
                moveFile(currentFPath, newPath)


def main():
    folderLoop(startDirectory + oldDir)


if __name__ == "__main__":
    main()
