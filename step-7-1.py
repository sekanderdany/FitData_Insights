# Problem Solving—Integration

# Reading the data (hourly) in a dictionary

'''
Our integration journey starts with reading the hourly data that our client has provided and loading it up into a dictionary.
'''

import numpy


def read_data_in_dict(file_name):
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str)
    data_dict = {}
    for i in range(1, len(data)):  # Write 1 instead of 0 to skip the header row
        row = data[i]
        name = row[0]
        steps = numpy.array(row[1:], dtype=int)
        data_dict[name] = steps
    return data_dict


def main():
    file_name = "steps.csv"
    hourly_data = read_data_in_dict(file_name)
    print(hourly_data)


main()
