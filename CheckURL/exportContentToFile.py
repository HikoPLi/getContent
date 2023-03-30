def exportContentToFile(data):

    try:
        with open("Content(CheckURL)" + ".txt", "a") as outfile:
            outfile.write(data + "\n")

    except:

        return False
