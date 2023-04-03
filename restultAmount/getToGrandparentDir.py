import os


def grandparentDir():
    currentDir = os.path.abspath(".")
    parentDir = os.path.dirname(currentDir)
    grandparentDir = os.path.dirname(parentDir)
    os.chdir(grandparentDir)


def parentDir():
    currentDir = os.path.abspath(".")
    parentDir = os.path.dirname(currentDir)
    os.chdir(parentDir)
