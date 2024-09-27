# Computing required data

'''
Before plotting the graphs, process the data you read into the data you need to plot the visualizations. To calculate the performance statistics of individual users, you need to first obtain a list containing daily steps instead of hourly steps because that is your client’s requirement.

In the main() function, utilize the hourly_to_daily() function and make a dictionary that contains the names as keys and the daily step lists as values.
'''


import numpy


def data_to_dict(data):
    data_dict = {}
    for i in range(1, len(data)):
        row = data[i]
        name = row[0]
        steps = numpy.array(row[1:], dtype=int)
        data_dict[name] = steps
    return data_dict


def hourly_to_daily(hourly_steps):
    daily_steps = []

    for i in range(0, len(hourly_steps), 24):
        day_steps = hourly_steps[i:i+24]
        daily_step_count = sum(day_steps)
        daily_steps.append(daily_step_count)
    return daily_steps


def main():

    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)

    daily_step_dict = {}
    # The code that populates daily_step_dict using data_dict and hourly_to_daily
    for key in data_dict:
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    print(daily_step_dict)


main()




