import checkResultAmount
import URL
import math

number_string = checkResultAmount.checkAmount('python')
pages = int(number_string.replace(",", ""))


loops = math.ceil(pages/30)
# print(pages)
# print(loops)
i = 1
while i < loops:
    i = i + 1

    if i == loops:
        break
