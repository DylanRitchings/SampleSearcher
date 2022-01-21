#!/usr/bin/env python

import os
import shutil

startDirectory = ""
searchWord = ""
new = ""
wordDict = {'kick': './kick/', 'snare': './snare/'}


def moveFile(fPath, newDir):
    shutil.move(fPath, newDir)

def checkFile(fPath, searchWord):
    for word, newDir in wordDict:
        if word in fPath:
            moveFile(fPath, newDir)

def folderLoop(fPath):
    for filename in os.listdir(fpath):
        folderOrFile(fPath)

def folderOrFile(fPath):
     if os.path.isdir(fPath):
         folderLoop(fPath)
     elif os.path.isfile(fPath):
         checkFileLoop(fPath, searchWord)

def main():
    folderLoop(startDirectory)

if __name__ == "__main__":
    main()
