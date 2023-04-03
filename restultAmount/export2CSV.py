import csv
import os
import getToGrandparentDir

# define data for the table


def csvTitle():
    # getToGrandparentDir.grandparentDir()
    # os.chdir(f'../restultAmount/data')
    title = [
        ['UserInput', 'Page', 'Result', 'URL'],
    ]

    with open('Output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in title:
            writer.writerow(row)
    getToGrandparentDir.parentDir()


def csvContent(userInput, page, result, URL, number):

    # if number == 1:
    #     getToGrandparentDir.grandparentDir()

    table_data = [
        [userInput, str(page), result, URL, 'No: ' + str(number)]
    ]

    # write the data to a CSV file
    with open('Output.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for row in table_data:
            writer.writerow(row)
