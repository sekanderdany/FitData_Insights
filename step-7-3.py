# Computing a dictionary—one weekly entry per user

import numpy


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


def main():
    file_name = "steps.csv"
    hourly_data = read_data_in_dict(file_name)
    daily_data = hourly_to_daily(hourly_data)
    weekly_data = reduce_daily_to_weekly_dict(daily_data)
    print(weekly_data)


main()
