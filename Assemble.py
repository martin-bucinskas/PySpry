#!/usr/bin/python

from scripts import ASMScript
from scripts import ASMLibs
from scripts import Setup
import os

userInput = "";

def main():
    while userInput != 'q':
        print("PyMyOS - Operating System builder!");
        print("Version: 0.1");

        showMenu();
        getUserInput();

        input("Press any key to continue.");
        clearScreen();

def showMenu():
    print();
    print("1. Assemble bootloader");
    print("2. Assemble ASM libraries");
    print("3. Compile kernel");
    print("4. Compile kernel libraries");
    print("5. Create a floppy image");
    print("6. Copy the bootloader to the floppy image");
    print("SETUP. Setup the directories and the files required.");
    print("h. Help");
    print("q. Quit");

def clearScreen():
    os.system('cls');

def getUserInput():
    global userInput;
    userInput = input(">> ");
    options[userInput]();

def assembleBootloader():
    clearScreen();
    ASMScript.assemble();

def assembleASMLibs():
    clearScreen();
    ASMLibs.assemble();

def compileKernel():
    pass;

def compileKernelLibs():
    pass;

def createFloppyImg():
    pass;

def copyBootToFloppy():
    pass;

def setup():
    clearScreen();
    Setup.createDirs();

def displayHelp():
    pass;

def quitProg():
    pass;

options = {"1" : assembleBootloader,
           "2" : assembleASMLibs,
           "3" : compileKernel,
           "4" : compileKernelLibs,
           "5" : createFloppyImg,
           "6" : copyBootToFloppy,
           "SETUP" : setup,
           "h" : displayHelp,
           "q" : quitProg,
           }

if __name__ == "__main__":
    main();
