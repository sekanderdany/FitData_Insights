# Converting hourly data to daily

'''
Eventually, we want to have one whole number per user. We currently have 168 numbers representing the steps taken per hour of the entire week. We’ll get to one number, but first, let’s slice 24 hours and sum them so that we have steps taken every day of the week instead of every hour. Notice the modular approach to our coding structure. This really comes in handy for integration. The new features keep stacking as helper functions while everything else remains as it was.
'''

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


def main():
    file_name = "steps.csv"
    hourly_data = read_data_in_dict(file_name)
    daily_data = hourly_to_daily(hourly_data)
    print(daily_data)


main()
