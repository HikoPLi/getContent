import csv
import os

# define data for the table


def csvTitle():
    os.chdir('../restultAmount/data')
    title = [
        ['UserInput', 'Page', 'Result', 'URL'],
    ]

    with open('Output.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in title:
            writer.writerow(row)


def csvContent(userInput, page, result, URL, number):

    table_data = [
        [userInput, str(page), result, URL, 'No: ' + str(number)]
    ]

    # write the data to a CSV file
    with open('Output.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        for row in table_data:
            writer.writerow(row)
