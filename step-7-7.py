# Plotting sorted info (name, steps, rank)

import numpy
from matplotlib import pyplot


def read_data_in_dict(file_name):
    data = numpy.loadtxt(file_name, delimiter=",", dtype=str)
    data_dict = {}
    for i in range(1, len(data)):
        row = data[i]
        name = row[0]
        steps = numpy.array(row[1:], dtype=int)
        data_dict[name] = steps
    return data_dict


# Use the helper function for hourly_to_daily
def hourly_to_daily_list(hourly_list):
    daily_steps = []
    for i in range(0, len(hourly_list), 24):
        day_steps = hourly_list[i:i+24]
        daily_step_count = sum(day_steps)
        daily_steps.append(daily_step_count)
    return daily_steps


def hourly_to_daily(hourly_dict):
    daily_dict = {}
    for user_name in hourly_dict:
        daily_dict[user_name] = hourly_to_daily_list(hourly_dict[user_name])
    return daily_dict


def reduce_daily_to_weekly_dict(daily_data):
    new_dict = {}
    for key in daily_data:
        new_dict[key] = sum(daily_data[key])
    return new_dict


def compile_user_steps_lists(weekly_data):
    user_names_list = []
    user_steps_list = []
    for key in weekly_data:
        user_names_list.append(key)
        user_steps_list.append(weekly_data[key])
    return user_names_list, user_steps_list


def return_min_index(input_list):  # helper function for mySort
    current_min = input_list[0]
    min_index = 0
    for i in range(len(input_list)):
        if input_list[i] < current_min:
            current_min = input_list[i]
            min_index = i
    return min_index


def my_sort(user_names, user_steps):
    sorted_user_names = []
    sorted_user_steps = []
    for i in range(len(user_steps)):
        min_index = return_min_index(user_steps)
        sorted_user_names.append(user_names[min_index])
        sorted_user_steps.append(user_steps[min_index])
        user_steps[min_index] = float("inf")
    return sorted_user_names, sorted_user_steps


def print_sorted_info(user_names, user_steps):
    for i in range(len(user_steps)):
        print(user_names[i], "has taken", user_steps[i],
              "in the week, and stands at rank:", i)


def plot_sorted_info(user_names, user_steps):
    pyplot.bar(user_names, user_steps)
    pyplot.show()


def main():
    file_name = "steps.csv"
    hourly_data = read_data_in_dict(file_name)
    daily_data = hourly_to_daily(hourly_data)
    weekly_data = reduce_daily_to_weekly_dict(daily_data)
    user_names, user_steps = compile_user_steps_lists(weekly_data)
    sorted_user_names, sorted_user_steps = my_sort(user_names, user_steps)
    print_sorted_info(sorted_user_names, sorted_user_steps)
    plot_sorted_info(sorted_user_names, sorted_user_steps)


main()
