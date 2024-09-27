import numpy

data = numpy.loadtxt('data.csv', delimiter=',', dtype='str')

name = data[0]
steps = data[1:]

print(data)
steps = steps.astype(int)
print(type(steps[0]))
