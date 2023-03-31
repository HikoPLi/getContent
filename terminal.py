from checkButton import CBmain
from CheckURL import CURLmain
from GetOption import ECTFmain
from restultAmount import RAmain
import rewrite


def example_switch_case(argument):
    switcher = {
        1: CBmain.main(),
        2: CURLmain.main(),
        3: ECTFmain.main(),
        4: RAmain.main()
    }
    return switcher.get(argument, "Invalid argument")


userChoice = input("Select 1, 2, 3, 4: ")
example_switch_case(userChoice)
