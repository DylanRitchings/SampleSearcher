#!/usr/bin/env python

import os

directory = ""
searchWord = ""
newFolder = ""


def main():
    for filename in os.listdir(directory):
        folderOrFile(filename)

if __name__ == "__main__":
    main()

 def folderOrFile(fPath):
     if os.path.isdir(fPath):
         print ("cd")
     elif os.path.isfile(fPath):
         print ("checkname")

def moveFile(fPath):
    print("move")
