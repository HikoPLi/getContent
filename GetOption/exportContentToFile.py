def exportContentToFile(data):

    try:
        with open("Content(GetOption)" + ".txt", "a") as outfile:
            outfile.write(data + "\n")

    except:

        return False
