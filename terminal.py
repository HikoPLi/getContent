from checkButton import CBmain
from CheckURL import CURLmain
from GetOption import ECTFmain
from restultAmount import RAmain
import rewrite


def choice():
    userChoice = input("Select 1, 2, 3, 4: ")
    if userChoice == "1":
        CBmain.main()

    if userChoice == "2":
        CURLmain.main()

    if userChoice == "3":
        ECTFmain.main()

    if userChoice == "4":
        RAmain.main()


choice()
