# Visualizing data

'''
With data all stored in appropriate data structures, start working on requirement 4, which is the main gist of this project.

Line plot for a day’s activity
For this requirement, pick a 24-value portion for any user and plot it using the matplotlib library. Start with the line plot for a particular user on a particular day.
'''

import numpy
from matplotlib import pyplot


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
    for avg_steps in avg_list:
        if avg_steps < 5000:
            categories["concerning"] = categories["concerning"] + 1
        elif 5000 < avg_steps < 10000:
            categories["average"] = categories['average'] + 1
        else:
            categories["excellent"] = categories["excellent"] + 1
    return categories


def daily_to_total(daily_steps):
    total_dict = {}
    for name, steps in daily_steps.items():
        total_dict[name] = sum(steps)
    return total_dict


def find_min_index(input_list):  # helper function for mySort
    current_min = input_list[0]
    index = 0
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]
            index = i
    return index


def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    for i in range(len(user_steps)):
        min_index = find_min_index(user_steps)
        sorted_user_names.append(user_names[min_index])
        sorted_user_steps.append(user_steps[min_index])
        user_steps[min_index] = float("inf")
    return sorted_user_names, sorted_user_steps


def plot_line(steps, save_path=""):
    # Making a list of hours in a day
    hour_list = range(24)
    # Making the line plot and defining the required labels
    pyplot.plot(hour_list, steps)
    pyplot.title("Performance over the day")
    pyplot.xlabel("Hour of the day")
    pyplot.ylabel("Number of steps")
    pyplot.savefig(save_path+"plot_line.png")
    pyplot.close()


def main():

    data = numpy.loadtxt("steps.csv", delimiter=",", dtype=str)
    data_dict = data_to_dict(data)

    daily_step_dict = {}
    for key in data_dict.keys():
        daily_step_dict[key] = hourly_to_daily(data_dict[key])

    stats_dict = compute_stats(daily_step_dict)

    avg_list = []
    for name in stats_dict:
        stats = stats_dict[name]
        avg_list.append(stats["average"])

    categories = choose_categories(avg_list)

    total_step_dict = daily_to_total(daily_step_dict)

    unsorted_names = list(total_step_dict.keys())
    unsorted_steps = list(total_step_dict.values())
    sorted_names, sorted_steps = my_sort(unsorted_names, unsorted_steps)

    # List preparation and function call for line plot
    steps = data_dict["Juliana"][0:24]
    plot_line(steps, save_path="e:/Documents & Learning/Python/FitData Insights/")


main()
