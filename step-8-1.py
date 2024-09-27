# Data Science Project: Delivered
'''
One way to approach this project is by fulfilling these requirements one by one. However, that won’t be an efficient way to go about it, and we might not be able to focus on a particular feat of the project. An efficient way to go about it is by breaking down the requirements so that it gets an implementational flow.

1. Import data from a file.

2. Process imported data and store it in an appropriate data structure.

3. Compute and save relevant data:

    I. Performance statistics for requirement 3.
    II. Group containing members based on performance for requirement 4b.
    III. Sort lists of users based on their performance for requirement 4c.
3. Create the required visualizations.
'''

# Importing data from a file

'''
First, let’s satisfy requirement 1 by reading the data we need to work on. This data is in the form of a steps.csv named CSV file. It’s a good idea to take a good look at the data file before we begin.
'''


import numpy
data = numpy.loadtxt("steps.csv", delimiter=",", dtype = str)

'''
To work on any data, it’s essential that we first understand what our data looks like. So, after reading the data, we should first check if it’s of the form that we expected. For this, we can print the data, its length, or a portion of it as required.
'''


data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)

print("Length of data = ", len(data))
print("Data:\n", data)

'''
The length of data suggests that it’s a list containing eleven elements, and each element is a list in itself. Let’s now check what one of its elements looks like
'''


data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)

print("Length of an element: ", len(data[0]))
print("First element of data: ", data[0])

'''
So, the first element of data just looks like a list that informs us about the structure of data. Such a list is known as a header. According to the header, the first element of a list should contain a name, while the rest should contain the number of steps for each hour. Let’s see if the second element of the list looks like what is hinted by the header list.
'''


data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)

print("Second element of data: ", data[1])

'''
Great! So it’s just as we expected. Now, we can proceed with dealing with data and store it somewhere
'''
