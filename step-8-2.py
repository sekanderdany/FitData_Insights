# Storing data

'''
Each list from this data seems exactly like the one that you dealt with in the previous lessons, and you learned an efficient way of storing this data, i.e., in the form of dictionaries. Make a function that takes in the data that contains lists of integers, changes the data type as required, and returns a dictionary. The key should be the name of the member, and the value should be a list of 168 integers.
'''

import numpy


def data_to_dict(data):
    data_dict = {}
    for i in range(1, len(data)):
        row = data[i]
        name = row[0]
        steps = numpy.array(data[i][1:], dtype=int)
        data_dict[name] = steps  # adding a key:value pair to the dictionary
    return data_dict


data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
data_dict = data_to_dict(data)

# printing to make sure we have the correct data in our dict
print(data_dict)


'''
Now that you’ve made a function, it’s a good time to start putting it in its rightful place in the program structure. Define a function that will maintain the overall flow of your program; call it main(). The main() function will also be used to test other component functions that you’re making along the way. Place the required code to print the output of the dict_to_data() function in the main() function. To execute your program, call the main() function at the end of the code.
'''


def data_to_dict(data):
    data_dict = {}
    for i in range(1, len(data)):
        row = data[i]
        name = row[0]
        steps = numpy.array(row[1:], dtype=int)
        data_dict[name] = steps
    return data_dict


def main():
    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)
    print(data_dict)


main()

'''
Great! So, all of your data is in the form of a dictionary now, and you can easily access the steps simply by using the name of the member. Now, move toward summary statistics.
'''
