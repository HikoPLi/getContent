
def exportContentToFile(data):

    try:

        with open("Content(RestultAmount)" + ".txt", "a") as outfile:
            outfile.write(data + "\n")

    except:

        return False
