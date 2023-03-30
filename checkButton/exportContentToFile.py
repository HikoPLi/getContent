def exportContentToFile(data):

    try:
        with open("Content(CheckButton)" + ".txt", "a") as outfile:
            outfile.write(data + "\n")

    except:

        return False
