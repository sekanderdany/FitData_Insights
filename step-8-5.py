# Categorizing data

'''
Categorize the users into three groups based on their average number of steps in a week. Complete a choose_categories() named function to find the group that takes in avg_list and returns a dictionary for the number of members in each category. The categories are defined as follows:

 - Below 5,000 steps are concerning.

 - 5,000 steps or above but below 10,000 are average.

 - 10,000 or more steps are excellent.
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


def choose_categories(avg_list):
    categories = {"concerning": 0, "average": 0, "excellent": 0}
    # Using loop to iterate over the loop
    for avg_steps in avg_list:
        # Using conditionals and comparison operators to categorize each value.
        if avg_steps < 5000:
            categories["concerning"] = categories["concerning"] + 1
        elif 5000 <= avg_steps < 10000:
            categories["average"] = categories['average'] + 1
        else:
            categories["excellent"] = categories["excellent"] + 1

    return categories


def main():

    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)

    daily_step_dict = {}
    for key in data_dict.keys():
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    stats_dict = compute_stats(daily_step_dict)

    # Separating out a list of averages
    avg_list = []
    for name in stats_dict:
        stats = stats_dict[name]
        avg_list.append(stats["average"])

    # Calling the categorizing function and storing it's output in a variable
    categories = choose_categories(avg_list)

    print("Members in each group:", categories)


main()
