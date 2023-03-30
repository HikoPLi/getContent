from checkButton import CBmain
from CheckURL import CURLmain
from GetOption import ECTFmain
from restultAmount import RAmain
import rewrite


def choice(input):

    if input == "1":
        CBmain.main()
        rewrite.rewrite()

    if input == "2":
        CURLmain.main()
        rewrite.rewrite()

    if input == "3":
        ECTFmain.main()
        rewrite.rewrite()

    if input == "4":
        RAmain.main()
        rewrite.rewrite()


userChoice = input("Select 1, 2, 3, 4: ")
choice(userChoice)
