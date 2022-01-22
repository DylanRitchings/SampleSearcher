#!/usr/bin/env python

import os
import shutil

newDir = "/NewSamples"
oldDir = "/OldSamples"
startDirectory = os.getcwd()
searchWord = ""
wordDict = {"kick": "/kick/", "snare": "/snare/", "hat": "/hats/"}


def fileExists(fPath):
    count = 1
    while True:
        if os.path.exists(fPath):
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


def checkFile(fPath):
    for word, newDir in wordDict.items():
        if word in fPath.lower():
            moveFile(fPath, startDirectory + newDir)


def folderOrFile(fPath):
    if os.path.isdir(fPath):
        folderLoop(fPath)
    elif os.path.isfile(fPath):
        checkFile(fPath)


def folderLoop(dirPath):
    for filename in os.listdir(dirPath):
        folderOrFile(dirPath + "/" + filename)


def main():
    folderLoop(startDirectory + oldDir)


if __name__ == "__main__":
    main()
