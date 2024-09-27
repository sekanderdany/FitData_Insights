# Computing performance statistics

'''
Now, proceed to calculate the statistics for the data. While calculating statistics at the end of the “Importing Libraries” chapter, we calculated the statistics one by one in the main() function. Doing that for all ten members will mess up the structure of your code, making it hard to read, understand, and reuse. To tackle this issue, make a function that will take in the data_dict dictionary and return another dictionary. This output dictionary will have member names as keys, and the values will be another dictionary of statistics.
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


def compute_stats(step_dict):
    stats_dict = {}
    for key, value in step_dict.items():
        stats_dict[key] = {"min": min(value), "max": max(
            value), "average": numpy.mean(value)}

    return stats_dict


def main():

    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)

    daily_step_dict = {}
    for key in data_dict:
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    stats_dict = compute_stats(daily_step_dict)
    for key in stats_dict:
        print(key, stats_dict[key])


main()
