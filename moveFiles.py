#!/usr/bin/env python

import os

# import shutil

newDir = "/NewSamples"
oldDir = "/OldSamples"
startDirectory = os.getcwd()
newPath = startDirectory + newDir
wordDict = {
    ## Drums
    # Breaks
    "break": "/drums/breaks/",
    "beat": "/drums/breaks/",
    "roll": "/drums/breaks/rolls/",
    "fill": "/drums/breaks/fills/",
    "ride": "/drums/breaks/rides/",
    "hats": "/drums/breaks/hats/",
    "tops": "/drums/breaks/tops/",
    "crescendo": "/drums/breaks/crescendo/",
    "drum loop": "/drums/breaks/",
    "drum_loop": "/drums/breaks/",
    "drum_lp": "/drums/breaks/",
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
    "clap": "/drums/clap/",
    "klack": "/drums/clap/",
    # AFRICAN
    "slit": "/drums/oneshots/African/slits/",
    "burundi": "/drums/oneshots/African/burundi/",
    "log": "/drums/oneshots/African/logs/",
    "udu": "/drums/oneshots/African/Nigerian Udus/",
    "conga": "/drums/oneshots/African/congas/",
    "wood": "/drums/oneshots/African/wood/",
    "afr": "/drums/oneshots/African/misc",
    # Misc
    "kit": "/drums/oneshots/misc/",
    "hit": "/drums/oneshots/misc/",
    # "drum": "/drums/misc/",
    ## Wrest
    # Instruments
    "guitar": "/instruments/guitar/",
    "rhodes": "/instruments/rhodes/",
    "piano": "/instruments/piano/",
    "bass": "/instruments/bass/",
    "fx": "/instruments/FX/",
    "bleep": "/instruments/FX/",
    "horn": "/instruments/horn/",
    "arp": "/instruments/arps/",
    "string": "/instruments/strings/",
    "vocal": "/instruments/vocals/",
    "voice": "/instruments/vocals/",
    "flute": "/instruments/flute/",
    "key": "/instruments/keys/",
    "voco": "/instruments/vocals/",
    "synth": "/instruments/synths/",
    "drone": "/instruments/drone/",
    "orchestra": "/instruments/orchestra/",
    "acoustic": "/instruments/guitar/acoustic/",
    "elec": "/instruments/guitar/electric/",
    "guitar": "/instruments/guitar/",
    "gtr": "/instruments/guitar/",
    "tone": "/instruments/tone/",
    "pad": "/instruments/pad/",
    # Genres
    "house": "/genre/junk/housejunk/",
    "techno": "/genre/junk/techno/",
    "trap": "/genre/junk/trap/",
    "edm": "/genre/junk/edm/",
    "dubstep": "/genre/junk/dubstep/",
    "blues": "/genre/blues/",
    "hip": "/genre/hiphop/",
    "ambi": "/genre/ambient/",
    "funk": "/genre/funk/",
    "reggae": "/genre/reggae/",
    "jazz": "/genre/jazz/",
    # Samples
    "maj": "/samples/major/",
    "min": "/samples/minor/",
    "malice": "/samples/malice/",
    "jungle": "/samples/loops/jungle",
    "chord": "/samples/chords/",
    "drop": "/samples/drop/",
    "creak": "/samples/creak/",
    # Other
    "pluck": "/samples/pluck/",
    "pick": "/samples/picking/",
    "bpm": "/bpm/",
    "#": "/tuned/",
    # Breaks again
    "prc": "/drums/breaks",
    "perc": "/drums/breaks",
    "drums": "/drums/breaks/",
    "loop": "/samples/loop/",
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
    os.copy(fPath, newPath)
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
