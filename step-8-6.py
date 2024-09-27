# Sorting data

'''
Sorting data is required to plot the bar chart that compares the performance of users. For this part, make a my_sort() named function that takes in a couple of lists, one containing the step counts and the other containing user names, and returns sorted versions of those lists. Furthermore, to sort the two lists, it might be a good choice to make a find_min_index() named helper function that provides the index for the minimum value’s location in the provided steps list.
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


def find_min_index(input_list):  # Use the helper function for mySort

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
        # Appending minimum value and the corresponding user_name to the lists
        sorted_user_names.append(user_names[min_index])
        sorted_user_steps.append(user_steps[min_index])
        # Substituting the used value with an appropriate placeholder
        user_steps[min_index] = float("inf")

    return sorted_user_names, sorted_user_steps


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

    # Relevant list formation and function calls
    unsorted_names = list(total_step_dict.keys())
    unsorted_steps = list(total_step_dict.values())
    sorted_names, sorted_steps = my_sort(unsorted_names, unsorted_steps)

    for i in range(len(sorted_names)):
        print(sorted_names[i], sorted_steps[i])


main()
