import subprocess

dolphin = "C:/Users/lucy.white.207_acc/Documents/Collegg/Emulators/Dolphin-x64/Dolphin.exe" #File path to dolphin
file = "C:/Users/lucy.white.207_acc/Documents/Collegg/Game files/Kirby's Return to Dream Land (USA) (En,Fr,Es).wbfs" #File path to video game

subprocess.run(args=[dolphin, "-b", "-e", file]) #-b = without GUI, -e opens the file
